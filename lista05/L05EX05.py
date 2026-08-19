print (f'==================================== lista de exercício 05 ====================================')
print(f'------------------------------------------- Questão 5 -------------------------------------------\n')
print ("Programe um algoritmo com mais algumas funções úteis para a manipulação de listas numéricas:\n")
print ("\n\n\t• Uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso possua um ou mais elementos;\n\n\t• Uma função que receba uma lista e retorne o maior valor;\n\n\t• Uma função que receba uma lista e retorne o menor valor;\n\n\t• Uma função que receba uma lista e retorne o valor médio;\n\n\t• As funções dos itens b, c e d devem retornar -1 caso a lista esteja vazia.")
print(f'\n------------------------------------------------------------------------------------------------\n')

# setando as funções

# a) uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso possua um ou mais elementos
def isEmpty(a):
    if len(a) == 0:
        return True
    else:
        return False

# b) uma função que receba uma lista e retorne o maior valor
def highest_value(b):
    if isEmpty(b):
        return -1
    else:
        highest = max(b)
        return highest

# c) uma função que receba uma lista e retorne o menor valor
def lowest_value(c):
    if isEmpty(c):
        return -1
    else:
        lowest = min(c)
        return lowest

# d) uma função que receba uma lista e retorne o valor médio
def average_value(d):
    if isEmpty(d):
        return -1
    else:
        average = sum(d) / len(d)
        return average

# listas
empty_list = []
number_list = [10, 20, 30, 40, 50]

print(f'Lista vazia: {empty_list}')
print(f'Lista com números: {number_list}')

print(f'\nLista vazia? {isEmpty(empty_list)}')
print(f'Lista com números vazia? {isEmpty(number_list)}')

print(f'\nMaior valor da lista vazia: {highest_value(empty_list)}')
print(f'Maior valor da lista com números: {highest_value(number_list)}')

print(f'\nMenor valor da lista vazia: {lowest_value(empty_list)}')
print(f'Menor valor da lista com números: {lowest_value(number_list)}')

print(f'\nValor médio da lista vazia: {average_value(empty_list)}')
print(f'Valor médio da lista com números: {average_value(number_list)}')
