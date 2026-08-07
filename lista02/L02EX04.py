print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 4----------------------------------")
print ("\n\n\n\t\tImplemente um algoritmo que exiba na tela os números pares de 0 até um número")
print("\tdigitado pelo usuário. Dica: você pode utilizar o operador módulo (%) ou contar de 2 em 2.")
print("\n\n\n------------------------------------------------------------------------")

# recebo o número que o usuário escolhe
number=int(input("para os múltiplos de dois, coloque um numero na qual você deseja que seja o último:"))

#uso o range para formar isso
for number in range (0, number+1, 2):
        print(f"• {number}")