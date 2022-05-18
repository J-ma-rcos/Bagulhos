from random import randint

a = str("seu numero e : ")

#apresentação
print("bem vindo ao 'dado' aqui sera gerado um numero aleatorio entre 1 e 6\n")
#pergunta se quer jogar
r1 = input('vamos jogar? yes(y) no(n)\n')

while r1 == "y" :
     print( 'seu numero e :',randint(1,6))
     r1 = input("quer continuar? [Y/N]")
print(" fim do programa")

