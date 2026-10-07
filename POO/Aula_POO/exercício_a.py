from minhas_classes import Estudante

estudante_1= Estudante("Clara", "Olivette Queiroz", 17, "000.000.000-00", "F")
estudante_2= Estudante("Felipe", "Tomé Pacheco", 16, "111.111.111-11", "M")
estudante_3= Estudante("Vitória Valentina", "Ortiz", 17, "222.222.222-22", "F")

        

print (f"{estudante_1.artigo()} {estudante_1.nome} tem {estudante_1.idade}")
print (f"{estudante_2.artigo()} {estudante_2.nome} tem {estudante_2.idade}")
print (f"{estudante_3.artigo()} {estudante_3.nome} tem {estudante_3.idade}")

'''
5 – Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.
6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
conforme abaixo:'''