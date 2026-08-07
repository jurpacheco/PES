print ("========================Lista de Exercícios 3============================")
print ("\n------------------------------Questão 2----------------------------------")
print ("\n\n\tCrie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura ")
print ("\tde todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou")
print ("\treprovado(a)).")
print ("\n\n------------------------------------------------------------------------------------------")

#Solicito ao usuario as notas
grades = list(map(int, input("Digite as suas 4 notas desse semestre, separadas por espaço: ").split()))
average=0
total= 0
#percorre as notas e somo os valores
for i in range(len(grades)):
    total = total + grades[i]

#faço a média
average = total/(len(grades))
print(f"A sua média é de: {average}")