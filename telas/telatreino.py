import PySimpleGUI as sg


class TelaTreino():

    def __int__(self):
        self.__window = None

    def mostrar_msg(self, msg: str):
        sg.popup("", msg)

    def mostrar_tela_treino(self, treino):  # mostra tela com os dados do treino
        infos_treino = "Nome:" + treino["nome"] + '\n'
        for exercicio in treino["exercicios"]:
            infos_treino = infos_treino + "Nome:" + exercicio["nome"] + '\n'
            infos_treino = infos_treino + "Serie:" + exercicio["serie"] + '\n'
            infos_treino = infos_treino + "Repeticao:" + exercicio["repeticao"] + '\n'
            infos_treino = infos_treino + "Tempo de Descanso:" + exercicio["tempo_descanso"] + '\n'
            infos_treino = infos_treino + "Categoria:" + exercicio["tipo_exercicio"].categoria_exercicio + '\n' + '\n'
        sg.popup("------DADOS TREINO------", infos_treino)

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
        layout = [
            [sg.Text('Digite o nome do treino:', font=("Helvica", 25))],
            [sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        return nome

    def escolher_alteracao_treino(self):
        layout = [
            [sg.Text('O que você deseja fazer?', font=("Helvica", 25))],
            [sg.Radio('Alterar nome do treino', "RD7", key='1')],
            [sg.Radio('Excluir e incluir novos exercícios no treino', "RD7", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        escolha = 0
        if values['1']:
            escolha = 1
        elif values['2']:
            escolha = 2
        return escolha

    def mexer_treino(self):
        layout = [
            [sg.Text('----- INÍCIO -----', font=("Helvica", 25))],
            [sg.Text('----- ABA TREINO -----', font=("Helvica", 25))],
            [sg.Text('O que você deseja fazer?', font=("Helvica", 25))],
            [sg.Radio('Cadastrar treino', "RD8", key='1')],
            [sg.Radio('Alterar treino', "RD8", key='2')],
            [sg.Radio('Excluir treino', "RD8", key='3')],
            [sg.Radio('Listar treinos', "RD8", key='4')],
            [sg.Radio('Consultar treino', "RD8", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        escolha = 0
        if values['1']:
            escolha = 1
        elif values['2']:
            escolha = 2
        elif values['3']:
            escolha = 3
        elif values['4']:
            escolha = 4
        elif values['5']:
            escolha = 5
        return escolha
