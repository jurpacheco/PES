print ("-"*51)
print ("="*20, "Questão 1", "="*20)
print (f"Construa um algoritmo que solicite o nome de usuário\ne a senha. Se o nome de usuário for igual\n'admin' e a senha for igual a '12345' exiba\n'Login bem sucedido'. Caso contrário exiba 'Nome de \nusuário ou senha incorretos'.")
print ("-"*51)

user_name=input("Para entrar na conta, insira o seu username: ")
password=input("Insira a sua senha: ")

if user_name == 'admin' and password == '12345':
    print ("Login bem-sucedido.")
else:
    print("Nome de usuário ou senha incorretos.")