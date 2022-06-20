
class TelaTreinoDiario():
    def __init__(self):
        pass

    def mostrar_tela_desempenho(self):
        print("----- ABA ALUNO -----")
        print("----- ABA DESEMPENHO -----")
        print("Ola Aluno, você quer consultar o desempenho?")
        print("1 - Confirmar Check-in!")
        print("2 - Consultar seu desempenho!")
        print("3 - voltar")
        escolha = int(input())
        return escolha

    def printar_tela_treino_diario(self):
        print("Ola Professor, você que você deseja?")
        print("1 - consultar o desempenho")
        print("2 - Voltar ao menu inicial")
        escolha = int(input())
        return escolha

    def montar_treino_diario(self, lista_treinos):
        contador = 0
        for treino in lista_treinos:
            print(contador, " - Nome do treino:", treino.nome)
            contador += 1
        resposta = int(input("Qual treino você fará hoje?"))
        return resposta

    def montar_treino_diario_2(self):
        print(f"Você gostaria de fazer outro treino ?")
        opcao = input("1 - Sim ou 2 - Não")
        return opcao

    def mostrar_dias_treino(self, dias):
        print(f"Parabéns você foi {dias} treinar")

    def contar_calorias(self, calorias):
        print(f"Parabéns você perdeu {calorias} calorias")

    def mensagem(self, msg):
            return msg
