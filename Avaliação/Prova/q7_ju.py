print ("-"*73)
print ("="*31, "Questão 7", "="*31)
print (f"codifique um programa que funcionará como um cadastro de placas de\nauttomóveis de um estacionamento (sem limite de automóveis). o cadastro deve ser\nrealizado em uma lista. Seu programa deve ter um menu com a seguinte estrutura:\n")
print ("-"*29)
print ("!\t1 - Cadastrar       !\n!\t2 - Excluir         !\n!\t3 - Listar          !\n!\t4 - Sair            !")
print ("-"*29)
print ("")
print ("-"*73)


print (f"\n\nDigite abaixo qual a opção você deseja utilizar.")
print ("-"*29)
print ("!\t1 - Cadastrar       !\n!\t2 - Excluir         !\n!\t3 - Listar          !\n!\t0 - Sair            !")
print ("-"*29)

plates= []

while True:

    option = int(input(f"\n↪ "))


    if option == 0:
        break

    elif option == 1:
        print (f"\n Coloque abaixo a placa do carro que você deseja cadastrar")
        plate = input("↪ ")
        if plate in plates:
            print("Esta placa já foi cadastrada!")
        else:
            plates.append(plate)
            print (f"Cadastro concluido com sucesso!")
    elif option == 2:
        print (f"\n Coloque abaixo a placa do carro que você deseja excluir do banco de dados")
        plate_delete = input("↪ ")
        if plate_delete in plates:
            plates.remove(plate)
            print ("Exclusão concluida com êxito! ")
        else:
            print ("Essa placa não existe nos cadastros.")
    elif option == 3:
        print (f"\n Placas registradas:")
        for k, i in enumerate(plates, start=1):
            print (f"{k} - {i}")
    else:
        print ("A opção selecionada não existe, tente novamente.")