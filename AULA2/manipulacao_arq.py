#1/usr/bin/python3


#######
##manipulando arquivos com pithon
#######

#### abrir um arquivo para modifiocacao
##########metodo nao recomendado

# ponteiro = open('nomedoarquivo.txt','a') #abre um ponteiro para 
# #escrita de arquivos, o modo utilizado é o read plus (r+) que serve para
# #leitura e escrita. possuimos varios modos de acesso, por exemplo:
# # w = sobreescrita
# # r = somente leitura
# # + = abre um arquivo para atualização (acrescenta e modifica)
# # a = complemento 
# # x = criação 
# # este metodo não é recomendado porque o ponteiro sempre necessita 
# # ser encerrado com o close, isso doi substituido com a adição do comando with (mostraremos em breve)


# ponteiro.write ('olá mundo\n')
# ponteiro.close()


### metodo usual###3


with open('nomedoarquivo2.txt', 'w') as arquivo:
    arquivo.write('olá mundo\n')    
with open('nomedoarquivo2.txt','r') as arquivo:
    letras = arquivo.read()     
    print(letras)   
