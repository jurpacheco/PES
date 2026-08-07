print ("========================Lista de Exercícios 3============================")
print ("\n------------------------------Questão 1----------------------------------")
print ("\n\n\tImplemente um programa com um cadastro de idades de 6 alunos utilizando lista. O")
print ("\tprograma deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se")
print ("\tapresentar apenas as idades que forem maiores ou iguais a 16.")
print ("\n------------------------------------------------------------------------------------------")

#Solicito ao usuario a idaDE DOS alunos
ages = list(map(int, input("Digite as idades dos 6 alunos, separadas por espaço: ").split()))

#percorre a lista de idades e verifica quais são maiores ou iguais a 16
for i in range(len(ages)):
    if ages[i] >= 16:
        print(f"A idade do aluno {i+1} é: {ages[i]}")