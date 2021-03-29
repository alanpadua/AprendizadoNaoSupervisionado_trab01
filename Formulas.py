from mpmath import mp


class Formulas:

    @staticmethod
    def calcula_hipotenusa(a: float, b: float):
        hipotenusa = ((a * a) + (b * b))
        return hipotenusa

    @staticmethod
    def distancia_ponto_centroid(ponto_conjunto: list, ponto_centroid: list):
        # ponto_conjunto x1 e y1
        x1 = ponto_conjunto[0]
        y1 = ponto_conjunto[1]
        # print(f" x1 e y1: {x1}, {y1}")

        # ponto_centroid x2 e y2
        x2 = ponto_centroid[0]
        y2 = ponto_centroid[1]
        # print(f" x2 e y2: {x2}, {y2}")

        distancia = mp.sqrt(mp.exp(x1 - x2) + mp.exp(y1 - y2))
        # distancia = math.sqrt(math.exp(x1 - x2) + math.exp(y1 - y2))

        return distancia
