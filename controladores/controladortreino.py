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
        novo_treino, nome_treino = self.__tela_treino.montar_treino() #pedir o nome do treino e os exercicios
        while (novo_treino==1) and (nome_treino is not None): #pra criar novo treino
            treino = Treino(nome_treino) #instancia o treino
            novo_exercicio, dados_exercicio = self.__tela_treino.montar_exercicio(self.__tipos_exercicio)
            while novo_exercicio==1: #pra criar novo exercicio
                treino.incluir_exercicio(dados_exercicio["nome"], dados_exercicio["serie"], dados_exercicio["repeticao"],\
                dados_exercicio["tempo_descanso"], self.__tipos_exercicio[dados_exercicio["tipo_exercicio"]])
                novo_exercicio, dados_exercicio = self.__tela_treino.montar_exercicio()
            novo_treino, nome_treino = self.__tela_treino.montar_treino()
            self.vincular_treino_aluno(treino)
            self.__treinos.append(treino)

    def excluir_treino(self):
        pass

    def alterar_treino(self):

        nome_treino = self.__tela_treino.seleciona_treino() #implementar
        treino = self.pega_treino_por_nome(nome_treino) #implementar
        if(treino is not None):
            novos_dados_treino = self.__tela_treino.pega_dados_treino() #implementar
            treino.nome = novos_dados_treino["nome"]
#           #!!!!perguntar se aqui eu devo permitir alterar os exercícios que compõem o treino
        else:
            self.__tela_treino.mostra_mensagem("ATENCAO: treino não existente")
        
    def consultar_treino(self):
        nome_treino = self.__tela_treino.seleciona_treino() #implementar
        for treino in self.__treinos:
            if treino.nome == nome_treino:
                treino = {"nome":treino.nome, "exercicios":treino.exercicios}
                self.__tela_treino.mostrar_tela_treino(treino)
            else:    
                self.__tela_treino.mostra_mensagem("ATENCAO: treino não existente")

    def vincular_treino_aluno(self, treino: Treino):
        cpf_aluno = self.__controlador_sistema.controlador_aluno.tela_aluno.seleciona_aluno() #retorna o cpf do aluno q deseja vincular

        #chama o método seleciona_aluno() aí dá um append nos exercicios[] do Aluno
        pass

    def retornar(self):
        pass
