from telas.telaaluno import TelaAluno
from entidades.aluno import Aluno


class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__tela_aluno = TelaAluno()

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            try:
                for aluno in self.__alunos:
                    if (aluno.login == login) and (aluno.senha == senha):
                        return True, aluno  # aluno q achou retornar
                    if not aluno.login and not aluno.senha:
                        raise TypeError
            except TypeError:
                self.__tela_aluno.mostrar_msg("Login e senha inválidos")
            else:
                return False

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        for aluno in self.__alunos:
            if dados_aluno["login"] == aluno.login:
                self.__tela_aluno.mostrar_msg("Este login já consta no sistema!")
                return self.incluir_aluno()
            elif dados_aluno["cpf"] == aluno.cpf:
                self.__tela_aluno.mostrar_msg("Este cpf já consta no sistema!")
                return self.incluir_aluno()
        else:
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
            return None

    def buscar_aluno_por_treino(self, treino):
        for aluno in self.__alunos:
            for treino_individual in aluno.treinos:
                if treino_individual.nome == treino.nome:
                    return aluno
        else:
            return None

    def alterar_aluno(self):
        opcao_alteracao = self.__tela_aluno.opcao_alterar()
        lista_opcoes = {1: self.alterar_aluno_nome, 2: self.alterar_aluno_cpf,
                        3: self.alterar_aluno_login, 4: self.alterar_aluno_senha,
                        5: self.alterar_aluno_treino, 0: self.retornar}
        if opcao_alteracao != 0:
            aluno = self.selecionar_aluno()
            try:
                while True:
                    if aluno is not None:
                        # retorna a opcao escolhida
                        alteracao_aluno = lista_opcoes[opcao_alteracao]  # executa a alteração
                        return alteracao_aluno(aluno)
                    else:
                        raise Exception
            except Exception:
                self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente. Favor escolher um aluno existente.")
                return self.alterar_aluno()
        else:
            alteracao_aluno = lista_opcoes[opcao_alteracao]  # executa a alteração
            return alteracao_aluno()

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
        try:
            opcao = self.__tela_aluno.escolher_opcao_treino()  # excluir algum treino ou adicionar um treino ao aluno
            if opcao != 1 and opcao != 2:
                raise ValueError
            lista_opcoes = {1: self.desvincular_aluno_treino, 2: self.vincular_aluno_treino}
            treino = self.__tela_aluno.mostrar_treino_aluno(aluno.treinos)  # retorna o numero do treino
            treino_escolhido = aluno.treinos[treino]  # retorna a instancia do treino da lista de treinos
            while True:
                funcao_escolhida = lista_opcoes[opcao]
                return funcao_escolhida(aluno, treino_escolhido)
        except ValueError:
            self.__tela_aluno.mostrar_msg("Digite os valores dados na tela, por favor.")
            self.alterar_aluno_treino(aluno)

    def vincular_aluno_treino(self, aluno: Aluno, treino):
        aluno.adicionar_treino_aluno(treino)
        self.__tela_aluno.mostrar_msg("Treino vinculado ao aluno!")
        return self.alterar_aluno()

    def desvincular_aluno_treino(self, aluno: Aluno, treino):
        aluno.remover_treino_aluno(treino)
        self.__tela_aluno.mostrar_msg("Treino desvinculado do aluno!")
        return self.alterar_aluno()

    def excluir_aluno(self):
        try:
            aluno = self.selecionar_aluno()
            if aluno is not None:
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostrar_msg("Aluno removido com sucesso!")
                return self.abre_tela_funcoes_aluno()
            else:
                raise Exception
        except Exception:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente. Favor escolher um aluno existente.")
            return self.excluir_aluno()

    def consultar_aluno(self):
        try:
            cpf = self.__tela_aluno.pegar_cpf()
            for aluno in self.__alunos:
                if aluno.cpf == cpf:
                    self.__tela_aluno.mostrar_aluno(
                        {"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf,
                         "treinos": aluno.treinos})
                    return self.abre_tela_funcoes_aluno()
            else:
                raise Exception
        except Exception:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente. Favor escolher um aluno existente.")
            return self.consultar_aluno()
        # ajustar visualização das listas

    def listar_alunos(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostrar_aluno(
                {"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf,
                 "treinos": aluno.treinos})
        if self.__alunos == []:
            self.__tela_aluno.mostrar_msg("Não há nenhum aluno cadastrado")
        return self.abre_tela_funcoes_aluno()

    def abre_tela_funcoes_aluno(self):
        try:
            lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno,
                            3: self.excluir_aluno, 4: self.listar_alunos, 5: self.consultar_aluno,
                            6: self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario_personal,
                            0: self.retornar
                            }
            while True:
                opcao = self.__tela_aluno.mexer_aluno()
                if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6 and opcao != 0:
                    raise ValueError
                funcao_escolhida = lista_opcoes[opcao]
                return funcao_escolhida()
        except ValueError:
            self.__tela_aluno.mostrar_msg("Digite uma das opções sugeridas, por favor")
            self.abre_tela_funcoes_aluno()

    def retornar(self):
        return self.__controlador_sistema.controlador_personal_trainer.abre_tela_inicial()

    def abre_tela_inicial(self):  # abre a tela aluno pós login da tela
        try:
            usuario = self.__controlador_sistema.usuario_logado
            mexer_aluno_opcoes = {1: self.consultar_treino_aluno,
                                  2: self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario,
                                  3: self.__controlador_sistema.controlador_treino_diario.desempenho_aluno,
                                  0: self.retornar
                                  }
            while True:
                opcao_escolhida = self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 0:
                    raise ValueError
                if opcao_escolhida == 1:
                    return self.consultar_treino_aluno(usuario.treinos)
                else:
                    funcao_escolhida = mexer_aluno_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueError:
            self.__tela_aluno.mostrar_msg("Digite uma das opções sugeridas, por favor")
            self.abre_tela_inicial()

    def consultar_treino_aluno(self, treinos):
        for treino in treinos:
            treino = {"nome": treino.nome, "exercicios": treino.exercicios}
            self.__controlador_sistema.controlador_treino.tela_treino.mostrar_tela_treino(treino)
        return self.abre_tela_inicial()
