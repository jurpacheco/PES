print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 8----------------------------------")
print ("\n\n\n\t\tSuponha que você recebeu a última fatura do seu cartão de crédito no valor de R$ ")
print("\t1.000,00 e que você não possa pagá-la. Faça um programa que calcule sua dívida total ")
print(f"\tprograma. Considere que a taxa de juros mensal de um cartão de crédito é de 15,30% ao")
print("\tmês. A título de curiosidade, simule sua dívida final no prazo de 2 anos (24 meses).")
print("\n\n\n------------------------------------------------------------------------")

#Valor, taxa e meses
value= 1000
tax= 0.1530
i=1

#O total vai ser as taxas vezes a quantidade de meses vezes o valor. O +1 é para o 100%
while i<=24:
    value = value*(1+tax)
    i=i+1

print(f"O valor da fatura ao fim dos dois anos será de R${value:.2f}.")
