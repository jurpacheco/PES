print ("==================================Lista de Exercícios 4======================================")
print ("\n---------------------------------------Questão 2-------------------------------------------")
print("\nCrie um programa que registrará as notas de um estudante. O programa deve\nperguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das\nnotas e, ao final, exibir todas as notas digitadas na tela.\n")
print ("\n\n------------------------------------------------------------------------------------------")

'''Crie um programa que registrará as notas de um estudante. O programa deve
perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
notas e, ao final, exibir todas as notas digitadas na tela.'''

grades =[]
i=0
answer=0

answer= int(input("\n Quantas notas devem ser exibidas?: "))

for i in range(answer):
    grade=(input(f"Agora coloque a nota que você tirou na prova {i+1}: "))
    grades.append(grade)
    
#grades=", ".join(grades)
print (f"Notas : {grades}")