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

    def grafico_com_centroiods(self, conjunto: pd.DataFrame, pontos_centroid: list):
        N = len(conjunto)
        x = conjunto.cases.values
        y = conjunto.deaths.values

        colors = np.random.rand(N)

        area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)

        pontos = np.array(pontos_centroid)

        plt.scatter(pontos[:, 0], pontos[:, 1], color='red', marker="x", alpha=1)
        plt.show()
