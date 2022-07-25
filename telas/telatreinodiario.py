import PySimpleGUI as sg


class TelaTreinoDiario:
    def __init__(self):
        self.__window = None
        self.layout_mostrar_tela_desempenho()
        self.layout_printar_tela_treino_diario()
        self.layout_printar_tela_escolher_aluno()
        self.layout_montar_treino_diario_2()

    def close(self):
        self.__window.Close()

    def mensagem(self, msg):
        sg.popup(msg)

    def layout_mostrar_tela_desempenho(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("----- ABA ALUNO -----", font=("Helvica", 25))],
            [sg.Text('Olá, o quê deseja fazer hoje?', font=("Helvica", 15))],
            [sg.Radio('Efetuar Check-in!', "RD12", key='1')],
            [sg.Radio('Consultar meu desempenho!', "RD12", key='2')],
            [sg.Radio('Sair', "RD12", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Tela Desempenho by Aluno').Layout(layout)

    def mostrar_tela_desempenho(self):
        self.layout_mostrar_tela_desempenho()
        button, values = self.__window.Read()
        escolha = 0
        if values['1']:
            escolha = 1
        elif values['2']:
            escolha = 2
        elif values['0'] or button in (None, 'Cancelar'):
            escolha = 0
        self.close()
        return escolha

    def layout_printar_tela_treino_diario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Ola Personal, você que você deseja?", font=("Helvica", 25))],
            [sg.Text('O que você deseja fazer hoje ?', font=("Helvica", 15))],
            [sg.Radio('Consultar o desempenho', "RD11", key='1')],
            [sg.Radio('Voltar ao menu inicial', "RD11", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Personal').Layout(layout)

    def printar_tela_treino_diario(self):  # checar se tá sendo usado
        self.layout_printar_tela_treino_diario()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
            self.close()
        return opcao
        # print("Ola Professor, você que você deseja?")
        # print("1 - consultar o desempenho")
        # print("2 - Voltar ao menu inicial")
        # escolha = int(input())
        # return escolha

    def layout_printar_tela_escolher_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Digite o cpf do aluno, para saber seu desempenho:", font=("Helvica", 25))],
            [sg.Text('O que você deseja fazer hoje ?', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Personal').Layout(layout)

    def printar_tela_escolher_aluno(self):  # qual aluno ele quer ve o desempenho
        self.layout_printar_tela_escolher_aluno()
        button, values = self.__window.Read()
        cpf = values['cpf']
        if button in (None, 'Retornar'):
            self.close()
        self.close()
        return cpf
        # print("Digite o cpf do aluno, para saber seu desempenho:")
        # escolha = input()
        # return escolha

    def montar_treino_diario(self, lista_treinos):
        global escolha_treino, id
        sg.ChangeLookAndFeel('DarkTeal4')
        botoes_treinos = []
        contador = 0
        for id, treino in enumerate(lista_treinos):
            botoes_treinos.append([sg.Radio(treino.nome, "RD1", key=id)])
        layout = [
            [sg.Text("Qual treino você fará hoje?", font=("Helvica", 25))],
            botoes_treinos,
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window("Seleciona treino").Layout(layout)
        button, values = self.__window.Read()
        for treinos in lista_treinos:
            if id == contador:
                escolha_treino = contador
                contador += 1
        if button in (None, 'Retornar'):
            self.close()
        self.close()
        return escolha_treino

    # def montar_treino_diario(self, lista_treinos):
    #         contador = 0
    #         for treino in lista_treinos:
    #             print(contador, " - Nome do treino:", treino.nome)
    #             contador += 1
    #         resposta = int(input("Qual treino você fará hoje?"))
    #         return resposta

    def listar_treino_escolhido(self, lista: []):  # método n usado
        layout = [
            sg.popup_scrolled(*lista, title="Treino Escolhido")
        ]

    def layout_montar_treino_diario_2(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f"Você gostaria de fazer outro treino?", font=("Helvica", 25))],
            [sg.Radio('Sim', 'RD10', key='1')],
            [sg.Radio('Não', 'RD10', key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Personal').Layout(layout)

    def montar_treino_diario_2(self):
        self.layout_montar_treino_diario_2()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
        # print(f"Você gostaria de fazer outro treino?")
        # opcao = int(input("1 - Sim ou 2 - Não"))
        # return opcao

    def mostrar_dias_treino(self, dias):
        #sg.popup("------Dias de Treino------", dias)
        sg.popup(f"Parabéns! Você foi {dias} dia(s) treinar")

    def contar_calorias(self, calorias):
        # sg.popup("------Calorias Perdidas------", dias)
        sg.popup(f"Parabéns! Você perdeu {calorias} calorias")

    def mostrar_dias_treino_aluno(self, aluno, dias):
        sg.popup(f"O aluno do cpf {aluno} foi {dias} dia(s) treinar")

    def contar_calorias_aluno(self, aluno, calorias):
        sg.popup(f"O aluno do cpf {aluno} perdeu {calorias} calorias")
