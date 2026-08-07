print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 9----------------------------------")
print ("\n\n\n\t\tConsidere que você deseja fazer uma reserva mensal, em dinheiro, para a compra de")
print("\tum determinado presente para você mesmo(a). Considere que todo mês você depositará,")
print("\tem uma poupança no banco, um mesmo valor em reais. Faça um programa que leia o")
print("\tvalor que será depositado mensalmente e exiba na tela o valor acumulado mês a mês")
print(f"\tdurante 24 meses. Considere que a taxa de juros de uma poupança é 0,5% ao mês, que")
print("\ta poupança não possui nenhum saldo inicial.")
print("\n\n\n------------------------------------------------------------------------")

#peço o valor a ser depositado
deposit = input("Para sua reserva, insira o valor em reais do deposito mensal: ")

#caso o usuario escreva algo como "R$100,00"
deposit = deposit.replace("R$", "")
deposit= deposit.replace(",", ".")
deposit = float(deposit)

#determino as variáveis
tax=0.005
i=1
balance=0
#faço um laço que adiciona a taxa sobre o valor a cada mês
while i<=24:
    balance=balance*(1+tax)
    balance=balance+deposit

    i=i+1

print (f"O valor ao fim dos 24 meses é de: R${balance:.2f}")