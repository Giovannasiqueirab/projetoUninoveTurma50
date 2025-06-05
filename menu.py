# menu.py

from cadastro import cadastrar_cultura
from plantio import adicionar_dados
from faq_bot import iniciar_faq_bot   # <— importa o arquivo faq_bot.py

def mostrar_menu():
    print("\n=== Sistema de Gestão Agrícola ===")
    print("1. Cadastrar Cultura")
    print("2. Visualizar Culturas")
    print("3. Adicionar Plantio")
    print("4. Visualizar Plantios")
    print("5. Assistente Virtual (FAQ‐Bot)")
    print("0. Sair")

def selecionar_opcao():
    return input("Escolha uma opção: ").strip()

def menu_principal():
    culturas = []
    plantios = []

    while True:
        mostrar_menu()
        escolha = selecionar_opcao()

        if escolha == '1':
            cultura = cadastrar_cultura()
            if cultura:
                culturas.append(cultura)
                print(f"\n✅ Cultura '{cultura.nome}' cadastrada com sucesso!")

        elif escolha == '2':
            if not culturas:
                print("\n❗ Nenhuma cultura cadastrada.")
            else:
                print("\n🌱 Culturas Cadastradas:")
                for i, c in enumerate(culturas, start=1):
                    print(f"{i}. Nome: {c.nome} | Base: {c.base_plantio} | Espaçamento: {c.espacamento}")

        elif escolha == '3':
            plantio = adicionar_dados(culturas)
            if plantio:
                plantios.append(plantio)
                print("\n✅ Plantio cadastrado com sucesso!")

        elif escolha == '4':
            if not plantios:
                print("\n❗ Nenhum plantio registrado.")
            else:
                print("\n🌾 Plantios Registrados:")
                for i, p in enumerate(plantios, start=1):
                    c = p['cultura']
                    print(f"{i}. Cultura: {c.nome} | Área: {p['area_m2']:.2f} m² ({p['area_ha']:.2f} ha)")
                    if p['insumos']:
                        print("   Insumos necessários:")
                        for insumo, qtd in p['insumos'].items():
                            print(f"   - {qtd:.2f} kg de {insumo}")
                    else:
                        print("   Nenhum insumo necessário.")

        elif escolha == '5':
            iniciar_faq_bot()   # <— chama o FAQ-Bot

        elif escolha == '0':
            print("\n👋 Saindo do sistema. Até a próxima!")
            break

        else:
            print("\n❗ Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu_principal()
