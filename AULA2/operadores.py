#!/usr/bin/python3







#############
# Operadores Aritiméticos
############
#variaveis por nomenclatura podem ter no max 16 caracteres
num1 = 6
num2 = 8
adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
result_div_int = num1 // num2
resto_div_int = num1 % num2

# operadores de forma abreviada
#pegha o valor atual do numero e realiza um calculo
#atribuindo o resultado a variavel

numero = 1
numero += 3     #1+3        numero = numero + 3
numero -= 3     #4-3        numero = numero - 3
numero *= 4     #1*4        numero = numero * 4
numero /= 2     #4/2        numero = numero / 2
numero //= 2    #2//2=1     numero = numero //2
numero %= 2     #2%2=0      numero = numero % 2


########################
# Operadores relacionais
########################

#operadores relacionais servem para comparação entre fatores
#retornam valores booleanos (true false)
numero1 = 6
numero2 = 9
numero3 = numero1

print(numero1 == numero2)       #igualdade 
print(numero1 != numero2)       #Diferente 
print(numero1 < numero2)        #menor que  
print(numero1 <= numero2)       #menor ou igual
print(numero1 > numero2)        #maior
print(numero1 >= numero2)       #maior ou igual

print(numero3 is numero1)       #compara se estao alocados no mesmo bloco memoria 

