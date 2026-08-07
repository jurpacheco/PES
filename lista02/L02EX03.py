print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 3----------------------------------")
print ("\t\t\n\n\nFaça um programa que exiba na tela a contagem iniciando no número 1 e indo até um")
print("\tnúmero informado pelo usuário. Considere que a contagem pode ser até um número ")
print("\tpositivo ou até um número negativo.")
print("\n\n\n------------------------------------------------------------------------")

#vendo qual número o usuário escolheu
number= int(input("Escolha um número pra ver quais existem entre ele e 1! insira:"))

#fazendo 

if number <=0:
    for number in range (1, number-1, -1):
        print(f"• {number}")
else:
    for number in range (1, number+1, 1):
        print (f"• {number}")

