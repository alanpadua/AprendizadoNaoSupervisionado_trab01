from Formulas import Formulas
from Graficos import Graficos
from Processamento import Processamento
from KmeansCalculo import KmeansCalculo


class Main:

    def __init__(self):
        print("Main")
        self.formulas = Formulas()
        self.graficos = Graficos()
        self.labels: list = ['date', 'county', 'state', 'fips', 'cases', 'deaths']

    def processarDataset(self):
        print("Processar Dataset")
        processamento = Processamento('us-counties-covid-19-dataset.csv')
        conjunto = processamento.readDataset()
        conjunto = processamento.removeColunas(['date', 'state', 'fips'])

        processamento.salvarDataset('dataset_processado.csv')
        # print(conjunto.head(10))

        return conjunto

    def imprimirGraficos(self):
        print("Imprimir Graficos")
        conjunto = self.getDatasetProcessado()

        # self.graficos.plot_seaborn(conjunto)
        self.graficos.plot_scatter(conjunto)
        # self.graficos.mpld3(conjunto)

    def calculoHipotenusa(self):
        print("Calculo Hipotenusa")
        hipotenusa = self.formulas.calcula_hipotenusa(1.2, 4.5)
        # print(hipotenusa)

    def fit_k_means(self):
        print("Teste Kmeans")
        conjunto = self.getDatasetProcessado()
        kmeansCalculo = KmeansCalculo(conjunto)
        filtro = "cases > 1 and deaths > 1"
        x, y, N, matriz = kmeansCalculo.fit_k_means(qt_centroids=5, parada=20, max_iter=20, max_item_conjunto=500, filtro=filtro)
        # x, y, N, matriz = kmeansCalculo.fit_k_means(qt_centroids=5, parada=20, max_iter=20)
        kmeansCalculo.distribuir_pontos_centroids(matriz)
        self.graficos.grafico_com_centroiods(kmeansCalculo.conjunto, kmeansCalculo.gerar_pontos_centroids(3))

    def getDatasetProcessado(self):
        processamento = Processamento('dataset_processado.csv')
        conjunto = processamento.readDataset()
        return conjunto


main = Main()
main.processarDataset()
# main.imprimirGraficos()
# main.calculoHipotenusa()
main.fit_k_means()
