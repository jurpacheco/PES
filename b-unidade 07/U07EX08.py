#U07EX08.py
print("--------------------------------------------------------------------------------")
print("\n\t=========================U07EX08.py===========================")
print("\n\t  Implemente um algoritmo que leia a quantidade")
print("\tde partidas de um campeonato de futebol e indique a")
print("\tquantidade de minutos total (de todas as partidas juntas).")
print("\tConsidere que cada partida terá sempre o mesmo tempo.")
print("\tComente seu algoritmo.")
print("--------------------------------------------------------------------------------")

#recolhendo quantas partidas tem o campeonato
partidas= int(input("\n\n\tQuantas partidas tiveram este campeonato? Insira Aqui: "))

#recolhendo quantos minutos tem as partidas
tempo= int(input("\te quantos minutos as partidas tem de duração? "))

#fazendo o cálculo de quanto tempo tiveram as partidas no total
tempo_minuto=partidas*tempo

horas= tempo_minuto//60
minutos= tempo_minuto%60

print ("\n\t\tA duração total do campeonato foi de", tempo_minuto, "em minutos. Totalizando assim,", horas, "horas e", minutos, "minutos")
