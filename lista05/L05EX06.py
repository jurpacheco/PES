print (f'==================================== lista de exercício 05 ====================================')
print(f'------------------------------------------- Questão 6 -------------------------------------------\n')
print ("6 - Crie uma função chamada tempo_total que receba a quantidade de horas e minutos\nque um jovem passou jogando videogame e retorne o total de minutos jogados. Peça ao\nusuário para inserir as horas e minutos, e exiba o tempo total em minutos.\n")
print(f'\n------------------------------------------------------------------------------------------------\n')
def total_time(a,b):
    h_to_minute=a*60
    total=h_to_minute+b
    return total

hr, min= (input("Quanto tempo o rapaz passou jogando? Exemplo: 1h30!")).split('h')
hour=int(hr)
minute=int(min)


total_minutes= total_time(hour, minute)

print(f'O tempo total de jogatina do rapaz foi de {total_minutes} minutos')