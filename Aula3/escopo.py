#!/usr/bin/python3

#########################
## Escopo de variaveis locais e globais
#########################

#Variavel de escopo global
variavel =3

def muda_variavel():
    #variavel = 2  #escopo local
    global variavel
    variavel = 2    #escopo global
    print(variavel)

muda_variavel()    