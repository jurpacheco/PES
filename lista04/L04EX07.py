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
print ("\n---------------------------------------Questão 7-------------------------------------------")
print ("\nUtilizando como base o exercício 6, implemente dois novos recursos: um para\ninformar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso\nnão existam notas cadastradas, seu programa deve informar “Erro: não há notas\ncadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu\nprograma:")
print ("\n\n------------------------------------------------------------------------------------------")

#variaveis
grades=[]
element=0
while True:
    print (f"{cores['magenta_claro']}\n\tNotas:{cores['limpa']}\n\t-----\n\n\t{cores['magenta_claro']}1{cores['limpa']} - Cadastrar\n\t{cores['magenta_claro']}2{cores['limpa']} - Excluir\n\t{cores['magenta_claro']}3{cores['limpa']} - Listar\n\t{cores['magenta_claro']}4 {cores['limpa']}- Calcular média\n\t{cores['magenta_claro']}5{cores['limpa']} – Mostrar {cores['negrito']}{cores['magenta_claro']}maior{cores['limpa']} nota\n\t{cores['magenta_claro']}6{cores['limpa']} – Mostrar {cores['negrito']}{cores['magenta_claro']}menor{cores['limpa']} nota\n\t{cores['vermelho']}0 - Sair{cores['limpa']}\n\n\t-----")
    answer=int(input("Opção: "))

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

    #VER A MAIOR NOTA         
    if answer == 5:
         if grades ==[]:
             print (f"\n{cores['vermelho']}As notas estão vazias!{cores['limpa']}\n")  
         else:
            highest=grades[0]
            for element in grades:
                if element>highest:
                    highest=element
            print (f"Sua maior nota é: {highest}")

    #VER A MENOR NOTA
    if answer == 6:
         if grades ==[]:
             print (f"\n{cores['vermelho']}As notas estão vazias!{cores['limpa']}\n")  
         else:
            lowest=grades[0]
            for element in grades:
                if element<lowest:
                    lowest=element
            print (f"Sua menor nota é: {lowest}")

