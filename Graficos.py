import random

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import mpld3
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from mpld3 import plugins


class Graficos:

    def __init__(self):
        self.x: str = 'x'
        self.cores = {'blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink',
                      'gray',
                      'olive', 'cyan'}

    def plot_seaborn(self, conjunto: pd.DataFrame):
        plot_df = conjunto.reset_index()

        plot_dims = (20, 10)
        fig, ax = plt.subplots(figsize=plot_dims)

        sns.scatterplot(x='cases', y='deaths', data=plot_df, ax=ax) \
            .set(title='Relação entre casos e mortes nos condados americanos por COVID-19', xlabel='Casos de COVID-19',
                 ylabel='Mortes por COVID-19');

        plt.show()

    def plot_scatter(self, conjunto: pd.DataFrame):
        fig = px.scatter(conjunto, x='cases', y='deaths', hover_name='county')

        fig.update_layout(
            title='Relação entre casos e mortes nos condados americanos por COVID-19',
            xaxis_title="Casos de COVID-19",
            yaxis_title="Mortes por COVID-19",
        )

        fig.show()

    def mpld3(self, conjunto: pd.DataFrame):
        plot_dims = (20, 10)
        fig, ax = plt.subplots(figsize=plot_dims)
        ax.grid(True, alpha=0.3)

        labels = conjunto['county'].tolist()

        points = ax.plot(conjunto.cases, conjunto.deaths, 'o', color='b', mec='k', ms=15, mew=1, alpha=.6)

        ax.set_xlabel('Casos de COVID-19')
        ax.set_ylabel('Mortes por COVID-19')
        ax.set_title('Relação entre casos e mortes nos condados americanos por COVID-19', size=20)

        tooltip = plugins.PointHTMLTooltip(points[0], labels, voffset=10, hoffset=10)
        plugins.connect(fig, tooltip)

        # mpld3.display()
        # mpld3.show()
        return mpld3

    def grafico_com_centroiods(self, conjunto: pd.DataFrame, pontos_centroid: list, visualizar_label_centroid=True):
        N = len(conjunto)
        x = conjunto.cases.values
        y = conjunto.deaths.values

        colors = np.random.rand(N)
        plt.scatter(x, y, s=self.area_ponto(N), c=colors, alpha=0.5)

        pontos = np.array(pontos_centroid)
        plt.scatter(pontos[:, 0], pontos[:, 1], color='black', marker="x", alpha=1)

        if visualizar_label_centroid : self.label_do_centroid(zip(pontos[:, 0], pontos[:, 1]))

        plt.xlabel("Cases")
        plt.ylabel("Deaths")
        plt.grid(True)

        plt.show()

    def area_ponto(self, N):
        area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii
        return area

    def label_do_centroid(self, pontos_zip: zip):
        count: int = 0
        for x, y in pontos_zip:
            label: str = f"centroid_{count}: ({x},{y})"
            # label = f"centroid_{count}"
            plt.annotate(label,  # Texto
                         (x, y),  # Coorenadas dos pontos x e y
                         textcoords="offset points",  # Como o texto se posicionara
                         xytext=(0, 10),  # Ditância do texto para o ponto (x,y)
                         ha='center')  # horizontal alinhamento pode ser: left, right or center
            count += 1

    def grafico_com_centroiods_agrupados(self, matriz: pd.DataFrame, pontos_centroid: list, visualizar_legenda=True, visualizar_label_centroid=True):
        """
        Gera os graficaos dos agrupados por centroids e coloca cores para visualização.

        :param matriz:
        :param pontos_centroid:
        :return:
        """

        lista_cores = self.cores
        count: int = 0
        handles = []
        for _grupo in range(0, len(pontos_centroid)):
            # Filtrar pro grupo de centroids
            filtro = f"centroid_id == 'centroid_{count}'"
            sub_conjunto = matriz.query(filtro)
            N = len(sub_conjunto)

            cor = random.sample(lista_cores, 1)
            lista_cores.remove(cor[0])

            if visualizar_legenda: handles.append(mpatches.Patch(color=cor[0], label=f'Centroid {count + 1}'))

            # Pontos Agrupados
            plt.scatter(sub_conjunto.ponto_x, sub_conjunto.ponto_y, color=cor, s=self.area_ponto(N), alpha=0.5)

            # Centroids
            plt.scatter(pontos_centroid[_grupo][0], pontos_centroid[_grupo][1], color=cor, s=50, marker="x", alpha=1)
            count += 1

        if visualizar_label_centroid : self.label_do_centroid(pontos_centroid)
        if visualizar_legenda: plt.legend(handles=handles)
        plt.xlabel("Cases")
        plt.ylabel("Deaths")
        plt.grid(True)
        plt.show()

    def cores_ramdomicas(self):
        """
        Cores randomicas para os gráficos

        :return:
        """
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        return color
