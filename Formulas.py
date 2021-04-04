import numpy as np
from scipy.spatial import distance


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

        # ponto_centroid x2 e y2
        x2 = ponto_centroid[0]
        y2 = ponto_centroid[1]

        # distancia = np.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        # return distancia

        return distance.euclidean(ponto_conjunto, ponto_centroid)
