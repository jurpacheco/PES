print ("==================================Lista de Exercícios 4======================================")
print ("\n---------------------------------------Questão 5-------------------------------------------")
print("\nCrie um programa que funcionará como um cadastro de Amigos Próximos no\nInstagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,\nconforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os\namigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.\nCrie um menu, conforme abaixo, para permitir a interação com o seu programa:\t\n\nAmigos Próximos\t\n---------------\t\n1 - Cadastrar\t\n2 - Excluir\t\n3 - Listar\t\n0 - Sair\t\n---------------")
print ("\n\n------------------------------------------------------------------------------------------")

#variaveis
cf=[]

while True:
    print("\t\n\nAmigos Próximos\t\n---------------\t\n1 - Cadastrar\t\n2 - Excluir\t\n3 - Listar\t\n0 - Sair\t\n---------------")

    answer=int(input("Digite o numero correspondente a sua acao: "))
    # SAIR
    if answer == 0:
      print ("Fechando seus amigos proximos...")
      break

    # CADASTRAR
    if answer == 1:
       print ("Otimo! Vamos adicionar um amigo ao Close friends:")
       friend=input("Digite o user do seu amigo:")
       cf.append(friend)
       print(f"{friend} adicionado ao seu Close Friends!")

    # EXCLUIR
    if answer == 2:
       print ("Excluiremos alguem do seu close friends")
       delet_friend= input("Qual o user de quem deve ser removido do close friends? ")
       if delet_friend in cf:
        cf.remove(delet_friend)
        print (f"{delet_friend} removido do seu Close friends")
       else:
          print("Este usuario nao esta no seu close friends!")

    # LISTAR
    if answer == 3:
       if len(cf)>0:
          print("\n\tClose friends")
          i=0
          for i in cf:
             print(f"• @{i}")  
       else: 
        print("Seu close friends esta vazio.")
    
    #Respostas erradas
    validoptions=[0, 1, 2, 3]
    if answer not in validoptions:
       print("Parece que sua resposta nao corresponde as opcoes de acoes! \n Tente novamente!")