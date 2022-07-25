import PySimpleGUI as sg
from excecoes.treinoinvalidoException import TreinoInvalidoException


class TelaTreino:

    def __int__(self):
        self.__window = None

    def mostrar_msg(self, msg: str):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def layout_alterar_treino(self, treino: {}):
        botoes_exercicios = []
        for i, exercicio in enumerate(treino["exercicios"]):
            botoes_exercicios.append([sg.InputText(exercicio.nome, key=exercicio.nome)])
            botoes_exercicios.append([sg.InputText(exercicio.repeticao, key=exercicio.repeticao)])
            botoes_exercicios.append([sg.InputText(exercicio.serie, key=exercicio.serie)])
            botoes_exercicios.append([sg.InputText(exercicio.tempo_descanso, key=exercicio.tempo_descanso)])
            #botoes_exercicios.append([sg.InputText(exercicio.tipo_exercicio.categoria_exercicio, key=exercicio.tipo_exercicio.categoria_exercicio)])
        layout = [
            [sg.Text('Nome do treino:', font=("Helvica", 25))],
            [sg.InputText(treino["nome"], key='nome')],
            [sg.Text('Exercícios:', font=("Helvica", 25))],
            botoes_exercicios,
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        lista_exercicios = []
        for exercicio in treino["exercicios"]:
            nome_ex = values[exercicio.nome]
            repeticao_ex = values[exercicio.repeticao]
            serie_ex = values[exercicio.serie]
            tempo_descanso_ex = values[exercicio.tempo_descanso]
            lista_exercicios.append(
                {"nome": nome_ex, "repeticao": repeticao_ex, "serie": serie_ex, "tempo_descanso": tempo_descanso_ex})
        self.close()
        return {"nome": nome, "exercicios": lista_exercicios}

    def exercicio_novamente(self):
        layout = [[sg.Text('Deseja cadastrar um novo exercicio?', font=("Helvica", 25))],
                  [sg.Button('Sim'), sg.Button('Nao')]]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        if button == 'Nao':
            opcao = 1
        else:
            opcao = 2
        self.close()
        return opcao

    def mostrar_tela_treino(self, treino):  # mostra tela com os dados do treino
        infos_treino = ""
        for t in treino:
            infos_treino += "Nome:" + t.nome + '\n'
            for exercicio in t.exercicios:
                infos_treino = infos_treino + "Nome do exercicio:" + exercicio.nome + '\n'
                infos_treino = infos_treino + "Serie:" + exercicio.serie + '\n'
                infos_treino = infos_treino + "Repeticao:" + exercicio.repeticao + '\n'
                infos_treino = infos_treino + "Tempo de Descanso:" + exercicio.tempo_descanso + '\n'
                infos_treino = infos_treino + "Tipo exercicio:" + exercicio.tipo_exercicio.categoria_exercicio + '\n' + '\n'
        sg.popup("------DADOS TREINO------", infos_treino)
        self.close()

    def montar_treino(self):  # mostra tela perguntando se quer cadastrar novo treino
        try:
            layout = [
                [sg.Text('Digite o nome do treino:', font=("Helvica", 25))],
                [sg.InputText('', key='nome')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('').Layout(layout)
            button, values = self.__window.Read()
            nome = values['nome']
            if nome is None:
                raise TreinoInvalidoException
            self.close()
            return nome
        except TreinoInvalidoException as e:
            self.mostrar_msg(e)
            self.montar_treino()

    def montar_exercicio(self, lista_tipos):  # mostra tela perguntando se quer cadastrar novo exercício
        botoes_tipos = []
        for id, tipo_exercicio in enumerate(lista_tipos):
            botoes_tipos.append(
                [sg.Radio(tipo_exercicio.categoria_exercicio, "RD9", key=tipo_exercicio.categoria_exercicio)])
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
        return {"nome": nome, "serie": serie, "repeticao": repeticao, "tempo_descanso": tempo_descanso,
                "tipo_exercicio": tipo_escolhido}

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

