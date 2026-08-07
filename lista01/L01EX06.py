print ("========================Lista de Exercícios 01============================")
print ("\n------------------------------Questão 06----------------------------------")
print ("\t\t\n\n\nJogo do Pedra, Papel, Tesoura. Solicite as escolhas do jogador 1 e do jogador 2")
print("\t(“pedra”, “papel” ou “tesoura”). Use condicionais para determinar quem ganhou:")
print("\t• Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.”;")
print("\t• Exiba uma mensagem como “Jogador 1 venceu!” ou “Empate!”.")
print("\n\n\n---------------------------------------------------------------------------------")

# peço o jogador 1 para que ele escolha pedra, papel ou tesoura
print("\n\n\nVamos jogar pedra, papel ou tesoura com mais um amigo!")

player1, move1 = input("\n\n\tColoque seu nome e então, separado por um espaço a sua jogada.").split()

#Agora pego os dados do jogador 2

player2, move2 = input("\tJogador dois! coloque seu nome e então, separado por um espaço a sua jogada.").split()

#fiz isso aqui por fins esteticos na hora que estiver no terminal
player1 = player1.strip().upper()
player2 = player2.strip().upper()

#coloco toda resposta possivel de jogada em minusculo para não ter problemas de leitura depois.
move1= move1.lower().strip()
move2= move2.lower().strip()

#Faço os testes nas quais o jogador 1 ganha 
#estou usando ".startswith()" para poder captar o maior numero de respostas que possam ter sido digitadas erradas.

if move1.startswith("pe") and move2.startswith("t"):
    print(f"Pedra ganha de tesoura! {player1} você GANHOU!")

elif move1.startswith("t") and move2.startswith("pa"):
    print(f"Tesoura ganha de papel! {player1} você GANHOU!")

elif move1.startswith("pa") and move2.startswith("pe"):
    print(f"Papel ganha de pedra! {player1} você GANHOU!")

#Ocasioes na qual o jogador dois pode ganhar
elif move1.startswith("t") and move2.startswith("pe"):
    print(f"Pedra ganha de tesoura! {player2} você GANHOU!")

elif move1.startswith("pa") and move2.startswith("t"):
    print(f"Tesoura ganha de pedra! {player2} você GANHOU!")

elif move1.startswith("pe") and move2.startswith("pa"):
    print(f"Papel ganha de pedra! {player2} você GANHOU!")

#Casos de empate
elif move1.startswith("pe") and move2.startswith("pe"):
    print(f"Pedra e pedra!? {player1} e {player2} EMPATAM! Quanta sintonia.")

elif move1.startswith("t") and move2.startswith("t"):
    print(f"Tesoura e Tesoura!? {player1} e {player2} EMPATAM! Quanta sintonia.")

elif move1.startswith("pa") and move2.startswith("pa"):
    print(f"Papel e papel!? {player1} e {player2} EMPATAM! Quanta sintonia.")

#Caso não de certo:

else :
    print("Resposta inválida! tenha certeza que jogou certo.")
