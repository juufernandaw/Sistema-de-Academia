from entidades.treino import Treino
from excecoes.listavaziaexception import ListaVaziaException
from telas.telatreino import TelaTreino
from entidades.tipoexercicio import TipoExercicio


class ControladorTreino:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__treinos = []
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
            nome_treino = self.__tela_treino.montar_treino()  # pedir se quer incluir novo treino e o nome do treino
            if nome_treino is not None:  # pra criar novo treino
                for treino in self.__treinos:
                    print("treino nome", treino["nome"])
                    if treino["nome"] == nome_treino:
                        self.__tela_treino.mostrar_msg("ATENÇÃO: Treino já existe no sistema. Favor cadastrar outro.")
                        return self.incluir_treino()
                else:
                    treino = Treino(nome_treino)  # instancia o treino
                    self.criar_exercicio(treino)  # chama o método para incluir exercicios no treino
                    print("Oi")
                    self.__treinos.append({"nome": treino.nome, "exercicios": treino.exercicios})
                    self.__tela_treino.mostrar_msg("Treino cadastrado com sucesso!")
                    aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno()  # seleciona o aluno pra vincular #seleciona a instancia do aluno
                    while (aluno is None):
                        self.__tela_treino.mostrar_msg("ATENÇÃO: Aluno inexistente! Favor digite um aluno válido")
                        aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno()
                    aluno.adicionar_treino_aluno({"nome": treino.nome, "exercicios": treino.exercicios})  # chama o método pela instancia do aluno
                    self.__tela_treino.mostrar_msg("Treino vinculado ao aluno!")
                    return self.abre_tela_funcoes_treino()
            else:
                self.__tela_treino.mostrar_msg("ATENÇÃO: Treino inválido. Digite um treino válido.")
                return self.incluir_treino()

    def criar_exercicio(self, treino: Treino):
        dados_exercicio = self.__tela_treino.montar_exercicio(self.__tipos_exercicio)
        treino.incluir_exercicio(dados_exercicio["nome"], dados_exercicio["serie"], dados_exercicio["repeticao"],
                                dados_exercicio["tempo_descanso"],
                                self.__tipos_exercicio[dados_exercicio["tipo_exercicio"]])
        self.__tela_treino.mostrar_msg("Exercicio cadastrado com sucesso!")
        novo_exercicio = self.__tela_treino.exercicio_novamente() #opcao = 1 novo exercicio
        print("novo_exercicio", novo_exercicio)
        if novo_exercicio == 2:
            print("Treino", treino)
            self.criar_exercicio(treino)

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
            self.__tela_treino.mostrar_msg("ATENÇÃO: Treino não existente. Digite um treino válido.")
        return self.abre_tela_funcoes_treino()

    def listar_treinos(self):
        self.__tela_treino.mostrar_tela_treino(self.__treinos)
        return self.abre_tela_funcoes_treino()

    def pegar_treino_por_nome(self):
        nome_treino = self.__tela_treino.selecionar_treino_por_nome()
        for treino in self.__treinos:
            if treino["nome"] == nome_treino:
                print("Treino", treino)
                return treino

        else:
            return None

    def alterar_treino(self):
        try:
            treino = self.pegar_treino_por_nome()
            if treino is None:
                raise ListaVaziaException
            if treino is not None:
                opcao = self.__tela_treino.escolher_alteracao_treino()
                if opcao != 1 and opcao != 2:
                    raise ValueError
                if opcao == 1:
                    self.alterar_nome_treino(treino)
                elif opcao == 2:
                    treino.excluir_exercicios()  # exclui os exercicios do treino
                    self.criar_exercicio(treino)  # inclui os novos exercicios do treino
                    return self.abre_tela_funcoes_treino()
        except ValueError:
            self.__tela_treino.mostrar_msg("ATENÇÃO: Valor inválido. Selecione um dos valores que estão na tela.")
            return self.alterar_treino()
        except ListaVaziaException:
            self.__tela_treino.mostrar_msg("ATENÇÃO: Treino não existente. Informe um treino válido.")
            return self.alterar_treino()

    def alterar_nome_treino(self, treino: Treino):
        treino.nome = self.__tela_treino.selecionar_treino_por_nome()
        self.__tela_treino.mostrar_msg("Nome do treino alterado com sucesso!")
        return self.abre_tela_funcoes_treino()

    def consultar_treino(self):
        treino = self.pegar_treino_por_nome()
        print("Treino", treino)
        print("oiie",)
        if treino is not None:
            self.__tela_treino.mostrar_tela_treino([treino])
            return self.abre_tela_funcoes_treino()
        else:
            self.__tela_treino.mostrar_msg("ATENÇÃO: Treino não existente. Favor digitar um treino válido")
            return self.consultar_treino()

    def abre_tela_funcoes_treino(self):
        lista_opcoes = {1: self.incluir_treino, 2: self.alterar_treino,
                        3: self.excluir_treino, 4: self.listar_treinos, 5: self.consultar_treino,
                        0: self.__controlador_sistema.controlador_personal_trainer.abre_tela_inicial}
        while True:
            opcao = self.__tela_treino.mexer_treino()
            funcao_escolhida = lista_opcoes[opcao]
            return funcao_escolhida()
