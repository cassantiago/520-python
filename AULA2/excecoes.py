#!/usr/bin/python3

######
#tratando excecoes
######

# try:
#     print('soma de dois valores')
#     numero1 = int(input('digite um numero a ser somado: '))
#     numero2 = int(input('digite outro numero a ser somado '))
#     print(numero1 + numero2)
# except ValueError:    #Exceção              
#     print('Insira  somente Números') 

# try:
#     print('divisoes de dois valores')
#     numero1 = int(input('digite um numero a ser dividido: '))
#     numero2 = int(input('digite outro numero a ser dividido '))
#     print(numero1 / numero2)
# except ValueError:    #Exceção              
#     print('Insira  somente Números') 
# except ZeroDivisionError as e:
#     print('não foi possivel fazer a divisão', e)
# except Exception as e:
#     print('Erro de execucao do programa', e)
# finally:
#     print('saindo do script')         
           


#############
##Lançando Exceções
#############

#try:
opcao = input('não digite 5:')
if opcao == '5':
    raise ValueError('eu falei pra você não digitar 5')
#except ValueError as e:
#    print('Deu erro: ', e)        