# cultura.py

class Cultura:
    def __init__(self, nome, base_plantio, espacamento):
        self.nome = nome
        self.base_plantio = base_plantio
        self.espacamento = espacamento

    def calcular_area(self, comprimento, largura):
        if self.base_plantio == "quadrado":
            return comprimento * comprimento
        elif self.base_plantio == "retangulo":
            return comprimento * largura
        elif self.base_plantio == "triangulo":
            return (comprimento * largura) / 2
        elif self.base_plantio == "hexagono":
            return (3 * (comprimento ** 2) * (3 ** 0.5)) / 2
        elif self.base_plantio == "linhas_paralelas":
            return comprimento * largura
        else:
            raise ValueError("Base de plantio não suportada.")

    def calcular_insumos(self, area):
        # 'area' está em hectares
        if self.nome.lower() in ["cenoura"]:
            npk = 0.1 * area
            potassio = 0.05 * area
            return {"NPK 4-14-8": npk, "Potássio": potassio}
        elif self.nome.lower() in ["abóbora", "abobora"]:
            npk = 0.1 * area
            nitrogenio = 0.07 * area
            return {"NPK 4-14-8": npk, "Nitrogênio": nitrogenio}
        elif self.nome.lower() in ["cana-de-açúcar", "cana-de-acucar", "cana de açúcar", "cana de acucar"]:
            fosforo = (3 * area) / 1000
            nitrogenio = (8 * area) / 1000
            potassio = (10 * area) / 1000
            return {"Fósforo (P2O5)": fosforo, "Nitrogênio (N)": nitrogenio, "Potássio (K2O)": potassio}
        elif self.nome.lower() in ["algodão", "algodao"]:
            fosforo = (4 * area) / 1000
            nitrogenio = (6 * area) / 1000
            potassio = (8 * area) / 1000
            return {"Fósforo (P2O5)": fosforo, "Nitrogênio (N)": nitrogenio, "Potássio (K2O)": potassio}
        else:
            return {}
