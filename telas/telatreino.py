

class TelaTreino():

    def mostrar_tela_treino(self, treino): #mostra tela com os dados do treino
        print("Nome do treino",treino["nome"])
        for exercicio in treino["exercicios"]:
            print("Nome do exercício",exercicio.nome)
            print("Série do exercício",exercicio.serie)
            print("Repetição do exercício",exercicio.repeticao)
            print("Tempo de descanso do exercício",exercicio.tempo_descanso)
            print("Tipo do exercício",exercicio.tipo_exercicio)

    def montar_treino(self): #mostra tela perguntando se quer cadastrar novo treino
        opcao = int(input("Deseja cadastrar um novo treino? 1- Sim 2- Não"))
        if opcao == 1:
            nome_treino = input("Nome do treino:")
        else:
            nome_treino = None
        return opcao, nome_treino
            
    def montar_exercicio(self, lista_tipos): #mostra tela perguntando se quer cadastrar novo exercício
        opcao = int(input("Deseja cadastrar um novo exercício? 1- Sim 2- Não"))
        if opcao == 1:
            nome = input("Nome:")
            serie = input("Série:")
            repeticao = input("Repetição:")
            tempo_descanso = input("Tempo de descanso:")
            num=0
            for tipo_exercicio in lista_tipos:
                print("Número:", num, ". Categoria do exercício:",tipo_exercicio[0])
                num+=1
            tipo_exercicio = input("Informe o número correspondente ao exercício desejado") #chamar a lista de tipos_chamados
        else:
            nome, serie, repeticao, tempo_descanso, tipo_exercicio = None
        return opcao,{"nome":nome, "serie":serie, "repeticao":repeticao, "tempo_descanso":tempo_descanso, "tipo_exercicio":tipo_exercicio}


    