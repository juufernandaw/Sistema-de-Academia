# from telas.telaaluno import TelaAluno
# from entidades.aluno import Aluno
# from controladores.controladorpersonaltrainer import PersonalTrainer
# from controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.telas.telaaluno import TelaAluno
from TrabalhoPOO.entidades.aluno import Aluno


class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__manter_tela = True
        self.__tela_aluno = TelaAluno()

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            for aluno in self.__alunos:
                if (aluno.login == login) and (aluno.senha == senha):
                    return True, aluno  # aluno q achou retornar
            else:
                return False

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["login"], dados_aluno["senha"], dados_aluno["cpf"])
        self.__alunos.append(aluno)
        if aluno is not None:
            self.__tela_aluno.mostrar_msg("Aluno cadastrado com sucesso!")
            return self.abre_tela_funcoes_aluno()

    def selecionar_aluno(self):
        cpf_aluno = self.__tela_aluno.pegar_cpf()
        for aluno in self.__alunos:
            if aluno.cpf == cpf_aluno:
                return aluno
        else:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente")

    def buscar_aluno_por_treino(self, treino):
        for aluno in self.__alunos:
            for treino_individual in aluno.treinos:
                if treino_individual.nome == treino.nome:
                    return aluno
        else:
            return None

    def alterar_aluno(self):
        opcao_alteracao = self.__tela_aluno.opcao_alterar()
        aluno = self.selecionar_aluno()
        lista_opcoes = {1: self.alterar_aluno_nome, 2: self.alterar_aluno_cpf,
                        3: self.alterar_aluno_login, 4: self.alterar_aluno_senha, 5: self.alterar_aluno_treino}
        while True:
            if aluno is not None:
                # retorna a opcao escolhida
                alteracao_aluno = lista_opcoes[opcao_alteracao]  # executa a alteração
                return alteracao_aluno(aluno)

    def alterar_aluno_nome(self, aluno: Aluno):
        aluno.nome = self.__tela_aluno.pegar_nome()
        self.__tela_aluno.mostrar_msg("Aluno alterado com sucesso!")
        return self.abre_tela_funcoes_aluno()

    def alterar_aluno_cpf(self, aluno: Aluno):
        aluno.cpf = self.__tela_aluno.pegar_cpf()
        self.__tela_aluno.mostrar_msg("Aluno alterado com sucesso!")
        return self.abre_tela_funcoes_aluno()

    def alterar_aluno_login(self, aluno: Aluno):
        aluno.login = self.__tela_aluno.pegar_login()
        self.__tela_aluno.mostrar_msg("Aluno alterado com sucesso!")
        return self.abre_tela_funcoes_aluno()

    def alterar_aluno_senha(self, aluno: Aluno):
        aluno.senha = self.__tela_aluno.pegar_senha()
        self.__tela_aluno.mostrar_msg("Aluno alterado com sucesso!")
        return self.abre_tela_funcoes_aluno()

    def alterar_aluno_treino(self, aluno: Aluno):
        opcao = self.__tela_aluno.escolher_opcao_treino() #excluir algum treino ou adicionar um treino ao aluno
        lista_opcoes = {1: self.desvincular_aluno_treino, 2: self.vincular_aluno_treino}
        treino = self.__tela_aluno.mostrar_treino_aluno(aluno.treinos) #retorna o numero do treino
        treino_escolhido = aluno.treinos[treino] #retorna a instancia do treino da lista de treinos
        while True:
            funcao_escolhida = lista_opcoes[opcao]
            return funcao_escolhida()

    def vincular_aluno_treino(self, aluno: Aluno, treino):
        aluno.adicionar_treino_aluno(treino)
        self.__tela_aluno.mostrar_msg("Treino vinculado ao aluno!")
        return self.alterar_aluno()

    def desvincular_aluno_treino(self, aluno: Aluno, treino):
        aluno.remover_treino_aluno(treino)
        self.__tela_aluno.mostrar_msg("Treino desvinculado do aluno!")
        return self.alterar_aluno()

    def excluir_aluno(self):
        aluno = self.selecionar_aluno()
        if aluno is not None:
            self.__alunos.remove(aluno)
            self.__tela_aluno.mostrar_msg("Aluno removido com sucesso!")
        else:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente")
        return self.abre_tela_funcoes_aluno()

    def consultar_aluno(self):
        cpf = self.__tela_aluno.pegar_cpf()
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                self.__tela_aluno.mostrar_aluno(
                    {"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf,
                     "treinos": aluno.treinos})
        return self.abre_tela_funcoes_aluno()
        # ajustar visualização das listas

    def listar_alunos(self):
        print(self.__alunos)
        for aluno in self.__alunos:
            self.__tela_aluno.mostrar_aluno(
                {"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf,
                 "treinos": aluno.treinos})
        # ajustar visualização das listas
        return self.abre_tela_funcoes_aluno()

    def abre_tela_funcoes_aluno(self):
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno,
                        3: self.excluir_aluno, 4: self.listar_alunos, 5: self.consultar_aluno,
                        6: self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario, 
                        7: self.voltar_menu_personal
                        }
        while True:
            opcao = self.__tela_aluno.mexer_aluno()
            funcao_escolhida = lista_opcoes[opcao]
            return funcao_escolhida()

    def retornar(self):
        return self.__controlador_sistema.iniciar_tela_sistema()

    def voltar_menu_personal(self):
        return self.__controlador_sistema.controlador_personal_trainer.abre_tela_inicial()
