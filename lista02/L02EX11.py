print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 11----------------------------------")
print ("\n\n\n\t\tFaça um programa para controlar o caixa de uma cantina. Seu programa deve")
print("\tsolicitar ao usuário o código do produto pedido e a quantidade comprada. Suponha que")
print("\tpara cada compra, apenas um tipo de produto possa ser comprado. O programa deve ser")
print("\tinterrompido caso o usuário digite 0. Para cada compra, seu programa deve exibir na tela")
print("\to nome do produto comprado e o valor total da compra. Ao final do programa, deve exibir")
print("\to valor total acumulado no caixa.")
print("\n\n\n------------------------------------------------------------------------")

#seto as variáveis
total_cash = 0.0

#Explico o que o código faz ao usuário
print ("Caixa da cantina")

#faço um laço que roda infinitamente
while True:
    code = int(input("\nDigite o código do produto (ou 0 para fechar o caixa): "))

#se a resposta for 0 o código para de rodar imediatamente
    if code == 0:
        break

    quantity = int(input("Digite a quantidade comprada: "))
    
    product_name = ""
    unit_price = 0.0

#verifico qual produto foi selecionado com base na tabela
    if code == 1:
        product_name = "Suco"
        unit_price = 6.00
    elif code == 2:
        product_name = "Pão de queijo"
        unit_price = 3.00
    elif code == 3:
        product_name = "Pastel"
        unit_price = 7.00
    elif code == 4:
        product_name = "Salada de frutas"
        unit_price = 9.00
    elif code == 5:
        product_name = "Café com leite"
        unit_price = 3.50
    elif code == 6:
        product_name = "Cappuccino"
        unit_price = 4.50
    elif code == 7:
        product_name = "Iogurte"
        unit_price = 6.50
    elif code == 8:
        product_name = "Água"
        unit_price = 2.50
    else:
        print("Código inválido! Tente novamente.")
        continue #faz o loop voltar para o início sem calcular nada inválido

#calculo o valor da compra atual e acumulo no caixa geral
    purchase_total = unit_price * quantity
    total_cash = total_cash + purchase_total

#exibo o resultado de cada compra logo após ela ser feita
    print(f"Produto comprado: {product_name} | Valor total da compra: R$ {purchase_total:.2f}")

#E então, somente quando há o break, a resposta final aparece

print(f"O valor total acumulado no caixa foi de: R$ {total_cash:.2f}")

