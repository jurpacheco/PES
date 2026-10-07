class Estudante:
    def __init__(self, nome, sobrenome, idade, cpf, sexo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cpf = cpf
        self.sexo = sexo

    def artigo(self):
        if self.sexo == "M":
            return "O"
        else:
            return "A"