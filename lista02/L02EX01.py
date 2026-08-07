cores= {'limpa': '\033[m',
        'rosa': '\033[95m',}

print (f"{cores['rosa']}========================Lista de Exercícios 2============================{cores['limpa']}")
print (f"{cores['rosa']}\n------------------------------Questão 01----------------------------------{cores['limpa']}")
print(f"{cores['rosa']}\n\n\n\tFaça um programa para exibir os números de 1 a 100.{cores['limpa']}")
print(f"{cores['rosa']}\n\n\n---------------------------------------------------------------------------{cores['limpa']}")

print ("A baixo será exibido os números de 1 à 100.")

#fazendo imprimir o 100
i = 1
while i<=100:
    print (f"• {i}")
    i=i+1

