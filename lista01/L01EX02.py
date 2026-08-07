print ("========================Lista de Exercícios 01============================")
print ("\n------------------------------Questão 02----------------------------------")
print ("\n\nPeça a idade de uma pessoa. Usando estruturas de decisão, exiba uma mensagem ")
print ("com a classificação indicativa permitida para essa pessoa:")
print ("\tMenor que 10 anos: 'Você pode assistir apenas a filmes com classificação Livre'.")
print ("\tEntre 12 e 13 anos: 'Você pode assistir a filmes com classificação até 12 anos'.")
print ("\tEntre 14 e 15 anos: 'Você pode assistir a filmes com classificação até 14 anos.'")
print ("\tEntre 16 e 17 anos: 'Você pode assistir a filmes com classificação até 16 anos.'")
print ("\t18 anos ou mais: 'Você pode assistir a filmes com classificação até 18 anos.'")
print ("\n\n-----------------------------------------------------------------------------")


# pedindo a idade do usuário

idade= int(input("\n\n\nDiga-nos sua idade para que possamos saber qual a classificação indicativa permitida para você:"))

# uso a a variavel idade para saber a idade e qual classificação o usuário deve seguir com if
if idade <10:
    print ("Você pode assistir apenas a filmes com classificação Livre")
elif 10>= idade <=11:
    print ("Você pode assistir a filmes com classificação até 10 anos")
elif 12<= idade <=15:
    print ("Você pode assistir a filmes com classificação até 12 anos")
elif 16<= idade <=17:
    print ("Você pode assistir a filmes com classificação até 16 anos.")
elif idade >= 18:
    print ("Você pode assistir a filmes com classificação até 18 anos.")