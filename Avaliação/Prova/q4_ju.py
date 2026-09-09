print ("-"*51)
print ("="*20, "Questão 4", "="*20)
print (f"faça um programa que exiba nna tela a  tabuada de um número informado pelo\nusuário. Vamos supor que o número informado seja o 2, então o programa deve exibir\no seguinte resultado na tela:") 
print ("\ntabuada do 2\n2 x 0 = 0\n2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n")
print ("-"*51)

number=int(input(f'\nO número que você deseja saber a tabuada: '))
print (f'\nTABUADA DO NÚMERO {number}')
i=0
while i<=10:
    times=number*i
    print(f'{number} x {i} = {times}')
    i=i+1


