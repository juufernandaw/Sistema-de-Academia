class TelaTreino():

    def mostrar_msg(self, msg: str):
        print(msg)

    def mostrar_tela_treino(self, treino):  # mostra tela com os dados do treino
        print("Nome do treino", treino["nome"])
        for exercicio in treino["exercicios"]:
            print("Nome do exercício", exercicio.nome)
            print("Série do exercício", exercicio.serie)
            print("Repetição do exercício", exercicio.repeticao)
            print("Tempo de descanso do exercício", exercicio.tempo_descanso)
            print("Tipo do exercício", exercicio.tipo_exercicio.categoria_exercicio)

    def montar_treino(self):  # mostra tela perguntando se quer cadastrar novo treino
        opcao = int(input("Deseja cadastrar um novo treino? 1- Sim 2- Não"))
        if opcao == 1:
            nome_treino = input("Nome do treino:")
        else:
            nome_treino = None
        return opcao, nome_treino

    def montar_exercicio(self, lista_tipos):  # mostra tela perguntando se quer cadastrar novo exercício
        opcao = int(input("Deseja cadastrar um novo exercício? 1- Sim 2- Não"))
        if opcao == 1:
            nome = input("Nome:")
            serie = input("Série:")
            repeticao = input("Repetição:")
            tempo_descanso = input("Tempo de descanso:")
            num = 0
            for tipo_exercicio in lista_tipos:
                print("Número:", num, ". Categoria do exercício:", tipo_exercicio.categoria_exercicio)
                num += 1
            tipo_exercicio = int(input("Informe o número correspondente ao exercício desejado"))  # chamar a lista de
            # tipos_chamados
            return opcao, {"nome": nome, "serie": serie, "repeticao": repeticao, "tempo_descanso": tempo_descanso,
                           "tipo_exercicio": tipo_exercicio}
        else:
            return opcao, None

    def selecionar_treino_por_nome(self):
        nome_treino = input("Nome do treino:")
        return nome_treino

    def escolher_alteracao_treino(self):
        opcao = int(input("Escolha o que deseja fazer: 1) Alterar nome do treino 2) Excluir e incluir novos "
                          "exercícios no treino "))
        return opcao

    def mexer_treino(self):
        print("----- INÍCIO -----")
        print("----- ABA TREINO -----") 
        print("O que você deseja fazer hoje? Digite o número correspondente:")
        print("1 - Cadastrar treino")
        print("2 - Alterar treino")
        print("3 - Excluir treino")
        print("4 - Listar treinos")
        print("5 - Consultar treino")
        print("6 - Retornar à tela inicial")

        opcao = int(input())
        return opcao
