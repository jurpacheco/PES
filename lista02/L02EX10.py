print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 10----------------------------------")
print ("\n\n\n\t\tEscreva um programa que leia números inteiros do teclado. O programa deve ler os")
print("\tnúmeros até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de")
print("\tnúmeros digitados, assim como a soma e a média aritmética.")
print("\n\n\n------------------------------------------------------------------------")

#seto as variáveis
sum = 0
average = 0
numbers = 0

#Explico o que o código faz ao usuário
print ("Coloque os números inteiros que queres saber a soma e a média aritmética. Digite 0 para parar: ")

#faço um laço que roda infinitamente
while True:
    answer = int(input("\n\n* digite: "))

#se a resposta for 0 o código para de rodar imediatamente
    if answer == 0:
        break

#se não, ve a quantidade de números digitados, a soma e a média aritmética
    numbers = numbers + 1
    sum = sum + answer
    average = sum / numbers

#E então, somente quando há o break, a resposta aparece
print(f"Você somou {numbers} números, o resultado da soma foi {sum}, e sua média é de {average}.")