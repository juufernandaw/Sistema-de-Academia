import PySimpleGUI as sg


class TelaTreino:

    def __int__(self):
        self.__window = None

    def mostrar_msg(self, msg: str):
        sg.popup("", msg)

    def layout_alterar_treino(self, treino: {}):
        botoes_exercicios = []
        print("botoes_exer", botoes_exercicios)
        print("treino", treino)
        for i, exercicio in enumerate(treino["exercicios"]):
            print("treino exercicios", treino["exercicios"])
            print("exercicio", exercicio)
            botoes_exercicios.append([sg.InputText(exercicio["nome"], key=exercicio["nome"])])
            botoes_exercicios.append([sg.InputText(exercicio["repeticao"], key=exercicio["repeticao"])])
            botoes_exercicios.append([sg.InputText(exercicio["serie"], key=exercicio["serie"])])
            botoes_exercicios.append([sg.InputText(exercicio["tempo_descanso"], key=exercicio["tempo_descanso"])])
        layout = [
            [sg.Text('Nome do treino:', font=("Helvica", 25))],
            [sg.InputText(treino["nome"], key='nome')],
            [sg.Text('Exercicios', font=("Helvica", 25))],
            botoes_exercicios,
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        self.close()
        return {"nome": nome}

    def exercicio_novamente(self):
        layout = [[sg.Text('Deseja cadastrar um novo exercicio?', font=("Helvica", 25))],
            [sg.Button('Sim'), sg.Button('Nao')]]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        print("Botao", button)
        if button == 'Nao':
            opcao = 1
        else:
            opcao = 2
        self.close()
        return opcao

    def mostrar_tela_treino(self, treino):  # mostra tela com os dados do treino
        print("CHEGUEI AQUI")
        print("MISERICORDIA TREINO", treino)
        infos_treino = ""
        for t in treino:
            print("MISERICORDIA T", t)
            print("MISERICORDIA T exercicios", t["exercicios"])
            infos_treino += "Nome:" + t["nome"] + '\n'
            for exercicio in t["exercicios"]:
                infos_treino = infos_treino + "Nome:" + exercicio["nome"] + '\n'
                infos_treino = infos_treino + "Serie:" + exercicio["serie"] + '\n'
                infos_treino = infos_treino + "Repeticao:" + exercicio["repeticao"] + '\n'
                infos_treino = infos_treino + "Tempo de Descanso:" + exercicio["tempo_descanso"] + '\n'
                infos_treino = infos_treino + "Categoria:" + exercicio["tipo_exercicio"].categoria_exercicio + '\n' + '\n'
        sg.popup("------DADOS caralho------", infos_treino)
        self.close()

    def montar_treino(self):  # mostra tela perguntando se quer cadastrar novo treino
        layout = [
            [sg.Text('Digite o nome do treino:', font=("Helvica", 25))],
            [sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        self.close()
        return nome

    def montar_exercicio(self, lista_tipos):  # mostra tela perguntando se quer cadastrar novo exercício
        botoes_tipos = []
        for id, tipo_exercicio in enumerate(lista_tipos):
            botoes_tipos.append([sg.Radio(tipo_exercicio.categoria_exercicio, "RD9", key=tipo_exercicio.categoria_exercicio)])
        layout = [
            [sg.Text('Nome do exercicio:', font=("Helvica", 25))],
            [sg.InputText('', key='nome')],
            [sg.Text('Serie:', font=("Helvica", 25))],
            [sg.InputText('', key='serie')],
            [sg.Text('Repeticao:', font=("Helvica", 25))],
            [sg.InputText('', key='repeticao')],
            [sg.Text('Tempo de descanso:', font=("Helvica", 25))],
            [sg.InputText('', key='tempo_descanso')],
            [sg.Text('Tipo do exercício:', font=("Helvica", 25))],
            botoes_tipos,
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        tipo_escolhido = values[tipo_exercicio.categoria_exercicio]
        nome = values['nome']
        serie = values['serie']
        repeticao = values['repeticao']
        tempo_descanso = values['tempo_descanso']
        self.close()
        return {"nome": nome, "serie": serie, "repeticao": repeticao, "tempo_descanso": tempo_descanso, "tipo_exercicio": tipo_escolhido}

    def selecionar_treino_por_nome(self):
        layout = [
            [sg.Text('Digite o nome do treino:', font=("Helvica", 25))],
            [sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        self.close()
        return nome


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
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        escolha = 0
        if button == 'Retornar':
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
        self.close()
        return escolha

    def close(self):
        self.__window.Close()