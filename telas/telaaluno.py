import PySimpleGUI as sg


class TelaAluno:

    def __init__(self):
        self.__window = None
        self.layout_mexer_aluno()
        self.layout_pegar_cpf()

    def mostrar_msg(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def layout_abre_tela_inicial(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('----- ABA ALUNO -----', font=("Helvica", 25))],
            [sg.Text('O que você deseja fazer hoje?', font=("Helvica", 15))],
            [sg.Radio('Consultar treino', "RD3", key='1')],
            [sg.Radio('Fazer Checkin e Desempenho', "RD3", key='2')],
            [sg.Radio('Retornar', "RD3", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('mx').Layout(layout)

    def abre_tela_inicial_tela_aluno(self):
        self.layout_abre_tela_inicial()
        button, values = self.__window.Read()
        escolha = 0
        if values['1']:
            escolha = 1
        elif values['2']:
            escolha = 2
        elif values['0'] or button in (None, 'Retornar'):
            escolha = 0
        self.close()
        return escolha

    def mostrar_aluno(self, dados_aluno):  # mostra os dados do aluno
        infos_aluno = ""
        for aluno in dados_aluno:
            infos_aluno += "Nome:" + aluno["nome"] + '\n'
            infos_aluno += "Login:" + aluno["login"] + '\n'
            infos_aluno += "Senha:" + aluno["senha"] + '\n'
            infos_aluno += "CPF:" + aluno["cpf"] + '\n'
            for treino in aluno["treinos"]:
                print("treino", treino)
                print("treinos aluno: ", aluno["treinos"])
                print("exercicios ", treino.exercicios)
                infos_aluno += "Nome do treino:" + treino.nome + '\n'
                for exercicio in treino.exercicios:
                    print("exercicio ", exercicio)
                    infos_aluno += "Nome do exercício:" + exercicio.nome + '\n'
                    infos_aluno += "Repeticao:" + exercicio.repeticao + '\n'
                    infos_aluno += "Series:" + exercicio.serie + '\n'
                    infos_aluno += "Tempo descanso:" + exercicio.tempo_descanso + '\n' + '\n'
                    #infos_aluno += "Tipo exercicio:" + exercicio.tipo_exercicio.categoria_exercicio + '\n' + '\n'
        sg.popup("------DADOS ALUNO------", infos_aluno)
        self.close()

    def mostrar_treino_aluno(self, treinos):
        botoes_treinos = []
        for id, treino in enumerate(treinos):
            botoes_treinos.append([sg.Radio(id, "RD6", key=treino.nome)])
        layout = [
            [sg.Text('Qual treino você deseja alterar?')],
            botoes_treinos,
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        treino_escolhido = values[treino.nome]
        self.close()
        return treino_escolhido

    def escolher_opcao_treino(self):
        self.layout_escolher_opcao_treino()
        button, values = self.__window.Read()
        escolha = 0
        if values['1']:
            escolha = 1
        elif values['2']:
            escolha = 2
        self.close()
        return escolha

    def layout_escolher_opcao_treino(self): #necessário mudar
        layout = [
            [sg.Text('O que você deseja fazer?', font=("Helvica", 25))],
            [sg.Radio('Excluir um treino de um aluno', "RD2", key='1')],
            [sg.Radio('Adicionar um treino ao aluno', "RD2", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)

    def pega_dados_aluno(self):
        self.layout_pega_dados_aluno()
        button, values = self.__window.Read()
        nome = values['nome']
        login = values['login']
        senha = values['senha']
        cpf = values['cpf']
        self.close()
        return {"nome": nome, "login": login, "senha": senha, "cpf": cpf}

    def layout_pega_dados_aluno(self):
        layout = [
            [sg.Text('Digite o nome do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='nome')],
            [sg.Text('Digite o login do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='login')],
            [sg.Text('Digite a senha do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='senha')],
            [sg.Text('Digite o cpf do aluno:', font=("Helvica", 25))],
            [sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)

    def mexer_aluno(self):
        self.layout_mexer_aluno()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        elif values['6']:
            opcao = 6
        elif button == 'Retornar':
            opcao = 0
        self.close()
        return opcao

    def layout_mexer_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('----- INÍCIO -----', font=("Helvica", 25))],
            [sg.Text('----- ABA ALUNO -----', font=("Helvica", 25))],
            [sg.Text('O que você deseja fazer hoje?', font=("Helvica", 15))],
            [sg.Radio('Cadastrar aluno', "RD3", key='1')],
            [sg.Radio('Alterar aluno', "RD3", key='2')],
            [sg.Radio('Excluir aluno', "RD3", key='3')],
            [sg.Radio('Listar alunos', "RD3", key='4')],
            [sg.Radio('Consultar aluno', "RD3", key='5')],
            [sg.Radio('Consultar Desempenho do aluno', "RD3", key='6')],
            [sg.Button('Confirmar'), sg.Cancel('Retornar')]
        ]
        self.__window = sg.Window('mx').Layout(layout)

    def layout_pegar_nome(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite o nome do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='nome')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)

    def pegar_nome(self):
        self.layout_pegar_nome()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            nome = None
        else:
            nome = values['nome']
        self.close()
        return nome

    def pegar_cpf(self):
        self.layout_pegar_cpf()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            cpf = None
        else:
            cpf = values['cpf']
        self.close()
        print("CPF:", cpf)
        return cpf

    def layout_pegar_cpf(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite o cpf do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='cpf')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)

    def pegar_login(self):
        self.layout_pegar_login()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            login = None
        else:
            login = values['login']
        self.close()
        return login

    def layout_pegar_login(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite o login do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='login')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)

    def pegar_senha(self):
        self.layout_pegar_senha()
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            senha = None
        else:
            senha = values['senha']
        self.close()
        return senha

    def layout_pegar_senha(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
                [sg.Text('Digite a senha do aluno:', font=("Helvica", 25))],
                [sg.InputText('', key='senha')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
        self.__window = sg.Window('').Layout(layout)

    def layout_alterar_aluno(self, aluno):
        layout = [
            [sg.Text('Nome:', font=("Helvica", 25))],
            [sg.InputText(aluno["nome"], key='nome')],
            [sg.Text('CPF:', font=("Helvica", 25))],
            [sg.InputText(aluno["cpf"], key='cpf')],
            [sg.Text('Login:', font=("Helvica", 25))],
            [sg.InputText(aluno["login"], key='login')],
            [sg.Text('Senha:', font=("Helvica", 25))],
            [sg.InputText(aluno["senha"], key='senha')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        cpf = values['cpf']
        login = values['login']
        senha = values['senha']
        self.close()
        return {"nome": nome, "cpf": cpf, "login": login, "senha": senha}
