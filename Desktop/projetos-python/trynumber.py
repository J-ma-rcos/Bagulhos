#objetivo: programa que gera numero aleatorio e o usuario tem que "adivinhar" o numero 

from random import randint

print( " bem vindo ao TENTE ACERTAR O NUMERO ")

V1 = randint(1,10) 

print(" deseja jogar? Y/N")

V2 = input()

if V2 == 'y' : v3 = int(input('digite o numero que vc acha que foi sorteado'))
elif V2 == 'n' : quit()
else: print(" resposta invalida ")

while(v3 != V1) : v3 = int(input(' voce errou, tente novamente '))

if v3 == V1 : print(' voce acertou no numero era : ' , V1)