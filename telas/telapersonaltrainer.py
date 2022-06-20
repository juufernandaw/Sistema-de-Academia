
class TelaPersonalTrainer():
    def __init__(self):
        pass

    def mostrar_personal_trainer(self, dados_personal):  # mostra os dados do personal
        print("Nome:", dados_personal["nome"])
        print("Login:", dados_personal["login"])
        print("Senha:", dados_personal["senha"])
        print("CPF:", dados_personal["cpf"])
        print("habilitacao:", dados_personal["habilitacao"])

    def tela_aba_personal(self):
        print("----- ABA PERSONAL -----")
        print("O que você deseja fazer hoje ?")
        print("1 - Consultar seus dados")
        print("2 - Alterar seus dados")
        print("0 - Voltar")
        opcao = int(input())
        return opcao

    def tela_alterar_dados(self):  # alterando personal
        print("Olá, Renove seus Dados:")
        nome = input("Digite o nome:")
        cpf = input("Digite o cpf:")
        login = input("Digite o login:")
        senha = input("Digite a senha:")
        habilitacao = input("Digite a habilitação:")
        return {"cpf": cpf, "nome": nome, "login": login, "senha": senha, "habilitacao": habilitacao}

    def mexer_personal(self):
        while True:
            print("----- INÍCIO -----")
            print("Seja bem-vindo, personal!")
            print("O que você deseja fazer hoje? Digite o número correspondente:")
            print("1 - ABA Personal")  # modificar personal
            print("2 - ABA Alunos")   # modificar alunos
            print("3 - ABA Treinos")  # modificar treino
            print("0 - Sair")

            opcao = int(input())
            return opcao

    def mostrar_msg(self, msg):
        print(msg)
