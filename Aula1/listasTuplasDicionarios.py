#!/usr/bin/python3

# lista = ['arroz','feijão','óleo','sal','açucar','temperos','cerveja','macarrão','vinagre','azeite']
# #           0       1       2       3       4       5
# #print(lista[-2])

# #vetores multidimensionais
# Lista3d = [
#     [2,3,4,5],
#     [2,5,7,13],
#     [7,6,5,4],
# ]

# lista.append('carne')  #inclui item no final da lista
# print(lista)
# lista.pop(3)                  #remove item
# lista.sort()                  #ordena por ordem alfabetica/ numerica 
# print(len(lista))             #mostra quantos indeces tem na lista 
# print(lista.index('feijão'))  #procura o item feijão
# lista.insert(4,'sabão em pó') #adicionar item em local determinado da lista 
# print(lista)
# lista.remove('sabão em pó') #remove o primeiro indice encontrado com o valor passado
# print(lista) 
# lista[3]='maça'     #sobrescreve um elemento
# print(lista)

#######################
#   TUPLAS
#######################

# tupla = ('maçã','banana','laranja','abacaxi','uva') #primeiro metodo
# tupla2= 'valor1',2, True, 2j    # segundo metodo
# print(type(tupla2))

# #acessando indices de uma tupla

# print(tupla[2])
# print(tupla[1:4])
# print(tupla[-2])

# #converter tupla para lista 
# lista_da_tupla= list(tupla)
# print(tupla)

# #####
# tupla = (['Indice 1'], 'nome')
# tupla[0].insert(1,'indice 2')
# print(tupla)

####################
#Dicionarios
####################

# criando dicionarios 
# apresentacoes = {
# 'paulista'  : 'Salve',
# 'Carioca'   : 'Eae',
# 'pirata'    : 'Argh',
# 'mineiro'   : 'pao de queijo',  
# 'acre'      : 'barulhos de dinossauro',

# }

# #acessando o dicionario
# print(apresentacoes['paulista'])

# linguagem_favorita={
#     'Daniel':{
#         'linguagem' : 'Python',
#         'tempo_de_experiencia' : 5
#     },
#     'Olympio' : {
#         'linguagem' :'R',
#         'linguagem2' : 'VBA',
#         'tempo_de_experiencia' : 10
#     },
# }
# print(linguagem_favorita.get('Daniel')['linguagem'])

# print(linguagem_favorita.keys())

# #acessar os itens

# print(linguagem_favorita.items())


#############
### Numeros
############


somar = 2+2
print(2+2, ' retornando o valor 2+2')
print(somar, 'retornando o somar')

subtrair = somar -2 #somar retorna um tipo de inteiro
print(subtrair, 'retornando o valor da subtração')
multiplicar = subtrair * 3  #subtrair tambem retorna um inteiro
print(multiplicar, 'retornando o valor da multiplicação')
divisao = multiplicar /5 #multiplicar tambem retorna um tipo inteiro
print(divisao, 'retornandoo dividir') #retorna um valor de ponto flutuante

potencia = 2**2
print(potencia, 'retornando o valor da potencia')
raiz=2**0.5
print(raiz, 'retornando o valor da raiz')

letras ='abcdefghijk' + 'lmnopqrstuvwxyz'
print(letras[5])