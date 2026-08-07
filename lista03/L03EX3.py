cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    'fundo_vermelho': '\033[41m',
    #{cores['NOME DA COR']}
    }

print ("========================Lista de Exercícios 3============================")
print ("\n------------------------------Questão 3----------------------------------")
print ("\n\n\t Faça um programa que funcionará como um cadastro de códigos de produtos de umaa ")
print ("\t loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize")
print ("\t os elementos da lista com -1, este valor indicará que o elemento está vago para o")
print ("\t cadastro. Seu programa deve ter um menu com uma opção para cadastrar um novo")
print ("\t código (apenas um por vez) e para listar os todos códigos cadastrados (não devem ser")
print ("\t listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha")
print ("\t na hora de cadastrar um novo código e também não deve ser possível cadastrar um")
print ("\t produto com o código -1. No momento do cadastro, não deve ser informado o valor do")
print ("\t índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:")
print ("\n\n------------------------------------------------------------------------------------------")

code = [-1]*10
i=0
j=0

while True:
 #Imprimo a tabela de opções
    print ("\n\t\t--------------\n\t\t1 – Cadastrar \n\t\t2 - Listar\n\t\t0 - Sair\n\t\t--------------")
    #Então, recebo as possíveis opções 
    answer= (int(input("- \ncoloque aqui: ")))
#SAIR
    if answer == 0:
        break 
#CADASTRAR
    elif answer == 1: 
        if i<10:
            code[i] = int(input(f"\n---------------------------\n\nCadastro {i+1}: "))
            if code[i] == -1:
                print (f"\n\n{cores['fundo_vermelho']}Erro: Você não pode cadastrar -1:{cores['limpa']}")
                
            i+=1  
        else:
            print(f"{cores['fundo_vermelho']}Erro: A lista de cadastros já está cheia!{cores['limpa']}")
#LISTAR
    elif answer == 2:
        if code[0] == -1:
            print (f"A lista está vazia.\n----------------------------")
        else:
            for code1 in code:
                if code[j] != -1:
                    print (f"\n-------------------------\nO produto {j+1} tem o código {code1}\n-------------------------")
                    j+=1