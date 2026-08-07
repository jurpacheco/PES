print ("==============U07EX10.py================")
print (" \n\tImplemente um algoritmo que solicite ao usuário a") 
print ("\tquantidade de salgados consumidos na cantina e o valor do")
print ("\tsalgado (considere que todos possuem o mesmo preço). Solicite") 
print ("\ttambém ao usuário a quantidade de sucos consumida e o valor") 
print ("\tdo suco (considere, também, que todos possuem o mesmo") 
print ("\tpreço). Em seguida, exiba o valor total da compra")

#solicitar ao usuário a quantidade e o preço dos salgados, float
quant_salgado= float(input("\n\n\t\tVocê cuida do seu dinheiro? sabe quanto gastou na cantina até hoje? Insira quantos salgados você já comprou lá:"))
valor_salgado= float(input("\n\n\t\t Agora coloque o valor do salgado da cantina!"))

#solicitar ao usuário a quantidade e o preço dos salgados, float
quant_suco= float(input("\n\n\t\t Os sucos tambem contam, sabia? Quantos você já comprou?"))
valor_suco= float(input("\n\n\t\t Agora coloque o valor do suco que voce tanto compra:"))

#Conta que calcula o valor gasto na cantina.
total_gasto= quant_salgado*valor_salgado+quant_suco*valor_suco

print ("\n\tVocê já gastou R$",total_gasto,". Quanto dinheiro né? Cuide melhor do seu bolso!")