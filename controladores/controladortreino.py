from entidades.treino import Treino
from telas.telatreino import TelaTreino
from entidades.tipoexercicio import TipoExercicio
from entidades.exercicio import Exercicio


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
        dados_treino = self.__tela_treino.montar_treino() #checar tipo_Exercicio
        exercicio = Exercicio(dados_treino["nome"], dados_treino["serie"], dados_treino["repeticao"], dados_treino["tempo_descanso"], tipo_exercicio)

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
