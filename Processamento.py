import pandas as pd


class Processamento:

    def __init__(self, path_conjunto: str):
        """
        Inicialização do Processamento deve ser passado o dataset para que possa ser alterado posteriormente.
        :param path_conjunto:
        """
        self.conjunto: pd.DataFrame = None
        self.PATH_DATASET: str = 'Dataset/'
        self.path_conjunto: str = self.PATH_DATASET + path_conjunto

    def read_dataset(self):
        """
        Lê o Dataset e retorna um Dataframe

        :param path_conjunto:
        :return: pd.DataFrame
        """
        self.conjunto = pd.read_csv(self.path_conjunto);

        return self.conjunto

    def remove_colunas(self, colunas: list):
        """
        Remove as colunas passadas como lista e retorna o próprio conjunto.

        Retorna o dataset sem as colunas

        :param colunas:

        :return:
        """
        self.conjunto.drop(columns=colunas, inplace=True)

        return self.conjunto

    def salvar_dataset(self, nome_dataset: str):
        """
        Salva o Dataset já processado com o nome_dataset
        :param nome_dataset:

        :return:
        """
        self.conjunto.to_csv(self.PATH_DATASET + nome_dataset)

    def filtrar_conjunto(self, max_item_conjunto: int = None, filtro: str = None):

        if filtro != None:
            self.conjunto = self.conjunto.query(filtro).reset_index()
            # self.conjunto = self.conjunto(filtro)
            # self.conjunto = self.conjunto(filtro).reset_index()

        if max_item_conjunto != None:
            self.conjunto = self.conjunto[0: max_item_conjunto]

        return self.conjunto
