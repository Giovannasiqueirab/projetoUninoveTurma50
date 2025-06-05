# faq_bot.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =====================================================================
# 1) Monte aqui seu conjunto de Perguntas (FAQ) e Respostas correlatas
# =====================================================================
faq = {
    # Pergunta (em minúsculas) : Resposta correspondente
    "qual dose de npk para milho em 1 hectare": 
        "Para milho, utiliza-se em média 100 kg de NPK 20-05-20 por hectare.",

    "qual dose de npk para soja em 1 hectare": 
        "Para soja, recomenda-se cerca de 50 kg de NPK 20-05-20 por hectare.",

    "quando plantar milho na região sudeste": 
        "No Sudeste, a melhor época de plantio do milho costuma ser entre setembro e outubro.",

    "como calcular custo de insumos para 2 hectares":
        "Multiplique a quantidade de insumo por hectare pelo preço unitário e depois por 2 hectares.",

    "quais os insumos necessários para plantio de cenoura":
        "Para cenoura, normalmente recomenda‐se 0.1 tonelada de NPK 4-14-8 e 0.05 tonelada de potássio por hectare.",

    "como calcular area em hectares": 
        "Para converter m² em hectares, divida a área em metros quadrados por 10 000 (por exemplo, 25 000 m² = 2.5 ha).",

    "qual epoca ideal de plantio de feijao": 
        "A época ideal de plantio do feijão varia conforme a safra, mas geralmente ocorre entre janeiro e março.",

    "qual espaçamento para abobora": 
        "Para abóbora, use espaçamento médio de 0.1 m entre plantas e 0.8 m entre fileiras.",

    # Você pode adicionar quantas entradas desejar...
}

# =====================================================================
# 2) Preparação do modelo TF-IDF e da matriz de vetores TF-IDF
# =====================================================================
perguntas = list(faq.keys())

# Cria o modelo/vectorizer (para converter texto → vetor TF-IDF)
vectorizer_model = TfidfVectorizer()

# Ajusta (fit) o modelo às perguntas do FAQ e armazena a matriz resultante
tfidf_matrix = vectorizer_model.fit_transform(perguntas)


def iniciar_faq_bot():
    """
    Inicia o loop de interação com o usuário:
    - Lê a pergunta digitada
    - Transforma em vetor TF-IDF usando o vectorizer_model
    - Calcula similaridade entre esse vetor e todos os vetores do FAQ (tfidf_matrix)
    - Se encontrar pontuação (score) alta o suficiente, exibe a resposta; 
      caso contrário, pede para reformular.
    Para sair, digite 'sair' ou 'voltar'.
    """
    print("\n=== Assistente FAQ (TF-IDF) ===")
    print("Digite sua pergunta sobre plantio, insumos ou área. (ou 'sair' para voltar ao menu)\n")

    while True:
        texto_usuario = input("Você: ").strip().lower()
        if texto_usuario in ["sair", "voltar", "exit"]:
            print("Voltando ao menu principal...\n")
            return  # Encerra o FAQ-Bot e volta ao menu

        # Converte a pergunta do usuário em vetor TF-IDF usando o mesmo model que treinamos
        vetor_usuario = vectorizer_model.transform([texto_usuario])

        # Calcula similaridade de cosseno (1×N) entre vetor_usuario e cada linha de tfidf_matrix
        similaridades = cosine_similarity(vetor_usuario, tfidf_matrix).flatten()

        # Índice da pergunta do FAQ com maior similaridade
        idx_max = similaridades.argmax()
        score_max = similaridades[idx_max]

        # Limiar de similaridade mínimo (ajuste conforme necessidade; 0.20 é razoável para FAQ)
        if score_max < 0.20:
            print("Bot: Desculpe, não entendi exatamente. Você pode reformular?\n")
        else:
            pergunta_mais_proxima = perguntas[idx_max]
            resposta = faq[pergunta_mais_proxima]
            print(f"Bot: {resposta}\n")
