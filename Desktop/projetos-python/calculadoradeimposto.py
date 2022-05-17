#calculadora de imposto sobre salario 


#apresentação
print("bem vindo a calculadora de impostos sobre salario\n")
#recolher o valor do salario 
salario = float(input('digite o valor do seu salario: '))
nsalario = 0;

#imposto de renda
if(salario <= 1900): ir = 0.01
elif(salario >= 1900 and salario < 2826): ir = 0.075
elif(salario >= 2826 and salario < 3751): ir = 0.15
elif(salario >= 3751 and salario < 4664): ir = 0.225
else : ir = 0.275
#inss
if(salario < 1045): inss = 0.01
elif(salario >= 1045 and salario < 2089): inss = 0.075
elif(salario >= 2089 and salario < 3134): inss = 0.09
elif(salario >= 3134 and salario < 6101): inss = 0.12
else : inss = 0.141
#variavel que armazena a soma dos impostos
tax = inss + ir

#calcula o valor a ser retirado do salario 
vtretirado = salario * tax;
#retira o valor da taxa do salario
nsalario = salario - vtretirado;
#imprime resultado
print("seu salario liquido é de {}" .format(nsalario))