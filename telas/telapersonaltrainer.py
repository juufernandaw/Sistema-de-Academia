
class TelaPersonalTrainer():
    def __init__(self):
        pass

    def tela_alterar_dados(self):  # Esse seria o mexer personal?
        print("Olá, você pode alterar todos os seus dados: Qual você deseja?")
        nome = input("Digite o nome:")
        cpf = input("Digite o cpf:")
        login = input("Digite o login:")
        senha = input("Digite a senha:")
        habilitacao = input("Digite o cpf:")
        return {"cpf": cpf, "nome": nome, "login": login, "senha": senha, "habilitacao": habilitacao}

    def mexer_personal(self):
        while True:
            print("----- INÍCIO -----")
            print("Seja bem-vindo, personal!")
            print("O que você deseja fazer hoje? Digite o número correspondente:")
            print("1 - Modificar minhas informações")
            print("2 - Modificar alunos")
            print("0 - Sair")
            opcao = int(input())
            if opcao == 1:
                self.tela_alterar_dados()
            elif opcao == 2:
                return 2
            elif opcao == 0:
                return 0
            else:
                print("Tratar para acertar o valor certo: 1, 2 ou 0")
                self.mexer_personal()

    def mostrar_msg(self, msg):
        print(msg)

    # Não precisa porque o personal é somente 1, ou seja, já ta instaciado.
    # def seleciona_personal(self):  # seleciona personal por cpf
    #     habilitacao = input("Digite seu cpf, personal:")
    #     return habilitacao
