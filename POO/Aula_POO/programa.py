from minhas_classes import Estudante

estudante1 = Estudante("João", "Silva", 20, "123.456.789-00", "M")
estudante2 = Estudante("Maria", "Souza", 22, "987.654.321-00", "F")

# criar objeto com input
n=input("Digite o nome do estudante: ")
s=input("Digite o sobrenome do estudante: ")
i=int(input("Digite a idade do estudante: "))
c=input("Digite o CPF do estudante: ")
sex=input ("O sexo do estudante:")
estudante3 = Estudante(n, s, i, c, sex)

#como ler os atributos do objeto
print(estudante1.nome)

#como mudar os atributos do objeto
estudante1.nome = "Ricardo"
print(estudante1.nome)
