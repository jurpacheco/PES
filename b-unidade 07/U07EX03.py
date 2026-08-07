print("\n\n\n\t=========================U07EX03.py===========================")
print("\n\tImplemente um algoritmo em Python que calcule a quantidade de minutos de 4 aulas e exiba o resultado na tela, sabendo-se que cada aula tem 55 minutos.")
#Quantidade de aulas
aulas=4

#Minutos por aula
minutos_aula=55

#Cálculo para saber quantos minutos tem 4 aulas
total_minutos=minutos_aula*aulas
print("\n\n\t\tO total de minutos nessas 4 aulas foi de", total_minutos, "minutos")

#A partir daqui, fiz porque quis e fiz a conta de horas e minutos dessas 4 aulas
#horas
horas=total_minutos//60
#minutos
minutos_restantes=total_minutos%60

print("\n\n\t\tMas qual foi a duração em horas dessas aulas? foi de", horas, "horas e", minutos_restantes, "minutos.")

