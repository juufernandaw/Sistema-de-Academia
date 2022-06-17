
class TelaTreinoDiario():
    def __init__(self):
        pass

    def mostrar_tela_desempenho(self):
        print("Ola Aluno e/ou Professor, você quer consultar o desempenho?")
        print("1 - SIM!")
        print("2 - NÃO")
        print("0 - Voltar")
        escolha = int(input())
        return escolha

    def registrar_treino(self):
        print("Registre seu treino")
        print("1- sim")
        print("2- não")
        registro_treino = int(input())
        return registro_treino

    def mostrar_desempenho(self):
        print("Quer vê seu desempenho ?")
        print("1- sim")
        print("2- não")
        mostrar_desempenho = int(input())
        return mostrar_desempenho

    def checkin(self):
        print(" Você frequentou em dias: ")
