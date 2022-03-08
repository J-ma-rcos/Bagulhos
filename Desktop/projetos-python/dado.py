from random import randint


print("bem vindo ao 'dado' aqui sera gerado um numero aleatorio entre 1 e 6")

r1 = input('vamos jogar? yes(y) no(n)')

while r1 == "y" :
     print(randint(1,6))
     r1 = input("quer continuar? [Y/N]")
print(" fim do programa")

