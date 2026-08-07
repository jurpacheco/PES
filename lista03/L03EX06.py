cores = {
    # Reseta a cor para o padrão do sistema (OBRIGATÓRIO usar no final)
    'limpa': '\033[m',
    'fundo_vermelho': '\033[41m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    #{cores['NOME DA COR']}
    }
print ("==================================Lista de Exercícios 3======================================")
print ("\n---------------------------------------Questão 6-------------------------------------------")
print ("\n\n\tAdicione ao programa da questão anterior, uma opção para excluir o cadastro\n\tbaseado no código da pessoa. Adicione também uma opção para pesquisar que utilizará\n\to nome da pessoa como critério de busca.")
print ("\n\n------------------------------------------------------------------------------------------")
i = 0
names = [""]
ages = [0]
heights = [0.0]
weights = [0.0]

while True:
    print("\n\t\t--------------")
    print("\t\t1 – Cadastrar")
    print("\t\t2 - Excluir por Código")
    print("\t\t3 - Alterar")
    print("\t\t4 - Listar Todos")
    print("\t\t5 - Pesquisar por Nome")
    print("\t\t0 - Sair")
    print("\t\t--------------")
    
    answer = int(input("- \ncoloque aqui: "))
    
    # SAIR
    if answer == 0:
        break
        
    # CADASTRAR
    elif answer == 1:
        if i == 0:
            names[0] = input("Para o cadastro, insira seu nome: ")
            ages[0] = int(input("Insira sua idade: "))
            heights[0] = float(input("Insira sua altura: "))
            weights[0] = float(input("Insira seu peso: "))
            i += 1
        else:
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
        
    # EXCLUIR POR CÓDIGO (ID)
    elif answer == 2:
        code = int(input("Digite o código (número do cadastro) que deseja excluir: "))
        search_index = code - 1 
        
        if 0 <= search_index < i and names[search_index] != "":
            print(f"{cores['verde']}Exclusão do cadastro de {names[search_index]} efetuada com sucesso!{cores['limpa']}")
            names[search_index] = ""
            ages[search_index] = 0
            heights[search_index] = 0.0
            weights[search_index] = 0.0
        else:
            print(f"{cores['vermelho']}Erro: Código de cadastro inválido ou já excluído.{cores['limpa']}")
            
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
                print(f"{cores['verde']}Alteração efetuada com sucesso!{cores['limpa']}")
                break
        if not found:
            print(f"{cores['vermelho']}Erro: Cadastro não encontrado{cores['limpa']}")
            
    # LISTAR TODOS
    elif answer == 4:
        active_registrations = any(nome != "" for nome in names[:i])
        if i == 0 or not active_registrations:
            print("A lista está vazia.\n----------------------------")
        else:
            for j in range(i):
                if names[j] != "":
                    print(f"-------------------------\nCódigo {j+1}: {names[j]}, {ages[j]} anos, {heights[j]}m, {weights[j]}kg.\n-------------------------")
                    
    # PESQUISAR POR NOME
    elif answer == 5:
        search = input("Digite o nome que deseja pesquisar: ")
        search = search.lower().strip()
        found = False
        for j in range(i):
            if names[j].lower().strip() == search:
                print(f"{cores['verde']}\nCadastro Encontrado!{cores['limpa']}")
                print(f"Código {j+1}: {names[j]}, {ages[j]} anos, {heights[j]}m, {weights[j]}kg.")
                found = True
                break
        if not found:
             print(f"{cores['vermelho']}Erro: Nome não encontrado na base de dados.{cores['limpa']}")