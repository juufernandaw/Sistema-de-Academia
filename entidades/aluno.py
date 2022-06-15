from entidades.usuario import Usuario
from entidades.treino import Treino


class Aluno(Usuario):

    def __init__(self, nome: str, login: str, senha: str, cpf: str, treinos: list):
        super().__init__(nome, login, senha, cpf)
        self.__treinos = treinos

    @property
    def treinos(self):
        return self.__treinos

    def vincular_treino_aluno(self, treino: Treino):
        if (treino is not None) and (isinstance(treino, Treino)):
            if treino not in self.__treinos:
                self.__treinos.append(treino)

    def desvincular_treino_aluno(self, treino: Treino):
        if (treino is not None) and (isinstance(treino, Treino)):
            if treino in self.__treinos:
                self.__treinos.remove(treino)
