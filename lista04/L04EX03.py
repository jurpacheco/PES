print ("==================================Lista de Exercícios 4======================================")
print ("\n---------------------------------------Questão 3-------------------------------------------")
print("\nUtilizando como base o exercício anterior, faça com seu programa exiba uma saída\nformatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você\ndeve fazer isso de duas formas: com while e com for.\nExibição com while:\n\n-------------------\nNota: 9.0\nNota: 7.5\nNota: 8.0\nExibição com for:\nNota: 9.0\nNota: 7.5\nNota: 8.0\n-------------------")
print ("\n\n------------------------------------------------------------------------------------------")

#COM FOR
grades =[]
i=0
answer=0
index=0
answer= int(input("\n Quantas notas devem ser exibidas?: "))

for i in range(answer):
    grade=(input(f"Agora coloque a nota que você tirou na prova {i+1}: "))
    grades.append(grade)
print (f"\n--------------\n Exibição com for:")
for i in grades:
    print (f"Nota:{grades[index]}")
    index+=1
print ("--------------")

#COM WHILE
grades1 =[]
i=0
answer1=0
index=0

answer1= int(input("\n Quantas notas devem ser exibidas?: "))
while len(grades1) < answer1:
    grade1=(input(f"Agora coloque a nota que você tirou na prova {i+1}: "))
    grades1.append(grade1)
    i+=1
print (f"\n--------------\n Exibição com while:")
for j in grades1:
    print (f"Nota:{grades1[index]}")
    index+=1
print ("--------------")