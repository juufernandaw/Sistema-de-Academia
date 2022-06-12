
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
