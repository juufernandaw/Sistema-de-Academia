from entidades.treino import Treino
from telas.telatreino import TelaTreino
from entidades.tipoexercicio import TipoExercicio


class ControladorTreino():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__treinos = []
        self.__manter_tela = True
        self.__tela_treino = TelaTreino()
        self.__tipos_exercicio = [TipoExercicio("Muscular - Superior",200), TipoExercicio("Muscular - Inferior",150), \
        TipoExercicio("Cardiovascular",300)]

    @property
    def tipos_exercicio(self):
        return self.__tipos_exercicio

    def incluir_treino(self):
        #pedir o nome do treino e os exercicios
        novo_treino = self.__tela_treino.montar_treino()
        novo_exercicio = self.__tela_treino.montar_exercicio()
        while novo_treino==1: #pra criar novo treino
            novo_exercicio = self.__tela_treino.montar_exercicio()
            treino = Treino(nome) #instancia o treino
            while novo_exercicio==1: #pra criar novo exercicio
                treino.incluir_exercicio(dados_treino["nome"], dados_treino["serie"], dados_treino["repeticao"], dados_treino["tempo_descanso"], self.__tipos_exercicio[dados_treino["tipo_exercicio"]])
        #chamar método vincular_treino_aluno

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
