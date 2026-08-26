 https://github.com/jurpacheco/PES.git
def total_time(a,b):
    h_to_minute=a*60
    total=h_to_minute+b
    return total

hr, min= (input("Quanto tempo o rapaz passou jogando? Exemplo: 1h30!")).split('h')
hour=int(hr)
minute=int(min)


total_minutes= total_time(hour, minute)

print(f'O tempo total de jogatina do rapaz foi de {total_minutes} minutos')