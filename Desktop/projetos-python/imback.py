# calculadora#
 
print("bem vindo a calculadora, digite os valores")

valor1 = int(input('digite um numero:'))
valor2 = int(input('digite um numero:'))

soma = valor1 + valor2
divisao = valor1/valor2
multi = valor1*valor2
subt = valor1 - valor2

r1 = input('qual operação deseja relizar? digite o simbolo da operação sendo +(soma)_-(subtração)_*(multiplicação)_/(divisão)')
if r1 == "+" : print(soma)
elif r1 == "-" :print(subt)
elif r1 == "*": print(multi)
elif r1 == "/": print(divisao)
else : print("operação invalida")


