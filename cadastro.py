# cadastro.py
from cultura import Cultura

def cadastrar_cultura():
    nome = input("Digite o nome da cultura: ").strip().capitalize()

    print("\nEscolha a base de plantio:")
    print("A. Quadrado")
    print("B. Retângulo")
    print("C. Triângulo Equilátero")
    print("D. Hexágono")
    print("E. Linhas Paralelas")

    escolha_base = input("Digite a letra correspondente à base de plantio: ").strip().lower()

    if escolha_base == "a":
        base_plantio = "quadrado"
        espacamento = "2m x 2m"
    elif escolha_base == "b":
        base_plantio = "retangulo"
        espacamento = "80 cm entre linhas e 30 cm entre plantas"
    elif escolha_base == "c":
        base_plantio = "triangulo"
        espacamento = "3 cm entre plantas e 20 cm entre fileiras"
    elif escolha_base == "d":
        base_plantio = "hexagono"
        espacamento = "20-30 cm entre plantas"
    elif escolha_base == "e":
        base_plantio = "linhas_paralelas"
        espacamento = "70-80 cm entre fileiras e 20-25 cm entre plantas"
    else:
        print("Opção inválida!")
        return None

    return Cultura(nome, base_plantio, espacamento)
