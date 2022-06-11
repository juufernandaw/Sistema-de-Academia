from treino import Treino
from aluno import Aluno
from datetime import date


class TreinoDiario():
    def __init__(self, aluno: Aluno, data: date, treinos: Treino):
        self.__aluno = aluno
        self.__data = data
        self.__treinos = []

    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.__aluno = aluno

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    def treinos(self, treinos: Treino):
        if isinstance(treinos, Treino):
            pass

