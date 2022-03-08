#calculadora de imposto sobre salario 

from ast import Pass
from cmath import nan
from contextlib import nullcontext


print("bem vindo a calculadora de impostos sobre salario")

salario = float(input('digite o valor do seu salario: '))

if(salario <= 1900): ir = 1
elif(salario >= 1900 and salario < 2826): ir = 0.075
elif(salario >= 2826 and salario < 3751): ir = 0.15
elif(salario >= 3751 and salario < 4664): ir = 0.225
else : ir = 0.275

if(salario < 1045): inss = 1
elif(salario >= 1045 and salario < 2089): inss = 0.075
elif(salario >= 2089 and salario < 3134): inss = 0.09
elif(salario >= 3134 and salario < 6101): inss = 0.12
else : inss = 0.141

tax = inss + ir
if(tax == 2): nsalario = salario
print("seu salario liquido é de {}" .format(nsalario))