print('='*25, 'Simulação de Prova', '='*25)
print('-'*25, 'Exercício 2', '-'*25)
print("Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.\nAceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e\nexiba os números do menor para o maior.\n")
print('='*50)

'''Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
exiba os números do menor para o maior.'''
i=0
numbers = []
print ("Coloque os 15 números da tabela, sem repeti-las: ")
while i<15:
    number= int(input(f'→ '))
    if number >= 1 and number<=75:
        if number in numbers:
            print (f'{number} já está na lista.\n')
        else:
            numbers.append(number)
            print(f'cadastrado com sucesso!\n')
            i=1+i
    else:
        print ("Número menor que 1 ou maior que 75.")

numbers.sort()

for item in numbers:
    print (f'- {item}')

