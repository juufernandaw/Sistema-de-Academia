#from TrabalhoPOO.entidades.exercicio import Exercicio
from entidades.exercicio import Exercicio


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

    def incluir_exercicio(self, nome, serie, repeticao, tempo_descanso, tipo_exercicio):
        exercicio = Exercicio(nome, serie, repeticao, tempo_descanso, tipo_exercicio)
        self.__exercicios.append(exercicio)

    def excluir_exercicios(self):
        self.__exercicios = []