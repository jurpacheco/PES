from class_02 import Carro

carro_1= Carro("Honda", "Branco")
a = input("De qual cor o carro vai ser pintado?: ")
carro_1.pintar(a)
print (f" A nova cor é: {carro_1.cor}")
