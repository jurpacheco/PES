from time import sleep
print ("==================================Lista de Exercícios 5======================================")
print ("\n---------------------------------------Questão 1-------------------------------------------")
print ("\n\n\t1 – Crie um programa com uma função para calcular a média aritmética simples entre 3\n\tnotas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.")
print ("\n\n------------------------------------------------------------------------------------------")

def grade(a, b, c):
    sum = a+b+c
    div = sum/3
    return div

g1= int(input('\nDigite a primeira nota: '))
g2= int(input('Digite a segunda nota: '))
g3= int(input('Digite a terceira nota: '))
average= grade(g1, g2, g3)

print('sua média é...')
sleep(0.5)
print (average)

