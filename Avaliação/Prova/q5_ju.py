from time import sleep
print ("-"*73)
print ("="*31, "Questão 5", "="*31)
print (f"faça um programa que exiba na tela a contagem iniciando no número 1 e indo\naté um número informado pelo usuário. Considere que a contagem pode ser \naté um número positivo ou até um número negativo")
print ("-"*73)

number= int(input("Até onde irá sua contagem: "))
i=0
if number >= 0:
    while i <= number:
        print (f"{i},")
        sleep (0.5)
        i=i+1
else:
    while number<=i:
        print (f"{i},")
        sleep (0.5)
        i=i-1

'''IREI FAZER A RECUPERAÇÃO JÁ QUE EU NÃO SOUBE FAZER ALGUMAS'''