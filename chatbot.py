# chatbot.py

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

def iniciar_chatbot():
    bot = ChatBot(
        'AgroBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database_chatbot.sqlite3',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'Desculpe, não entendi. Pode reformular?',
                'maximum_similarity_threshold': 0.90
            }
        ],
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace'
        ],
        read_only=False
    )

    # Treina com o corpus em português
    trainer = ChatterBotCorpusTrainer(bot)
    trainer.train('chatterbot.corpus.portuguese')

    # Frases customizadas para o contexto agrícola
    custom_trainer = ListTrainer(bot)
    exemplos = [
        "Qual dose de NPK para milho em 1 hectare?",
        "Para milho aplicamos 100 kg de NPK 20-05-20 por hectare.",
        "Como calcular insumos para 2 hectares de soja?",
        "Para 2 hectares de soja, multiplique 50 kg/ha × 2 ha = 100 kg.",
        "Quando é a melhor época de plantio de feijão?",
        "A época ideal varia conforme a região, mas geralmente entre janeiro e março.",
        "Qual o custo estimado de insumos para 3 hectares de café?",
        "Calcule 3 ha × (kg de insumo/ha) × preço/kg para obter o custo total."
    ]
    custom_trainer.train(exemplos)

    return bot

def conversar_com_bot(bot):
    print("\n=== Bem-vindo ao Assistente Virtual AgroBot ===")
    print("Digite sua pergunta (ou 'sair' para voltar ao menu principal):\n")

    while True:
        try:
            pergunta = input("Você: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nVoltando ao menu principal.\n")
            break

        if pergunta.lower() in ['sair', 'voltar', 'exit']:
            print("Voltando ao menu principal...\n")
            break

        resposta = bot.get_response(pergunta)
        print(f"AgroBot: {resposta}\n")
