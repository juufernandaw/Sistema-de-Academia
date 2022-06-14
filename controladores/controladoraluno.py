from telas.telaaluno import TelaAluno
from entidades.aluno import Aluno
from controladores.controladorpersonaltrainer import PersonalTrainer

class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__manter_tela = True
        self.__tela_aluno = TelaAluno()

#implementar essa verificacao
    # def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
    #     if isinstance(login, str) and isinstance(senha, str):
    #         if self.__alunos == login and self.__personal.senha == senha: #Set Para Mudar
    #             return True

    #adicionar o treino ao aluno
    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno() 
        aluno = Aluno(dados_aluno["nome"], dados_aluno["login"], dados_aluno["senha"], dados_aluno["cpf"])
        self.__alunos.append(aluno)

    def alterar_aluno(self):
        cpf = self.__tela_aluno.seleciona_aluno() 
        aluno = self.consultar_aluno(cpf) 
        if (aluno is not None):
            novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados_aluno["nome"]
            aluno.login = novos_dados_aluno["login"]
            aluno.senha = novos_dados_aluno["senha"]
            aluno.cpf = novos_dados_aluno["cpf"]
        else:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente")

    def excluir_aluno(self):
        cpf_aluno = self.__tela_aluno.seleciona_aluno() 
        aluno = self.consultar_aluno(cpf_aluno) 
        if (aluno is not None):
            self.__alunos.remove(aluno)
        else:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente")

    def consultar_aluno(self, cpf: str):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                return aluno
        return None

    def listar_alunos(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostrar_aluno({"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf})

    def abre_tela_funcoes_aluno(self):
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.excluir_aluno, 4: self.listar_alunos, 5: self.consultar_aluno, 6: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_aluno.mexer_aluno()]

    def retornar(self):
        pass
