class TelaTreino():

    def mostrar_tela_treino():
        pass

    def montar_treino():
        resposta = input("Deseja cadastrar um novo exercício? 1- Sim 2-Não")
        while resposta==1:
            nome = input("Nome:")
            serie = input("Série:")
            repeticao = input("Repetição:")
            tempo_descanso = input("Tempo de descanso:")
            tipo_exercicio = input("Escolha o tipo de exercício: 0) Muscular - Superior 1) Muscular - Inferior 2) Cardiovascular")
            return {"nome":nome, "serie":serie, "repeticao":repeticao, "tempo_descanso":tempo_descanso, "tipo_exercicio":tipo_exercicio}

    