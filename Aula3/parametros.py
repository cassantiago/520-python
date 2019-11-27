#!/usr/bin/python3

######################
##
#####################

# def retorna_pessoa(nome,idade=99):
#     print(f'nome: {nome}\nidade: {idade}')
# retorna_pessoa(nome='Daniel', idade=19)


#############
##especificar tipo de parametro e retorno
#############
#Anotacoes de funcao 
#print ('olá','mundo',',','prazer','sou','daniel')
############criando uma função que recebe multiplos valores
# def funcao_multi_valores(parametros_estaticos,*argumento_variavel):
#     print(parametros_estaticos,'parametro estático')
#     print(argumento_variavel)
    #fazendo acesso aos parametros
    #for argumento in argumento_variavel:
     #   print(argumento)
# funcao_multi_valores('valor estatico obrigatório',
#                      'Daniel','andressa','joão','Ana',
#                      'Paula','lucas','Leonardo','Pedro')

##Argumentos com palavras chave -kwargs

# def parametros_chave_valor(**dados):
#     if dados['nome']=='daniel':
#         print ('acesso negado')
#     print(dados)
# #Execução - metodo 1
# print('metodo 1')
# parametros_chave_valor(nome='Daniel',sobrenome='Silva',
#                         idade=19,sexo='masculino')

# #execução - metodo 2

dados_requisicao = {'nome':'Daniel',
                    'sobrenome':'Silva',
                    'Profissão':'Operador de empilhadeira'}

#parametros_chave_valor(**dados_requisicao)

#decoradores de função
#uma funcao que modifica o valor da outra


#declara uma funcao com uma variavel funcao obrigatoria
def mudaCor(retorno_funcao):
    def modificaAzul(retorno_funcao):
        return f'\033[91m{retorno_funcao}\033[0m'
    return modificaAzul
@mudaCor
def log(texto):
    return texto
print(log('oi'))   



3