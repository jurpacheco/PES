print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 12----------------------------------")
print ("\n\n\n\t\tImplemente um programa que funcione como uma calculadora entre dois números")
print("\tinformados. Seu programa deve exibir um menu que solicite a operação a ser realizada")
print("\tentre dois números (adição, subtração, divisão e multiplicação) e os dois números a")
print("\tserem utilizados no cálculo. Se o usuário digitar uma opção inválida, deve alertar o")
print("\tusuário e exibir o menu novamente.")
print("\n\n\n------------------------------------------------------------------------")

#seto as variáveis
result = 0.0

#faço um laço que roda infinitamente
while True:
    #Exibo o menu conforme solicitado pelo enunciado
    print("\nMenu")
    print("------")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("0 - Sair")
    
    option = int(input("Digite a opção: "))

#se a resposta for 0 o código para de rodar imediatamente
    if option == 0:
        break

#verifico se a opção é inválida antes de pedir os números
    if option < 1 or option > 4:
        print("\n[ALERT] Opção inválida! Escolha uma opção do menu.")
        continue #faz o loop voltar para o início e mostrar o menu novamente

#solicito os dois números para o cálculo
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

#verifico qual operação foi selecionada e realizo o cálculo
    if option == 1:
        result = num1 + num2
        print(f"\nResultado da Adição: {num1} + {num2} = {result}")
    elif option == 2:
        result = num1 - num2
        print(f"\nResultado da Subtração: {num1} - {num2} = {result}")
    elif option == 3:
        #valido se o segundo número é zero para evitar erro de divisão por zero
        if num2 == 0:
            print("\n[Erro] Não é possível dividir por zero!")
        else:
            result = num1 / num2
            print(f"\nResultado da Divisão: {num1} / {num2} = {result}")
    elif option == 4:
        result = num1 * num2
        print(f"\nResultado da Multiplicação: {num1} * {num2} = {result}")

#E então, somente quando há o break, a resposta final aparece

print("4Obrigado por usar a calculadora!")

