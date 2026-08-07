print ("========================Lista de Exercícios 01============================")
print ("\n------------------------------Questão 05----------------------------------")
print ("\t\t\n\n\nDeterminador de Temperatura: Solicite a temperatura do dia (em ºC). Dependendo da")
print("\ttemperatura informada, exiba a mensagem apropriada conforme abaixo:")
print("\t• Menos de 10 ºC: “Está muito frio! Use roupas quentes.”;")
print("\t• De 10 ºC até 20 ºC (inclusive): “Frio. Vista-se bem!”;")
print("\t• Acima de 20 ºC até 25 ºC (inclusive): “Temperatura agradável.”;")
print("\t• Acima de 25 ºC até 30 ºC (inclusive): “Está ficando quente!”;")
print("\t• Acima de 30 ºC: “Está muito quente! Fique hidratado.”.")
print("\tObs.: o algoritmo deve aceitar temperaturas com valores decimais (ex.: 20,5 ºC, 25,8 ºC,")
print("\tetc...)")
print("\n\n\n---------------------------------------------------------------------------------")

#recolhendo o valor da varivael de temperatura
degree= float(input("\n\n\nQual a tempertura do dia e hoje no local em que você mora? Digite aqui o valor em graus celcius:"))

if degree < 10:
    print("Está muito frio! Use roupas quentes.")

elif degree <= 20:
    print ("Frio. Vista-se bem!")

elif degree <= 25:
    print ("Temperatura agradável.")

elif degree <= 30:
    print ("Está ficando quente!")

elif degree > 31 :
    print ("Está muito quente! Fique hidratado.")
