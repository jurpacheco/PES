from time import sleep
print (f'==================================== lista de exercício 05 ====================================')
print(f'------------------------------------------- Questão 8 -------------------------------------------\n')
print ("8 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.\nPor exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada no formato\nde string, por exemplo: “15:31”. Deve haver pelo menos duas funções: uma para fazer a\nconversão e uma para imprimir a saída. A função que faz a conversão deve ter duas\nsaídas: uma com a hora convertida e outra com “A”, caso seja “A.M.” e “P”, caso seja\n“P.M.”. Inclua um loop que permita que o usuário repita esse cálculo para novos valores\nde entrada todas as vezes que desejar.\n")
print(f'\n------------------------------------------------------------------------------------------------\n')



def convert_12h(a, b):
    if a > 12:
        a=a-12
        period="P"
    else:  
        period="A"
    return (f"{a}:{b} {period}.M")
while True:
    time = input(f"Coloque o horario, sair para sair (formato 00:00)\n")
    time_clean = time.strip()
    time_lower = time_clean.lower()
    if time_lower.startswith("s"):
        print("Saindo...")
        sleep(1)
        break 
    hour, minute=time.split(":")
    hour=int(hour)
    print(convert_12h(hour, minute))
