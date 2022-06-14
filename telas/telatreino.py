class TelaTreino():

    def mostrar_tela_treino():
        pass

    def montar_treino(self):
        opcao = int(input("Deseja cadastrar um novo treino? 1- Sim 2- Não"))
        if opcao == 1:
            nome_treino = input("Nome do treino:")
        else:
            nome_treino = None
        return opcao, nome_treino
            
        #cadastro exercicio
    
    def montar_exercicio(self,lista_tipos=[]):
        opcao = int(input("Deseja cadastrar um novo exercício? 1- Sim 2- Não"))
        if opcao == 1:
            nome = input("Nome:")
            serie = input("Série:")
            repeticao = input("Repetição:")
            tempo_descanso = input("Tempo de descanso:")
            tipo_exercicio = input("Escolha o tipo de exercício: 0) Muscular - Superior 1) Muscular - Inferior 2) Cardiovascular")#chamar a lista de tipos_chamados
        else:
            nome, serie, repeticao, tempo_descanso, tipo_exercicio = None
        return opcao,{"nome":nome, "serie":serie, "repeticao":repeticao, "tempo_descanso":tempo_descanso, "tipo_exercicio":tipo_exercicio}


    