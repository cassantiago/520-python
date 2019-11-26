#!/usr/bin/python3

###############################
##estrutura condicional simples
###############################

nome = input ('digite seu nome: ') .strip() .title()
sobrenome = input('digite seu sobrenome: ').strip() .title()
# # if nome == 'Daniel':
# #     print('ola professor')
# # print('seja bem vindo')

#################################
##estrutura condicional composta
#################################
#nome = input ('digite seu nome: ')

if nome == 'Daniel' and sobrenome == 'Silva':
    print(f'Bem vindo Professor {nome}')
else:
    print(f'Bem vindo aluno {nome}')
print('Você pode utilizar a plataforma')


################################
##condicionais encadeadas
################################

if nome == 'Daniel':
    if sobrenome == 'silva':
        print ('Olá Professor')
    else:
        print('Você é Daniel, mas não e professor') 
else:
    print(f'Olá Aluno {nome}')           

