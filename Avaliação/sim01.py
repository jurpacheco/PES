print('='*25, 'Simulação de Prova', '='*25)
print('-'*25, 'Exercício 1', '-'*25)
print("Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando\né divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.\n")
print('='*50)

''''1 – Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando
é divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.'''


def is_leap(a):
    div_4=a%4
    div_400=a%400
    div_100=a%100
    if div_4==0 or div_400 == 0 and div_100 != 0:
        print ("O ano é bissexto!")
    else:
        print ("O ano não é bissexto")


year= int(input(f'Coloque o ano que você deseja saber se é bissexto: \n'))
is_leap(year)