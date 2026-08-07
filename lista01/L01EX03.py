print ("========================Lista de Exercícios 01============================")
print ("\n------------------------------Questão 03----------------------------------")
print ("\n\n\t Construa um algoritmo que solicite o nome de usuário e a senha. Se o nome de")
print ("\tusuário for igual a 'admin' e a senha for igual a '12345', exiba 'Login bem-sucedido'")
print ("\tCaso contrário, exiba 'Nome de usuário ou senha incorretos.")
print ("\n\n-----------------------------------------------------------------------------")

#recolho o nome de usuário
usuario= input ("\n\n\nPara entrar na conta insira seu nome de usuário:")

#recolho a senha do usuário
senha= input("Senha:")

#checo se o login e a senha estão certos
if usuario == "admin" and senha=="12345":
    print ("\n\n\nLogin bem-sucedido")
else:
    print ("Nome de usuário ou senha incorretos")