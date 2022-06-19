
class TelaPersonalTrainer():
    def __init__(self):
        pass

    def tela_alterar_dados(self):  # Esse seria o mexer personal?
        print("Olá, Renove seus Dados:")
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
            print("3 - Modificar treinos")
            print("0 - Sair")
            opcao = int(input())
            if opcao == 1:
                return 1
            elif opcao == 2:
                return 2
            elif opcao == 0:
                return 0
            else:
                print("Tratar para acertar o valor certo: 1, 2 ou 0")
                self.mexer_personal()

    def mostrar_msg(self, msg):
        print(msg)
