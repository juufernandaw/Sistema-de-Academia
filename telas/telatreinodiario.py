class TelaTreinoDiario():

    def mostrar_tela_desempenho(self):
        print("----- ABA ALUNO -----")
        print("Olá Aluno, o quê deseja fazer hoje?")
        print("1 - Efetuar Check-in!")
        print("2 - Consultar meu desempenho!")
        print("3 - Sair")
        escolha = int(input())
        return escolha

    def printar_tela_treino_diario(self):#checar se tá sendo usado
        print("Ola Professor, você que você deseja?")
        print("1 - consultar o desempenho")
        print("2 - Voltar ao menu inicial")
        escolha = int(input())
        return escolha

    def montar_treino_diario(self, lista_treinos):
        try:
            contador = 0
            if lista_treinos == []:
                raise Exception
            for treino in lista_treinos:
                print(contador, " - Nome do treino:", treino.nome)
                contador += 1
            resposta = int(input("Qual treino você fará hoje?"))
            return resposta
        except Exception:
            print("Não há treinos cadastrados para você.")
            return None

    def montar_treino_diario_2(self):
        print(f"Você gostaria de fazer outro treino?")
        opcao = int(input("1 - Sim ou 2 - Não"))
        return opcao

    def mostrar_dias_treino(self, dias):
        print(f"Parabéns! Você foi {dias} dia(s) treinar")

    def contar_calorias(self, calorias):
        print(f"Parabéns! Você perdeu {calorias} calorias")

    def mensagem(self, msg):
        print(msg)
