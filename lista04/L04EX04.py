print ("==================================Lista de Exercícios 4======================================")
print ("\n---------------------------------------Questão 4-------------------------------------------")
print(f"\nFaça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser\ncadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado\nna tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a\nremoção dela e imprima a lista novamente.")
print ("\n\n------------------------------------------------------------------------------------------")

cities=[]
index=0
element=0

amountcity=int(input("Quantas cidades devem ser cadastradas?"))

while len(cities)<amountcity:
    city=input("Cadastre a cidade:")
    city=city.lower().strip()
    cities.append(city)

for element in cities:
    print (f"•{element.title()}")
    index+=1

print("Agora, vamos excluir uma cidade da lista")
city_delet=input("digite aqui:")
city_delet.lower().strip()

if city_delet in cities:
    cities.remove(city_delet)
else:
    ("Essa cidade nao esta na lista!")

index=0
element=0
for element in cities:
    print (f"•{element.title()}")
    index+=1