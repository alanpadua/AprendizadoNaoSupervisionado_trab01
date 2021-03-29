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

    def calculo_hipotenusa(self):
        print("Calculo Hipotenusa")
        hipotenusa = self.formulas.calcula_hipotenusa(1.2, 4.5)

    def fit_k_means(self):
        print("Teste Kmeans")
        conjunto = self.get_dataset_filtrado()
        kmeansCalculo = KmeansCalculo(conjunto)

        x, y, N, matriz = kmeansCalculo.fit_k_means(qt_centroids=5, parada=20, max_iter=20)
        # x, y, N, matriz = kmeansCalculo.fit_k_means(qt_centroids=5, parada=20, max_iter=20)
        kmeansCalculo.distribuir_pontos_centroids(matriz)
        self.graficos.grafico_com_centroiods(kmeansCalculo.conjunto, kmeansCalculo.gerar_pontos_centroids(3))

    def get_dataset_processado(self):
        processamento = Processamento('dataset_processado.csv')
        conjunto = processamento.readDataset()

        return conjunto

    def get_dataset_filtrado(self):
        processamento = Processamento('dataset_processado.csv')
        conjunto = processamento.read_dataset()

        filtro = "cases > 1 and deaths > 1"
        conjunto = processamento.filtrar_conjunto(max_item_conjunto=500, filtro=filtro)

        return conjunto


main = Main()
main.processar_dataset()
# main.imprimir_graficos()
main.calculo_hipotenusa()
main.fit_k_means()
