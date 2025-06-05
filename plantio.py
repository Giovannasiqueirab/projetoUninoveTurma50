# plantio.py

from cultura import Cultura

def adicionar_dados(culturas):
    """
    Recebe a lista de objetos Cultura já cadastrados.
    - Se não houver nenhuma cultura, bloqueia o cadastro de plantio.
    - Pergunta ao usuário qual cultura usar, pede as dimensões,
      calcula a área em m² e em hectares, e imprime os insumos.
    Retorna um dicionário com as informações do plantio ou None se cancelar.
    """

    if not culturas:
        print("\nNenhuma cultura cadastrada. Cadastre uma cultura primeiro.")
        return None  # Sai da função caso não haja culturas

    # Exibe as culturas cadastradas para que o usuário escolha uma
    print("\nCulturas cadastradas:")
    for i, cultura in enumerate(culturas, start=1):
        print(f"{i}. {cultura.nome} ({cultura.base_plantio})")

    # Solicita ao usuário escolher a cultura
    try:
        escolha = int(input("Escolha o número da cultura para o plantio: ")) - 1
        if escolha < 0 or escolha >= len(culturas):
            print("Escolha inválida!")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None

    cultura = culturas[escolha]

    # Solicita as dimensões em metros
    try:
        comprimento = float(input("Digite o comprimento da área de plantio (em metros): "))
        largura = float(input("Digite a largura da área de plantio (em metros): "))
    except ValueError:
        print("Valores inválidos. Informe números válidos para comprimento e largura.")
        return None

    # Calcula a área em m² usando a própria classe Cultura
    area_m2 = cultura.calcular_area(comprimento, largura)
    area_ha = area_m2 / 10000  # converte de m² para hectares

    print(f"\nÁrea de plantio: {area_m2:.2f} m² ({area_ha:.2f} ha)")

    # Calcula os insumos por hectare (o método já espera hectares)
    insumos = cultura.calcular_insumos(area_ha)
    if insumos:
        print("\nInsumos necessários:")
        for insumo, quantidade in insumos.items():
            print(f"- {quantidade:.2f} kg de {insumo}")
    else:
        print("Nenhum insumo necessário para esta cultura.")

    # Retorna um dicionário com todas as informações para que o menu possa armazenar
    return {
        'cultura': cultura,
        'area_m2': area_m2,
        'area_ha': area_ha,
        'insumos': insumos
    }
