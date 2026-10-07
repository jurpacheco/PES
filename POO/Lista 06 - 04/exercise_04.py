from class_04 import Produto
n = input('Nome do produto: ')
q = int(input('Quantidade de produto: '))
produto= Produto(n, q)

if produto.esta_disponivel():
    print (f"{produto.nome} está disponível. ")
else:
    print (f"{produto.nome} não está disponível. ")

compra = input('Confirmar compra (s/n): ')
if compra.lower() == 's':
    produto.vender()
else:
    print (f"{produto.quantidade}")
