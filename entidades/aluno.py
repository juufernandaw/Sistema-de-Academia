from entidades.usuario import Usuario
from entidades.treino import Treino


class Aluno(Usuario):

    def __init__(self, nome: str, login: str, senha: str, cpf: str):
        super().__init__(nome, login, senha, cpf)
        self.__treinos = []

    @property
    def treinos(self):
        return self.__treinos

    @treinos.setter
    def treinos(self, treinos: list):
        self.__treinos = treinos

    def adicionar_treino_aluno(self, treino: {}):
        if (treino is not None) and (isinstance(treino, dict)):
            if treino not in self.__treinos:
                self.__treinos.append(treino)

    def remover_treino_aluno(self, treino: {}):
        if (treino is not None) and (isinstance(treino, dict)):
            if treino in self.__treinos:
                self.__treinos.remove(treino)
