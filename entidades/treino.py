class Treino():

    def __init__(self, nome: str):
        self.__nome = nome
        self.__exercicios = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def exercicios(self):
        return self.__exercicios