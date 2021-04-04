from Formulas import Formulas
from Graficos import Graficos
from Processamento import Processamento
from KmeansCalculo import KmeansCalculo


class Main:

    def __init__(self):
        print("Main")
        self.K = 5
        self.formulas = Formulas()
        self.graficos = Graficos()
        self.labels: list = ['date', 'county', 'state', 'fips', 'cases', 'deaths']

    def processar_dataset(self):
        print("Processar Dataset")
        processamento = Processamento('us-counties-covid-19-dataset.csv')
        conjunto = processamento.read_dataset()
        conjunto = processamento.remove_colunas(['date', 'state', 'fips'])

        processamento.salvar_dataset('dataset_processado.csv')
        # print(conjunto.head(10))

        return conjunto

    def imprimir_graficos(self):
        print("Imprimir Graficos")
        conjunto = self.get_dataset_filtrado()

        self.graficos.plot_seaborn(conjunto)
        self.graficos.plot_scatter(conjunto)
        self.graficos.mpld3(conjunto)

    def get_dataset_processado(self):
        processamento = Processamento('dataset_processado.csv')
        conjunto = processamento.read_dataset()

        return conjunto

    def get_dataset_filtrado(self):
        processamento = Processamento('dataset_processado.csv')
        conjunto = processamento.read_dataset()

        filtro = "cases > 2 and deaths > 2"
        conjunto = processamento.filtrar_conjunto(max_item_conjunto=500, filtro=filtro)

        return conjunto

    def fit_k_means(self):
        print("Teste Kmeans")
        conjunto = self.get_dataset_filtrado()
        # conjunto = self.get_dataset_processado()
        kmeansCalculo = KmeansCalculo(conjunto, parada=20, max_iter=20)

        X, y, N, centroids, matriz = kmeansCalculo.fit_k_means(qt_centroids=self.K)
        # X, y, N, centroids, matriz = kmeansCalculo.fit_k_means(qt_centroids=5, parada=20, max_iter=20)

        self.graficos.grafico_com_centroiods(kmeansCalculo.conjunto, centroids, visualizar_label_centroid=False)
        self.graficos.grafico_com_centroiods_agrupados(matriz, centroids, visualizar_legenda=True, visualizar_label_centroid=False)

        # kmeansCalculo.lista_centroids_mais_proximos(matriz)


main = Main()
main.processar_dataset()
# main.imprimir_graficos()
main.fit_k_means()
