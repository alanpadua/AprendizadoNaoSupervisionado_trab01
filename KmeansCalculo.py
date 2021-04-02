import random

import numpy
import numpy as np
import pandas as pd
import operator as op

from Formulas import Formulas


class KmeansCalculo:

    def __init__(self, conjunto: pd.DataFrame, max_iter: int = 10, parada: int = 10):
        self.X = None
        self.y = None
        self.N = None
        self.K = None
        self.conjunto: pd.DataFrame = conjunto
        self.centroids: list = None
        self.matriz: list = None

        self.max_iter = max_iter
        self.parada = parada

    def fit_k_means(self, qt_centroids: int):
        colunm_x: str = 'cases'
        colunm_y: str = 'deaths'

        # pontos: conjunto de pontos 2D (casos x mortes) que serão clusterizados
        self.N = len(self.conjunto)
        self.X = self.conjunto[colunm_x].values
        self.y = self.conjunto[colunm_y].values

        self.centroids = self.gerar_pontos_centroids(qt_centroids)
        self.matriz = self.lista_distancia_centroids(self.conjunto)

        return self.X, self.y, self.N, self.centroids, self.matriz

    def gerar_pontos_centroids(self, quantidade_pontos: int = 3):
        max_x = self.X.max()
        max_y = self.y.max()
        self.K = quantidade_pontos

        self.centroids = []
        for z in range(quantidade_pontos):
            rand_x = random.randint(0, max_x)
            rand_y = random.randint(0, max_y)
            self.centroids.append([rand_x, rand_y])

        return sorted(self.centroids)

    def lista_distancia_centroids(self, conjunto: pd.DataFrame, colunm_x: str = 'cases', colunm_y: str = 'deaths'):
        """
        matriz:
            Colunas: ponto_x  ponto_y  centroid_x  centroid_y          dist
        :param conjunto:
        :param colunm_x:
        :param colunm_y:
        :return:
        """
        total_conjuntos: int = len(conjunto)
        total_centroides: int = len(self.centroids)

        matriz = []
        for item_p in range(0, total_conjuntos):
            menor_distancia = 0
            row = None
            print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
            for _centroid in range(0, total_centroides):
                print("===============================================")
                ponto_conjunto = [self.conjunto[colunm_x][item_p], self.conjunto[colunm_y][item_p]]
                ponto_centroid = [self.centroids[_centroid][0],     self.centroids[_centroid][1]]
                dist = Formulas().distancia_ponto_centroid(ponto_conjunto, ponto_centroid)
                print(f"menor_distancia: {menor_distancia}")
                print(f"dist: {dist}")
                print(f"Condição 1: dist <= menor_distancia: {dist <= menor_distancia}")
                print(f"Condição 2: row == None: {row == None}")
                # if dist <= menor_distancia or row == None:

                if op.lt(dist, menor_distancia) or row == None:
                    print("########")
                    menor_distancia = dist
                    print("centroid_" + _centroid.__str__())
                    row = [self.conjunto[colunm_x][item_p], self.conjunto[colunm_y][item_p],
                           self.centroids[_centroid][0], self.centroids[_centroid][1],
                           "centroid_" + _centroid.__str__(),
                           dist]
                    print("#######")
            matriz.append(row)

        matriz = pd.DataFrame(matriz, columns=['ponto_x', 'ponto_y', 'centroid_x', 'centroid_y', 'centroid_id', 'dist'])

        return matriz

    def lista_centroids_mais_proximos(self, matriz: pd.DataFrame):
        df = matriz.squeeze()
        centroides = [centroides for centroides in df['centroid'].astype('str').unique()]

        resultado = [[], [], []]
        for centroid in centroides:
            sorted_df = df[df['centroid'].astype('str') == centroid]
            # sorted_df = df[df['centroid'] == centroid]
            sorted_df['ponto'] = sorted_df['ponto'].astype('str')
            sorted_df['centroid'] = sorted_df['centroid'].astype('str')
            sorted_df['dist'] = sorted_df['dist'].astype('float64')
            sorted_df = sorted_df.drop_duplicates()
            sorted_df = sorted_df.sort_values(by=['dist'])
            resultado.append([centroid, sorted_df['ponto'].to_list()[0]])

        # resultado = pd.DataFrame(resultado, columns=['centroid', 'ponto'])
        return resultado
