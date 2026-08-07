
print ("==================================Lista de Exercícios 3======================================")
print ("\n---------------------------------------Questão 5-------------------------------------------")
print ("\n\n\t Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu\n\tprograma deve ter uma estrutura que seja capaz de armazenar as seguintes informações\n\tsobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve\n\tser através de um menu com as seguintes opções:")
print ("\n\t\t--------------\n\t\t1 – Cadastrar \n\t\t2 - Excluir\n\t\t3 - Alterar\n\t\t4 - Listar\n\t\t0 - Sair\n\t\t--------------")
print ("\n\tA opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção\n\texcluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve\n\tsolicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações\n\tda pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações\n\tdas pessoas cadastradas. ")
print ("\n\n------------------------------------------------------------------------------------------")
i = 0
names = [""]
ages =  [0]
heights = [0.0]
weights = [0.0]
cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    'fundo_vermelho': '\033[41m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    #{cores['NOME DA COR']}
    }
while True:
    # Imprimo a tabela de opções
    print ("\n\t\t--------------\n\t\t1 – Cadastrar \n\t\t2 - Excluir\n\t\t3 - Alterar\n\t\t4 - Listar\n\t\t0 - Sair\n\t\t--------------")
    
    # Então, recebo as possíveis opções 
    answer = int(input("- \ncoloque aqui: "))
    
    # SAIR
    if answer == 0:
        break 

    # CADASTRAR
    elif answer == 1: 
        # Se for o primeiro cadastro, preenchemos a posição 0
        if i == 0:
            names[0] = input("Para o cadastro, insira seu nome: ")
            ages[0] = int(input("Insira sua idade: "))
            heights[0] = float(input("Insira sua altura: "))
            weights[0] = float(input("Insira seu peso: "))
            i += 1
        else:
            # Para os próximos, aumentamos a lista adicionando um espaço vazio e preenchemos
            names += [""]
            ages += [0]
            heights += [0.0]
            weights += [0.0]
            
            names[i] = input("Para o cadastro, insira seu nome: ")
            ages[i] = int(input("Insira sua idade: "))
            heights[i] = float(input("Insira sua altura: "))
            weights[i] = float(input("Insira seu peso: "))
            i += 1
            
        print(f"{cores['verde']}Cadastro efetuado com sucesso!{cores['limpa']}")

    # EXCLUIR
    elif answer == 2:
        search = input("Digite o nome do cadastro que deve ser excluido: ")
        search = search.lower().strip()
        
        found = False
        
        # Varremos a lista de nomes usando o j para achar o índice
        for j in range(i):
            if names[j].lower().strip() == search:
                names[j] = ""
                ages[j] = 0
                heights[j] = 0.0
                weights[j] = 0.0
                found = True
                print (f"{cores['verde']}Exclusão do cadastro de {search} efetuada com sucesso!{cores['limpa']}")
                break      
        if not found:
            print (f"{cores['vermelho']}Erro: Cadastro não encontrado{cores['limpa']}")

    # ALTERAR
    elif answer == 3:
        search = input("Digite o nome do usuario que deve ter o dado alterado: ")
        search = search.lower().strip()
        
        found = False
        for j in range(i):
            if names[j].lower().strip() == search:
                found = True
                data_to_alter = input("Qual o dado a ser alterado?(Peso, Altura ou Idade): ")
                data_to_alter = data_to_alter.lower().strip()

                if data_to_alter.startswith("i"):
                    ages[j] = int(input("Altere sua idade: "))
                elif data_to_alter.startswith("a"):
                    heights[j] = float(input("Altere sua altura: "))
                elif data_to_alter.startswith("p"):
                    weights[j] = float(input("Altere seu peso: "))
                
                print (f"{cores['verde']}Alteração efetuada com sucesso!{cores['limpa']}")
                break
                
        if not found:
            print (f"{cores['vermelho']}Erro: Cadastro não encontrado{cores['limpa']}")

    # LISTAR
    elif answer == 4:
        if i == 0:
            print("A lista está vazia.\n----------------------------")
        else:
            for j in range(i):
                if names[j] != "":
                    print (f"-------------------------\nCadastro {j+1}: {names[j]}, {ages[j]} anos, {heights[j]}m, {weights[j]}kg.\n-------------------------")