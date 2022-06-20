class CpfExistente(Exception):
    def __init__(self, msg):
        self.msg = "Aluno com cpf já cadastrado."
        super().__init__(self.msg)