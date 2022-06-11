from entidades.treino import Treino
from telas.telatreino import TelaTreino

class ControladorTreino():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__treinos = []
        self.__manter_tela = True
        self.__tela_treino = TelaTreino()

