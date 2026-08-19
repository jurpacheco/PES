#exemplo 00
from time import sleep
print('exemplo 00 - Como utiliza função')
lista=['a', 'b', 'c']
qnt=len(lista)
print (f'len de uma lista usando len(): {qnt}')


#exemplo 01
print(f'\n\nexemplo 01 - criando funções')
print(f'\ndef bom_dia():')
print("    print ('Oi, eu sou uma função que diz apenas...')")
print("    sleep (1)")
print("    print ('Bom dia!')")
print(f'\nbom_dia()')

def bom_dia():
    print (f'\nOi, eu sou uma função que diz apenas...')
    sleep (1)
    print ('Bom dia!')

bom_dia()


#exemplo 02
print(f'\n\nexemplo 02 - criando funções sem retorno')
def soma(a, b):
    resposta = a + b
    print (resposta)

v1= int(input('\nDigite o primeiro valor: '))
v2= int(input('Digite o segundo valor: '))
soma(v1, v2)


#exemplo 03
print(f'\n\nexemplo 03 - criando funções com retorno')
def fa2ce(tempf):
    c = (tempf - 32) * 5/9
    return c

#programa principal
tempc=fa2ce(float(input('\nDigite a temperatura em Fahrenheit: ')))
print (f'A temperatura em Celsius é: {tempc:.2f}ºC')


                   

