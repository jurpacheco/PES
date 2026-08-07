cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    # Estilos de Texto
    'negrito': '\033[1m',
    # Cores Padrão (Texto)
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'magenta_claro': '\033[95m',

    # Cores de Fundo (Background)
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
     #{cores['NOME DA COR']}
}


print ("==================================Lista de Exercícios 4======================================")
print ("\n---------------------------------------Questão 6-------------------------------------------")
print ("\n Elabore um programa que funcionará como um cadastro notas de um estudante. Seu\nprograma deve permitir que notas sejam cadastradas ou removidas (através do seu\níndice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também\ndeve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve\navisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para\ncalcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6\ne reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação\ncom o seu programa:\n\n\t\tNotas\n\t\t-----\n\t\t1 - Cadastrar\n\t\t2 - Excluir\n\t\t3 - Listar\n\t\t4 - Calcular média\n\t\t0 - Sair\n\t\t-----\n\t\tOpção:")
print ("\n\n------------------------------------------------------------------------------------------")

#variaveis
grades=[]
element=0
while True:
    print("\n\n\t\tNotas\n\t\t-----\n\t\t1 - Cadastrar\n\t\t2 - Excluir\n\t\t3 - Listar\n\t\t4 - Calcular média\n\t\t0 - Sair\n\t\t-----\n\t\tOpção:")
    answer=int(input(""))

    #SAIR
    if answer==0:
        print (f"{cores['magenta_claro']}Fechando o Programa...{cores['limpa']}")
        break

    #CADASTRAR
    if answer == 1:
        print ("\n Vamos cadastrar sua nota!")
        grade= float(input(f"Digite sua nota {len(grades)+1}:"))
        grades.append(grade)
        print (f"\n{cores['verde']}Nota cadastrada com sucesso!{cores['limpa']}\n")
        

    #EXCLUIR
    if answer == 2:
        print ("Qual a nota que voce deseja excluir?")
        grade_delete=int(input(f"A nota que você quer excluir, foi qual nota a ser cadastrada? (1, 2...)"))
        grade_delete=grade_delete-1
        if 0 <= grade_delete < len(grades):
            grades.pop(grade_delete)
            print (f"\n{cores['verde']}Nota excluída com sucesso!{cores['limpa']}\n")
        else:
           (f"\n{cores['vermelho']}Este indice é invalido!{cores['limpa']}\n") 

    #LISTAR
    if answer == 3:
        if grades == []:
            print (f"\n{cores['vermelho']}As notas estão vazias!{cores['limpa']}\n")
        else: 
            print (f"\n\t{cores['magenta_claro']}Suas notas cadastradas:{cores['limpa']}\n")
            i=0
            for element in grades:
                print (f"\tNota {i+1}: {element}")
                i+=1
    
    #MÉDIA
    if answer == 4:
        if grades == []:
          print (f"\n{cores['vermelho']}As notas estão vazias!{cores['limpa']}\n")  
        else:
            amount=len(grades) 
            sum=0
            for element in grades:
                sum = element+sum
            average = sum/amount
            print (f"\n\t{cores['magenta_claro']}A média do aluno é de: {average:.2}{cores['limpa']}\n")
            if average < 6:
                print (f"\nSituação: {cores['vermelho']}Reprovado!{cores['limpa']}\n")
            else:
                print (f"\nSituação: {cores['verde']}Aprovado!{cores['limpa']}\n")

    