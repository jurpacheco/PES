print ("========================Lista de Exercícios 01============================")
print ("\n------------------------------Questão 07----------------------------------")
print ("\t\t\n\n\nQual é o seu Signo? Solicite o dia e o mês de nascimento do usuário. Com base")
print("\t(nesses valores, use condicionais para determinar o signo.")
print("\n\n\n------------------------------------------------------------------------")

#Recolho o dia de nascimento do usuário.
day, month, year = map(int,input("\n\n\nInsira sua data de nascimento no modelo DMY (dd/mm/yyyy):").split("/"))

#agora vou testando as variaveis

#Janeiro
if month == 1 and 1 <= day <= 20:
    print (f"Ser de janeiro, você é de capricórnio!")

elif month == 1 and 21 <= day <= 31:
    print (f"Ser de janeiro, você é de Áquario!")

# Fevereiro
elif month == 2 and 1 <= day <= 18:
    print("Ser de fevereiro, você é de Áquario!")

elif month == 2 and 19 <= day <= 29:
    print("Ser de fevereiro, você é de Peixes!")

# Março
elif month == 3 and 1 <= day <= 19:
    print("Ser de Março, você é de Peixes!")

elif month == 3 and 20 <= day <= 31:
    print("Ser de Março, você é de Áries!")

# Abril
elif month == 4 and 1 <= day <= 20:
    print("Ser de Abril, você é de Áries!")

elif month == 4 and 21 <= day <= 30:
    print("Ser de Abril, você é de Touro!")

# Maio
elif month == 5 and 1 <= day <= 20:
    print("Ser de Maio, você é de Touro!")

elif month == 5 and 21 <= day <= 31:
    print("Ser de Maio, você é de Gêmeos!")

# Junho
elif month == 6 and 1 <= day <= 20:
    print("Ser de Junho, você é de Gêmeos!")

elif month == 6 and 21 <= day <= 30:
    print("Ser de Junho, você é de Câncer!")

# Julho
elif month == 7 and 1 <= day <= 21:
    print("Ser de Julho, você é de Câncer!")

elif month == 7 and 22 <= day <= 31:
    print("Ser de Julho, você é de Leão!")

# Agosto
elif month == 8 and 1 <= day <= 22:
    print("Ser de Agosto, você é de Leão!")

elif month == 8 and 23 <= day <= 31:
    print("Ser de Agosto, você é de Virgem!")

# Setembro
elif month == 9 and 1 <= day <= 22:
    print("Ser de Setembro, você é de Virgem!")

elif month == 9 and 23 <= day <= 30:
    print("Ser de Setembro, você é de Libra!")

# Outubro
elif month == 10 and 1 <= day <= 22:
    print("Ser de Outubro, você é de Libra!")

elif month == 10 and 23 <= day <= 31:
    print("Ser de Outubro, você é de Escorpião!")

# Novembro
elif month == 11 and 1 <= day <= 21:
    print("Ser de Novembro, você é de Escorpião!")

elif month == 11 and 22 <= day <= 30:
    print("Ser de Novembro, você é de Sagitário!")

# Dezembro
elif month == 12 and 1 <= day <= 21:
    print("Ser de Dezembro, você é de Sagitário!")

elif month == 12 and 22 <= day <= 31:
    print("Ser de Dezembro, você é de Capricórnio!")

#CASOS DE ERRO
else :
    print ("Acho que a data inserida é incompátivel!")