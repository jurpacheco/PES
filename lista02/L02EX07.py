print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 7----------------------------------")
print ("\n\n\n\t\tImplemente um programa para calcular sua média final em uma determinada unidade")
print("\tcurricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada ")
print("\tuma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante ")
print("\testá Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6.")
print("\n\n\n------------------------------------------------------------------------")

#recolho a quantidade de notas que tiveram
amount = int(input("\nQual a quantidade de notas que você teve nesse semestre:"))

#Arrumo 
i=1
totalgrades=0
while i<=amount:
    grade=int(input(f"\n\nColoque a nota da sua avaliação {i}: "))
    totalgrades=totalgrades+grade #soma das notas
    i= i+1

average = totalgrades/amount

print (f"\nSua média foi {average:.1f}")
 
if average >= 6:
    print("\nVocê foi aprovado!")
else: 
    print ("\nVocê foi reprovado.")