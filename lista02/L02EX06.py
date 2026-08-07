print ("========================Lista de Exercícios 2============================")
print ("\n------------------------------Questão 6----------------------------------")
print ("\n\n\n\t\tModifique o programa anterior de forma que o usuário também digite o início e o fim da")
print("\ttabuada, em vez de começar iniciar no 1 e terminar no 10.")
print("\n\n\n------------------------------------------------------------------------")


#vejo de qual tabuada o usuario quer saber
number, number2, number3= input("De qual número você quer saber a tabuada e em qual numero queres que comece e termine:").split()

#Transformo as variaveis que eram string, em integer
number = int(number)
number2= int(number2)
number3= int(number3)

#faço isso para ter certeza que vai começar no numero que o usuario escolher começar
number2=number2-1

#escrevo o título
print (f"\t\nTabuada do {number}")

#Enquanto numero que começa < que numero que termina
while number2<number3:
#Faz numero que começa + 1
    number2=number2+1
#Defino o resultado
    result=number*number2
    
#coloco o resultado 
    print (f"{number} x {number2} = {result}")
