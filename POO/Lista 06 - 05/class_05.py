'''5 – Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.'''

class Pessoa:
    def __init__ (self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    def escrevendo(self):
        return f"{self.nome}, {self.idade} anos, {self.altura}m de altura e {self.peso}Kg."
    def imc(self):
        imc=self.peso/self.altura**2
        return imc
    def nome_imc(self):
        return f"O imc de {self.nome} é de {self.imc()}"