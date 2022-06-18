
class TelaTreinoDiario():
    def __init__(self):
        pass

    def mostrar_tela_desempenho(self):
        print("Ola Aluno e/ou Professor, você quer consultar o desempenho?")
        print("1 - SIM!")
        print("0 - Voltar")
        escolha = int(input())
        return escolha

    def mensagem(self, msg):
        return msg

    def checkin(self, dias):
        print(f"Você fez {dias} de exercício, parabéns! Continue fime.")
