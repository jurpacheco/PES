print ("========================Lista de Exercícios 01============================")
print ("\n------------------------------Questão 4----------------------------------")
print ("\n\n Solicite ao usuário um superpoder entre três opções: “força”, “velocidade” ou “voo”")
print ("\tUse estruturas de decisão para exibir uma frase que diga qual super-herói você seria com")
print ("\tbase na escolha:")
print ("\t- Se escolher “força”: exiba “Você seria o Hulk!”;")
print ("\t- Se escolher “velocidade”: exiba “Você seria o Flash!”;")
print ("\t- Se escolher “voo”: exiba “Você seria o Superman!”.")
print ("\n\n-----------------------------------------------------------------------------")

#Dou ao usuario tres opções para que não haja perigo de ter inconsistencia de dados
print ("\n\n\nPara saber qual herói você seria, escolha o poder que você gostaria de ter:")
print ("1- Super-força ")
print ("2- Supervelocidade ")
print ("3- Vôo")

#Vendo qual dos poderes o usuário prefere
answer = input("A resposta deve ser um dos números (1, 2 ou 3):")

#qual o personagem que o usuario seria

if answer == "1":
    print ("Você seria o Hulk!")
elif answer == "2":
    print ("Você seria o Flash!")
elif answer == "3":
    print ("Você seria o Super Homem!")

#Garantindo que o usuário so escreva 1, 2 ou 3
if answer not in ["1", "2", "3"]:
    print ("Sua resposta é inválida!")