
class TelaTreinoDiario():
    def __init__(self):
        pass

    def mostrar_tela_desempenho(self):
        print("Ola Aluno e/ou Professor, você quer consultar o desempenho?")
        print("1 - SIM!")
        print("0 - Voltar")
        escolha = int(input())
        return escolha

    def printar_tela_treino_diario(self):
        print("Ola Professor, você que você deseja?")
        print("1 - consultar o desempenho")
        print("2 - Voltar ao menu inicial")
        print("3 - Colocar os treinos para o aluno vê") # faz sentido ? ou só em treino
        escolha = int(input())
        return escolha

    def montar_treino_diario(self, lista_treinos):
        contador = 0
        for treino in lista_treinos:
            print(contador, " - Nome do treino:", treino.nome)
            contador += 1
        resposta = int(input("Qual treino você fará hoje?"))
        return resposta

    def mensagem(self, msg):
        return msg

    def checkin(self, dias):
        print(f"Você fez {dias} de exercício, parabéns! Continue fime.")
