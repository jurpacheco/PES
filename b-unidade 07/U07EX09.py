print("\n\t=========================U07EX09.py===========================")
print("\n\tImplemente um algoritmo que solicite ao usuário a")
print("\tquantidade de salgados consumidos na cantina e o valor do")
print ("\tsalgado (considere que todos possuem o mesmo preço). ")
print("\tLembre-se que o preço é um número de ponto flutuante e não")
print("\tum inteiro. Em seguida, exiba o valor total da compra.")

#solicitar ao usuário a quantidade e o preço dos salgados, float
quant_salgado= float(input("\n\n\t\tVocê cuida do seu dinheiro? sabe quanto gastou na cantina até hoje? Insira quantos salgados você já comprou lá:"))
valor_salgado= float(input("\n\n\t\t Agora coloque o valor do salgado da cantina!"))

total_gasto= quant_salgado*valor_salgado

print ("\n\tVocê já gastou R$",total_gasto,". Quanto dinheiro né? Cuide melhor do seu bolso!")