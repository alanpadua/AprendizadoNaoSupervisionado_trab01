import random

import pandas as pd
from mpmath import mp


class KmeansCalculo:

    def __init__(self, conjunto: pd.DataFrame):
        self.s = '3'
        self.x = None
        self.y = None
        self.N = None
        self.conjunto = conjunto
        self.centroids = None
        self.matriz = None

    def calcula_hipotenusa(self, a: float, b: float):
        hipotenusa = ((a * a) + (b * b))
        return hipotenusa

    def fit_k_means(self, qt_centroids: list, parada: int, max_iter: int, max_item_conjunto: int = None, filtro: str = ''):

        # print("aqui")
        # print(len(self.conjunto))
        # # self.conjunto = self.conjunto.query("cases > 1")
        # print(len(self.conjunto))
        # print("aqui fim")

        colunm_x: str = 'cases'
        colunm_y: str = 'deaths'

        # pontos: conjunto de pontos 2D (casos x mortes) que serão clusterizados
        if max_item_conjunto != None:
            # print(f" max_item_conjunto={max_item_conjunto}")
            self.conjunto = self.conjunto[0: max_item_conjunto]

        self.N = len(self.conjunto)
        self.x = self.conjunto[colunm_x].values
        self.y = self.conjunto[colunm_y].values

        # print(self.N)
        # print(self.x)
        # print(self.y)

        centroids = self.gerar_pontos_centroids(qt_centroids)
        matrix = self.lista_distancia_centroids(self.conjunto, centroids)

        return self.x, self.y, self.N, matrix

    def gerar_pontos_centroids(self, quantidade_pontos: int = 3):
        max_x = self.x.max()
        max_y = self.y.max()

        centroids = []
        for z in range(quantidade_pontos):
            rand_x = random.randint(0, max_x)
            rand_y = random.randint(0, max_y)
            centroids.append([rand_x, rand_y])

        # print(pontos)
        return centroids

    def distancia_ponto_centroid(self, ponto_conjunto: list, ponto_centroid: list):

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

    def lista_distancia_centroids(self, conjunto: pd.DataFrame, centroids: list, colunm_x: str = 'cases',
                                  colunm_y: str = 'deaths'):

        total_conjuntos: int = len(conjunto)
        total_centroides: int = len(centroids)

        matriz = []
        for item_p in range(0, total_conjuntos):
            # print(f"Item: {item_p} ")
            # print(f"casos:{self.conjunto[colunm_x][item_p]}")
            # print(f"deaths:{self.conjunto[colunm_y][item_p]}")
            for item_c in range(0, total_centroides):
                # print(f"Centroid: {centroids[item_c]}")
                # print(f"Item P: {item_p}")
                # print(f"Item C: {item_c}")
                ponto_conjunto = [self.conjunto[colunm_x][item_p], self.conjunto[colunm_y][item_p]]
                ponto_centroid = [centroids[item_c][0], centroids[item_c][1]]
                dist = self.distancia_ponto_centroid(ponto_conjunto, ponto_centroid)
                matriz.append(
                    [[self.conjunto[colunm_x][item_p], self.conjunto[colunm_y][item_p]], centroids[item_c], dist])

        matriz = pd.DataFrame(matriz, columns=['ponto', 'centroid', 'dist'])

        print(type(matriz))
        return matriz

    def distribuir_pontos_centroids(self, matriz: pd.DataFrame):
        self.matriz = matriz

        # id_numbers = matriz.
        # id_numbers.nunique()

        matriz = matriz.sort_values(by='dist')
        for index, row in matriz.iterrows():
             print(f"ponto: {row.ponto}, centroid: {row.centroid}, dist: {row.dist}")
