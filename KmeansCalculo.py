import random

import pandas as pd

from Formulas import Formulas


class KmeansCalculo:

    def __init__(self, conjunto: pd.DataFrame):
        self.x = None
        self.y = None
        self.N = None
        self.conjunto: pd.DataFrame = conjunto
        self.centroids = None
        self.matriz = None

    def fit_k_means(self, qt_centroids: list, parada: int, max_iter: int):

        colunm_x: str = 'cases'
        colunm_y: str = 'deaths'

        # pontos: conjunto de pontos 2D (casos x mortes) que serão clusterizados
        self.N = len(self.conjunto)
        self.x = self.conjunto[colunm_x].values
        self.y = self.conjunto[colunm_y].values

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

    def lista_distancia_centroids(self, conjunto: pd.DataFrame, centroids: list, colunm_x: str = 'cases',
                                  colunm_y: str = 'deaths'):

        total_conjuntos: int = len(conjunto)
        total_centroides: int = len(centroids)

        matriz = []
        for item_p in range(0, total_conjuntos):
            for item_c in range(0, total_centroides):
                ponto_conjunto = [self.conjunto[colunm_x][item_p], self.conjunto[colunm_y][item_p]]
                ponto_centroid = [centroids[item_c][0], centroids[item_c][1]]
                dist = Formulas().distancia_ponto_centroid(ponto_conjunto, ponto_centroid)
                matriz.append(
                    [[self.conjunto[colunm_x][item_p], self.conjunto[colunm_y][item_p]], centroids[item_c], dist])

        matriz = pd.DataFrame(matriz, columns=['ponto', 'centroid', 'dist'])

        return matriz

    def distribuir_pontos_centroids(self, matriz: pd.DataFrame):
        self.matriz = matriz

        matriz = matriz.sort_values(by='dist')
        for index, row in matriz.iterrows():
            print(f"ponto: {row.ponto}, centroid: {row.centroid}, dist: {row.dist}")
