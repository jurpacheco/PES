print ("==================================Lista de Exercícios 3======================================")
print ("\n---------------------------------------Questão 6-------------------------------------------")
print ( "\nImplemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome\ndo primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,\ndeve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o\nprograma deve exibir o nome de todos os bairros cadastrados na tela\n")
print ("\n\n------------------------------------------------------------------------------------------")

neighborhoods=["Centro"]
i=0
j=1
print ("\nVamos completar os cinco bairros de garopaba! Eu começo com Centro, quais os 4 que faltam?")

for i in range(4):
        neighborhood = input(f"Qual o bairro número {j+1}: ")
        #pego a resposta e coloco na lista de bairros
        neighborhoods.append(neighborhood)
        j+=1
        #limpei e formatei
        answerstring = ", ".join(neighborhoods).title()
 #resposta
print (f"Os 5 bairros de garopaba são: {answerstring}")
    
