
class TelaSistema:
    def mostrarMenu_inicial(self):
        global opcao
        try:
            print("Olá, bem vindo! Aqui começa sua jornada"
                  " para superar seus limites!")
            print("Escolha sua opcao")
            print("1 - Login")
            print("0 - Sair da jornada")
            opcao = input()
        except Exception:
            if opcao != 1 and opcao != 0:
                print("Você só pode apertar 1 ou 0, caro padawan")
        return opcao
