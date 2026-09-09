
print ("-"*51)
print ("="*20, "Questão 3", "="*20)
print (f"Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como\nchaves e seus significados como valores. seu programa deve solicitar ao usuáro quantas\npalavras devem ser cadastradas, cadastrar as palavras e seus significados e, ao final,\nexibir todas as palavras e significaos cadastrados") 
print ("-"*51)


amount=int(input('Quantas palavras você deseja cadastrar? '))
dictionary={} 
amount_in=0

while amount_in<amount:
    word=input('Qual palavra deve ser adicionada ao dicionário? ')
    means=input('Qual o significado dessa palavra? \n')
    if word in dictionary:
        print('A palavra ja foi cadastrada! ')
    else:
        dictionary[word] = means
        amount_in=amount_in+1

for k, i in dictionary.items():
    print (f'palavra: {k}, seu significado: {i}.')


    
