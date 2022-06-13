class TelaAluno():

    def mostrar_tela_opcoes(self):
        print("----- INÍCIO -----")
        print("Seja bem-vindo, aluno!")
        print("O que você deseja fazer hoje? Digite o número correspondente:")
        print("1 - Consultar meu treino")
        print("2 - Efetuar check-in")
        print("3 - Consultar meu desempenho")
        print("4 - Sair")

        opcao = int(input())
        return opcao

    def mostrar_msg(self, msg):
        print(msg)

    def mostrar_aluno(self, dados_aluno):
        print("Nome:",dados_aluno["nome"])
        print("Login:",dados_aluno["login"])
        print("Senha:",dados_aluno["senha"])
        print("CPF:",dados_aluno["cpf"])

    def seleciona_aluno(self):
        cpf = input("Digite o cpf do aluno:")
        return cpf

    def pega_dados_aluno(self):
        nome = input("Digite o nome do aluno:")
        login = input("Digite o login do aluno:")
        senha = input("Digite a senha do aluno:")
        cpf = input("Digite o cpf do aluno:")
        return {"nome":nome, "login":login, "senha":senha, "cpf":cpf}
