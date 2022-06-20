# from entidades.treino import Treino
# from telas.telatreino import TelaTreino
# from entidades.tipoexercicio import TipoExercicio
from TrabalhoPOO.entidades.treino import Treino
from TrabalhoPOO.telas.telatreino import TelaTreino
from TrabalhoPOO.entidades.tipoexercicio import TipoExercicio


class ControladorTreino:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__treinos = []
        self.__manter_tela = True
        self.__tela_treino = TelaTreino()
        self.__tipos_exercicio = [TipoExercicio("Muscular - Superior", 200), TipoExercicio("Muscular - Inferior", 150),
                                  TipoExercicio("Cardiovascular", 300)]

    @property
    def tipos_exercicio(self):
        return self.__tipos_exercicio

    @property
    def treinos(self):
        return self.__treinos

    def incluir_treino(self):
        novo_treino, nome_treino = self.__tela_treino.montar_treino()  # pedir se quer incluir novo treino e o nome do treino
        while (novo_treino == 1) and (nome_treino is not None):  # pra criar novo treino
            treino = Treino(nome_treino)  # instancia o treino
            self.criar_exercicio(treino)  # chama o método para incluir exercicios no treino
            # !verificar se já existe o treino
            self.__treinos.append(treino)  # adiciona o treino a lista de todos os treinos do sistema
            aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno()  # seleciona o aluno pra vincular #seleciona a instancia do aluno
            aluno.adicionar_treino_aluno(treino)  # chama o método pela instancia do aluno
            novo_treino, nome_treino = self.__tela_treino.montar_treino()  # pedir se quer incluir novo treino e o nome do treino
        if novo_treino == 2:  # se não deseja criar novo treino
            return self.abre_tela_funcoes_treino()

    def criar_exercicio(self, treino: Treino):
        novo_exercicio, dados_exercicio = self.__tela_treino.montar_exercicio(self.__tipos_exercicio)
        while novo_exercicio == 1:  # pra criar novo exercicio ->lembrar de verificar se não estão vazias as infos
            treino.incluir_exercicio(dados_exercicio["nome"], dados_exercicio["serie"], dados_exercicio["repeticao"],
                                     dados_exercicio["tempo_descanso"],
                                     self.__tipos_exercicio[dados_exercicio["tipo_exercicio"]])
            novo_exercicio, dados_exercicio = self.__tela_treino.montar_exercicio(self.__tipos_exercicio)

    def excluir_treino(self):
        treino = self.pegar_treino_por_nome()  # busca infos do treino requisitado
        if treino is not None:
            self.__treinos.remove(treino)  # remove o treino da lista de treinos do sistema
            aluno = self.__controlador_sistema.controlador_aluno.buscar_aluno_por_treino(
                treino)  # verifica se há algum aluno vinculado ao treino
            if aluno is not None:
                aluno.remover_treino_aluno(treino)  # remove o treino da lista de treinos do aluno
            self.__tela_treino.mostrar_msg("Treino excluído com sucesso!")
        else:
            self.__tela_treino.mostrar_msg("ATENCAO: treino não existente")
        return self.abre_tela_funcoes_treino()

    def listar_treinos(self):
        for treino in self.__treinos:
            treino_visualizar = {"nome": treino.nome, "exercicios": treino.exercicios}
            self.__tela_treino.mostrar_tela_treino(treino_visualizar)
        return self.abre_tela_funcoes_treino()

    def pegar_treino_por_nome(self):
        nome_treino = self.__tela_treino.selecionar_treino_por_nome()
        for treino in self.__treinos:
            if treino.nome == nome_treino:
                return treino
        else:
            return None

    def alterar_treino(self):
        treino = self.pegar_treino_por_nome()
        if treino is not None:
            opcao = self.__tela_treino.escolher_alteracao_treino()
            if opcao == 1:
                self.alterar_nome_treino(treino)
            elif opcao == 2:
                treino.excluir_exercicios()  # exclui os exercicios do treino
                self.criar_exercicio(treino)  # inclui os novos exercicios do treino
                return self.abre_tela_funcoes_treino()
        else:
            self.__tela_treino.mostrar_msg("ATENCAO: treino não existente")

    def alterar_nome_treino(self, treino: Treino):
        treino.nome = self.__tela_treino.selecionar_treino_por_nome()
        self.__tela_treino.mostrar_msg("Nome do treino alterado com sucesso!")
        return self.abre_tela_funcoes_treino()

    def consultar_treino(self):
        treino = self.pegar_treino_por_nome()
        if treino is not None:
            treino = {"nome": treino.nome, "exercicios": treino.exercicios}
            self.__tela_treino.mostrar_tela_treino(treino)
        else:
            self.__tela_treino.mostrar_msg("ATENCAO: treino não existente")
        return self.abre_tela_funcoes_treino()

    def abre_tela_funcoes_treino(self):
        try:
            lista_opcoes = {1: self.incluir_treino, 2: self.alterar_treino,
                            3: self.excluir_treino, 4: self.listar_treinos, 5: self.consultar_treino,
                            6: self.__controlador_sistema.controlador_personal_trainer.abre_tela_inicial}
            while True:
                opcao = self.__tela_treino.mexer_treino()
                if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                    raise ValueError
                funcao_escolhida = lista_opcoes[opcao]
                return funcao_escolhida()
        except ValueError:
            print("Escolha um valor entre os mostrados acima.")
            self.abre_tela_funcoes_treino()

    def retornar(self):
        return
