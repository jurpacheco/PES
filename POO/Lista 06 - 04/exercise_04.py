from class_04 import Produto
produto= Produto()
produto.nome = input('Nome do produto: ')
produto.quantidade = input ('Quantidade de produto: ')

if produto.esta_disponivel():
    print (f"{produto.nome} está disponível. ")
else:
    print (f"{produto.nome} não está disponível. ")

compra = input('COnfirmar compra (s/n): ')
if compra.lower() == 's':
    produto.vender()
else:
    print (f"{produto.quantidade}")
