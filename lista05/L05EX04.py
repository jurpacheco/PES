print ("==================================Lista de Exercícios 5======================================")
print ("\n---------------------------------------Questão 4-------------------------------------------")
print ("\n\n\t4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o\n\tresultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4\n\tnúmeros ao usuário, chamar a função e exibir o resultado da soma na tela.")
print ("\n\n------------------------------------------------------------------------------------------")

def sum(list):
    total=0
    for value in list:
        total=total+value
    return total

list=[]
values = input("Digite os 4 valores, separados por um espaço: ").split()
for element in values:
    num=int(element)
    list.append(num)

result=sum(list)
print (f"A soma de todos os valores na lista é de: {result}")