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

    def readDataset(self):
        """
        Lê o Dataset e retorna um Dataframe

        :param path_conjunto:
        :return: pd.DataFrame
        """
        self.conjunto = pd.read_csv(self.path_conjunto);

        return self.conjunto

    def removeColunas(self, colunas: list):
        """
        Remove as colunas passadas como lista e retorna o próprio conjunto.

        Retorna o dataset sem as colunas

        :param colunas:

        :return:
        """
        self.conjunto.drop(columns=colunas, inplace=True)

        return self.conjunto

    def salvarDataset(self, nome_dataset: str):
        """
        Salva o Dataset já processado com o nome_dataset
        :param nome_dataset:

        :return:
        """
        self.conjunto.to_csv(self.PATH_DATASET + nome_dataset)
