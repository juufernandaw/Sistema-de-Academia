
class TelaSistema:
    def mostrarMenu_inicial(self):
        global opcao
        try:
            print("Olá, bem vindo! Aqui começa sua jornada"
                  " para superar seus limites!")
            print("Faça seu login")
            print("1 - Professor")
            print("2 - Aluno")
            print("0 - Sair")
            opcao = input()
        except Exception:
            if opcao != 1 and opcao != 2:
                print("Você só pode apertar 1 ou 2, caro padawan")
        return opcao

    def mostrar_tela_aluno(self): #método tela inicial aluno
        print("----- INÍCIO -----")
        print("Seja bem-vindo, aluno!")
        print("O que você deseja fazer hoje? Digite o número correspondente:")
        print("1 - Consultar meu treino")
        print("2 - Efetuar check-in")
        print("3 - Consultar meu desempenho")
        print("4 - Sair")

        opcao = int(input())
        return opcao

    def mostrar_tela_personal(self): #método tela inicial personal
        print("----- INÍCIO -----")
        print("Seja bem-vindo, personal!")
        print("O que você deseja fazer hoje? Digite o número correspondente:")
        print("1 - Aba aluno")
        print("2 - Aba personal")
        print("3 - Aba treino")
        print("4 - Aba treino diário")
        print("5 - Sair")

        opcao = int(input())
        return opcao

