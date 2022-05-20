from random import randint;
import random;

i=0;
u=0;
ppt=["pedra", "papel", "tesoura"];

#pergunta se quer jogar
r1 = input(str("vamos jogar pedra papel e tesoura\n"))

while (r1 == 'y' or 'n') :
    #receber a jogada do user
    if r1 == 'y': r2 = input(str(" qual sua jogada? \npedra| papel | tesoura \n")) 
    elif r1 == 'n' : quit();
#armazena pedra papel ou tesoura aleatorio
    pc=random.choice(ppt);
#comparar resultado
    if pc == r2 : print(" empate ")
    elif pc == 'pedra' and r2 == 'papel' : i = i + 1
    elif pc == 'papel' and r2 == 'tesoura' : i = i + 1
    elif pc == 'tesoura' and r2 == 'pedra' : i = i + 1
    else: u = u +1
#somar no placar
    print("placar \n pc: " , u , "voce: " , i)

    r1 = input(str("continuar a jogar?\n"))




