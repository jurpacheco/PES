print (f'==================================== lista de exercício 05 ====================================')
print(f'------------------------------------------- Questão 7 -------------------------------------------\n')
print ("Desenha moldura. Construa uma função que desenhe um retângulo usando os\ncaracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas,\nsendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se\nvalores fora da faixa forem informados, eles devem ser modificados para valores dentro\nda faixa de forma elegante.\n")
print(f'\n------------------------------------------------------------------------------------------------\n')

def create_rectangle(a, b):
    if 20>a>1 and 20>b>1:
        l=a-2
        print ("+", "-"*l, "+", sep="")
        i=0
        while i<b:
            i+=1
            print ("|", " "*l,"|",sep="" )
        print ("+", "-"*l, "+", sep="")
    else:
        print("Os valores adicionados nao podem ser usados")
        print ("+", "-"*5, "+", sep="")
        i=0
        while i<1:
            i+=1
            print ("|", "error","|", sep="")
        print ("+", "-"*5, "+", sep="")


width, high = input('Quanto de altura e quanto de largura? Usar o formato larguraxaltura: ').split("x")

width=int(width)
high=int(high)

print (create_rectangle(width, high))
