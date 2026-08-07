print ("========================Lista de Exercícios 01============================")
print ("\n------------------------------Questão 01----------------------------------")
print("\n\n\n\tSolicite o valor total de uma compra. Se o valor for maior ou igual a 100, exiba")
print("\t'Você ganhou um cupom de desconto!'.")
print("\tCaso contrário, exiba 'Continue comprando para ganhar um cupom de desconto!'.")
print("\n\n\n---------------------------------------------------------------------------")


#Peço que o cliente informe o valor total da compra feita
valor= float(input("\n\n\n\tinsira o valor da compra efetuada:"))

#Informo que se o valor for maior que 100 há desconto
if valor >=  100:
    print ("Ao gastar", valor, "você recebeu um cupom de desconto!")

else: 
#Eu quis mostrar quanto faltava pro cliente conseguir o cupom, entao fiz o valor total menos 100
    valor_falta= 100-valor

#exibo o print do else.
#eu percebi que o resultado do valor que faltava pra conseguir
#o cupom ficava muito extenso, pesquisei e vi como usa a f-string
    print (f"Você gastou R$ {valor:.2f} falta somente R$ {valor_falta:.2f} para ganhar o desconto. Continue comprando para receber seu cupom!")
