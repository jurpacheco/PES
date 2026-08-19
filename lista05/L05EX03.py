from math import pi
print ("==================================Lista de Exercícios 5======================================")
print ("\n---------------------------------------Questão 3-------------------------------------------")
print ("\n\n\t3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu\n\tprograma principal deve solicitar a altura e o raio do cilindro em metros, chamar a função\n\te exibir o resultado na tela.")
print ("\n\n------------------------------------------------------------------------------------------")



def volume(a,b):
    vol=pi*(a**2)*b
    return vol

r= float(input('Qual o raio do cilindro em metros? Insira : '))
h= float(input('Qual a altura do cilindro em metros? Insira : '))
area = volume(r, h)

print (f'a área do cilindro é de {area:.2f} metros.')