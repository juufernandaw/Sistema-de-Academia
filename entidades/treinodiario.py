from entidades.aluno import Aluno
from datetime import date


class TreinoDiario:
    def __init__(self, aluno: Aluno, data: date, treinos: []):
        self.__aluno = aluno
        self.__data = data
        self.__treinos = treinos

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

    @property
    def treinos(self):
        return self.__treinos

    @treinos.setter
    def treinos(self, lista_treinos):
        if isinstance(lista_treinos, list):
            self.__treinos = lista_treinos

    def chave(self):  # ve se funciona se nao converter em str antes :isso é pra usar ac chave na persistencia
        chave = self.__aluno.nome + str(self.__data.strftime("%m%d%Y, %H:%M:%S"))  # date_str = dia_atual.strftime(
        # "%m%d%Y, %H:%M:%S")
        return chave
