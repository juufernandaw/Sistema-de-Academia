from TrabalhoPOO.entidades.treino import Treino
from TrabalhoPOO.telas.telatreino import TelaTreino


class ControladorTreino():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__treinos = []
        self.__manter_tela = True
        self.__tela_treino = TelaTreino()

    def incluir_treino(self):
        pass

    def excluir_treino(self):
        pass

    def alterar_treino(self):
        pass

    def consultar_treino(self):
        pass

    def vincular_treino_aluno(self):
        pass

    def retornar(self):
        pass
