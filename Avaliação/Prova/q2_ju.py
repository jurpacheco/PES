from time import sleep
print ("-"*51)
print ("="*20, "Questão 2", "="*20)
print (f"Utilizando alguma estrutura de repetição,\nfaça um programa para escrever a contagem\nregressiva do lançamento de um foguete.\nO programa deve imprimir: '10, 9, 8, ...., 1, 0 e fogo!'") 
print ("-"*51)


i=10

while i>-1:
    print (f'{i}...')
    i=i-1
    sleep (0.7)
sleep (1)
print ('e FOGO!')