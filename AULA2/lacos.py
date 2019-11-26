#!/usr/bin/python3

############
#Lacos de Repeticao
#############


############
## Laco While
###########
#Este laço executa enquanto uma condiçao for verdadeira

# i = 0
# while(i<10):    #enquanto i for menor que 10
#     print(i)    #mostra valor de i
#     i +=1       #i = i+1
    #repete

#como fazer controle de um loop while
# i = 0
# while(True):
#     print('teoricamente, um loop infinito')
#     i += 1
#     if i== 10:
#         break
#     if i == 5:
#         continue
#     print('teoricamente, um loop infinito')    
# i = 100             #numero inicial iterador
# while i > 0:        #enquanto i < 0
#     i -=1           #i = i - 1
#     if i % 2 == 1:  #
#         continue
#     print(i)    


    ################
    #laço for
    ################

    #percorre itens em determinado alcance de valores
# lista = []
# for i in range(0,100,3): #começa do 1, vai até 0 100 de 3 em 3
#     lista.append(i)
# print(lista)
# #percorrer uma lista
# for i in lista:
#     if i % 2 == 0:
#         print(f'\033[31m{i}\033[0m','par')
#     if i % 2 == 1:
#         print(f'\033[32m{i}\033[0m','impar')
#percorrer um dicionario

# dicionario = {'nome':
#  'Daniel',
#  'sobrenome': 'Silva'
#   } 
#for i in dicionario:
#    print(dicionario[i])

#for chave,valor in dicionario.itens():
#    print(chave)
#    print(valor) 
# 
# 
# ######################
# ##enumerando itens de uma lista 
########################

# lista = ['item1', 'item2','item3', 'item4', 'item5', 'item6', 'item7']
#print(list(enumerate(lista)))
# for indice, valor in enumerate(lista):
#     print (indice)

#list comprehension (compreensão de lista)
lista = [x for x in range(100)]
print(lista)