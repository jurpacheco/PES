#U07EX07.py
print("--------------------------------------------------------------------------------")
print("\n\t=========================U07EX07.py===========================")
print("\n\t Implemente um algoritmo que leia a idade de uma pessoa")
print("\te diga quantos dias essa pessoa já viveu.")
print("\tConsidere que um ano tem 365 dias.")
print("--------------------------------------------------------------------------------")

#Variaveis
ano_atual=2026

#recolhendo a idade do usuário
ano_nasc= int(input("\n\n\tQuer saber quantos dias você tem de vida? insira o ano que nasceu: "))

#idade da pessoa
idade2=ano_atual-ano_nasc

#dias que passaram desde o ano de nascimento
dias_anual=idade2*365

print("\n\t\tDesde", ano_nasc, "se passaram", dias_anual, "dias, mas ainda não temos um numero tão aproximado...")

#recolhendo quantes meses desde o aniversário
meses = int(input("\n\n\tQuer saber melhor? Insira quantos meses fazem que você fez aniversário: "))

#quantos dias se passaram desde o último aniversário
dias_mes = meses*30

#quantos dias no aproximadamente essa pessoa tem de vida?
total_de_dias= dias_mes+dias_anual

print ("\n\t\tVocê tem aproximadamente", total_de_dias, "dias de vida! Tá velho(a) hein?!")
