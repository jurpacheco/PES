from time import sleep

print ("==================================Lista de Exercícios 5======================================")
print ("\n---------------------------------------Questão 2-------------------------------------------")
print ("\n\n\t2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou\n\tímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o\n\tresultado na tela.")
print ("\n\n------------------------------------------------------------------------------------------")

def oddeven(a):
    div = a%2
    if div == 0:
        return "par"
    else:
        return "impar"

v1= int(input('\nDigite o número'))

result = oddeven(v1)

print('o número é..')
sleep(0.5)
print (result)