from telas.telaaluno import TelaAluno
from entidades.aluno import Aluno


class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__manter_tela = True
        self.__tela_aluno = TelaAluno()

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno() #implementar método pega_dados_aluno(): usuário digita tds as infos 
        aluno = Aluno(dados_aluno["nome"], dados_aluno["login"], dados_aluno["senha"], dados_aluno["cpf"])
        self.__alunos.append(aluno)

    def alterar_aluno(self):
        cpf = self.__tela_aluno.seleciona_aluno() #implementar seleciona_aluno()
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
        cpf_aluno = self.__tela_aluno.seleciona_aluno() #implementar seleciona_aluno()
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

    def abre_tela_inicial(self):
        pass

    def retornar(self):
        pass
