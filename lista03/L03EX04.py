cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    'fundo_vermelho': '\033[41m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    #{cores['NOME DA COR']}
    }
print ("==================================Lista de Exercícios 3======================================")
print ("\n---------------------------------------Questão 4-------------------------------------------")
print ("\n\n\t  Codifique um programa que funcionará como um cadastro de placas de automóveis de")
print ("\t um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma")
print ("\t lista. Seu programa deve ter um menu com a seguinte estrutura:")
print ("\n\t\t--------------\n\t\t1 – Cadastrar \n\t\t2 - Excluir\n\t\t3 - Listar\n\t\t0 - Sair\n\t\t--------------")
print ("\n\t A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se\n\thouver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço\n\tdisponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo\n\tnome da placa) e informar se houve sucesso ou falha. Já a opção listar deve\n\tsimplesmente listar todas as placas cadastradas. Dica: utilize um valor padrão para definir\n\tum espaço vago na lista.")
print ("\n\n------------------------------------------------------------------------------------------")

code = [-1]*15
i=0
j=0

while True:
 #Imprimo a tabela de opções
    print ("\n\t\t--------------\n\t\t1 – Cadastrar \n\t\t2 - Excluir\n\t\t3 - Listar\n\t\t0 - Sair\n\t\t--------------")
    #Então, recebo as possíveis opções 
#SAIR 
    answer= (int(input("- \ncoloque aqui: ")))
    if answer == 0:
        break 
#CADASTRAR
    elif answer == 1: 
        if i<10:
            code[i] = input(f"\n---------------------------\n\nCadastro {i+1}: ")
            if code[i] == '-1':
                print (f"\n\n{cores['fundo_vermelho']}Erro: Você não pode cadastrar -1:{cores['limpa']}")
                
            i+=1  
        else:
            print(f"{cores['fundo_vermelho']}Erro: A lista de placas já está cheia!{cores['limpa']}")
#EXCLUIR
    elif answer == 2 :
        plate = input("Informe qual a placa do carro a ser excluido: ")
        if plate in code:
            code.remove(plate)
            print (f"{cores['verde']}Exclusão da placa {plate} efetuada com sucesso!{cores['limpa']}")
        else:
            print(f"{cores['vermelho']}Erro: Placa não encontrada{cores['limpa']}")
#LISTAR
    elif answer == 3:
        if code[0] == '-1':
            print (f"A lista está vazia.\n----------------------------")
        else:
            for code1 in code:
                if code[j] != -1:
                    print (f"-------------------------\nO número da placa {j+1} é {code1}\n-------------------------")
                    j+=1