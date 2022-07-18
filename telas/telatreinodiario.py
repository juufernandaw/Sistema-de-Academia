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
            [sg.Radio('Efetuar Check-in!', "RD1", key='1')],
            [sg.Radio('Consultar meu desempenho!', "RD1", key='2')],
            [sg.Radio('Sair', "RD1", key='0')],
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
        # print("----- ABA ALUNO -----")
        # print("Olá Aluno, o quê deseja fazer hoje?")
        # print("1 - Efetuar Check-in!")
        # print("2 - Consultar meu desempenho!")
        # print("0 - Sair")
        # escolha = int(input())
        # return escolha

    def layout_printar_tela_treino_diario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text("Ola Personal, você que você deseja?", font=("Helvica", 25))],
            [sg.Text('O que você deseja fazer hoje ?', font=("Helvica", 15))],
            [sg.Radio('Consultar o desempenho', "RD1", key='1')],
            [sg.Radio('Voltar ao menu inicial', "RD1", key='2')],
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
        self.printar_tela_escolher_aluno()
        button, values = self.__window.Read()
        cpf = values['cpf']
        if button in (None, 'Cancelar'):
            self.close()
        self.close()
        return cpf
        # print("Digite o cpf do aluno, para saber seu desempenho:")
        # escolha = input()
        # return escolha

    def montar_treino_diario(self, lista_treinos):
        sg.ChangeLookAndFeel('DarkTeal4')
        contador = 0
        for treino in lista_treinos:
            layout = [
                [sg.Text("Qual treino você fará hoje?", font=("Helvica", 25))],
                [sg.Text(f"{contador} - Nome do treino: {treino.nome}", font=("Helvica", 15))],
                [sg.Text('Treino escolhido:', size=(15, 1)), sg.InputText('', key='treino')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            # print(contador, " - Nome do treino:", treino.nome)
            contador += 1
        self.__window = sg.Window("Seleciona treino").Layout(layout)
        # resposta = int(input("Qual treino você fará hoje?"))
        button, values = self.__window.Read()
        escolha_treino = values['treino']
        if button in (None, 'Cancelar'):
            self.close()
        self.close()
        return escolha_treino
        # return resposta

    def layout_montar_treino_diario_2(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f"Você gostaria de fazer outro treino?", font=("Helvica", 25))],
            [sg.Radio('Sim', 'RD1', key='1')],
            [sg.Radio('Não', 'RD1', key='2')],
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
        self.close()
        return opcao

        # print(f"Você gostaria de fazer outro treino?")
        # opcao = int(input("1 - Sim ou 2 - Não"))
        # return opcao

    def mostrar_dias_treino(self, dias):
        sg.popup(f"Parabéns! Você foi {dias} dia(s) treinar")

    def contar_calorias(self, calorias):
        sg.popup(f"Parabéns! Você perdeu {calorias} calorias")

    def mostrar_dias_treino_aluno(self, aluno, dias):
        sg.popup(f"O aluno do cpf {aluno} foi {dias} dia(s) treinar")

    def contar_calorias_aluno(self, aluno, calorias):
        sg.popup(f"O aluno do cpf {aluno} perdeu {calorias} calorias")
