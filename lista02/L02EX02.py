print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 2----------------------------------")
print ("\t\t\n\n\nFaça um programa para escrever a contagem regressiva do lançamento")
print("\tde um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.")
print("\n\n\n------------------------------------------------------------------------")

print("Começando contagem regressiva para o lançamento do foguete...")

#setando a variavel
i=10
for i in range (10, -1, -1):
    print (f"{i}...")

#Ultima fala da contagem do foguete
print ("FOGO!")