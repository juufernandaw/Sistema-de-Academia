class LoginExistente(Exception):
    def __init__(self, msg):
        self.msg = "Aluno com login já cadastrado."
        super().__init__(self.msg)