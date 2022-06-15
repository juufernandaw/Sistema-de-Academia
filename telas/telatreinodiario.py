
class TelaTreinoDiario():
    def __init__(self):
        pass

    def mostrar_tela_desempenho(self):
        print("Ola Aluno, você quer ver seu desempenho da jornada?")
        print("1 - SIM!")
        print("2 - NÃO")
        print("0 - Voltar")
        escolha = int(input())
        return escolha

    def mostrar_desempenho(self):
        print("Aqui está seu desempenho:")
