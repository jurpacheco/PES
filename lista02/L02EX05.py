print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 5----------------------------------")
print ("\n\n\n\t\tFaça um programa que exiba na tela a tabuada de um número informado pelo")
print("\tusuário. Vamos supor que o número informado seja o 2, então o programa deve exibir o ")
print("\tseguinte resultado na tela:")
'''
Tabuada do número 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
'''
print("\n\n\n------------------------------------------------------------------------")

#vejo de qual tabuada o usuario quer saber
number= int(input("De qual número você quer saber a tabuada"))


i=-1
print (f"\t\nTabuada do {number}")
while i<10:
    i=i+1
    result=number*i
    print (f"{number} x {i} = {result}")
