# coding: utf-8

#======================================================================#
# Condicionais                                                         #
#======================================================================#
# Abaixo você pode encontrar alguns exemplos de uso de condicionais,   #
# expressões simples que você utilizará frequentemente na grande       #
# maioria dos seus algoritmos e programas nos quais você irá criar.    #
# Já no inicio da disciplina de Programação 1 (na terceira unidade)    #
# você será introduzido aos condicionais, que são eles: if, elif e     #
# else.                                                                #
# Para utilizar uma estrutura condicional, você DEVE começar com um if #
# que irá validar uma dada proposição lógica, que caso verdadeira ele  #
# irá executar seu bloco de cógido e após isso pular para fora da      #
# estrutura condicional, e caso falsa, ele irá pular o bloco do if e   #
# checar se a próxima condição é cumprida (seja ela dada por um elif   #
# ou um else. Se for um if, ela faz parte de outra estrutura).         #
# O elif só pode ser utilizado após um if ou outro elif, e só será     #
# executado caso todas as condicionais anteriores dessa estrutura      #
# sejam falsas.                                                        #
# O else, diferente do if e elif, não pode validar uma operação        #
# booleana, e será executado como último caso onde nem o if nem os     #
# elifs foram executados, e por isso só pode ser utilizado no final de #
# uma estrutura condicional.                                           #
#======================================================================#
# if                                                                   #
#======================================================================#

entrada = raw_input()   #receberá uma string qualquer como entrada
if len(entrada) > 5:    #checa se a string possui tamanho maior que 5
    print("TEM MAIS DE 5 CARACTERES!")
if len(entrada) > 10:   #checa se a string possui tamanho maior que 10
    print("TEM MAIS DE 10 CARACTERES!")
if len(entrada) > 15:   #checa se a string possui tamanho maior que 15
    print("TEM MAIS DE 15 CARACTERES!")

#======================================================================#
# No exemplo acima, pode-se observar que todas as três mensagens serão #
# imprimidas na tela caso você digite uma entrada com mais de 15       #
# caracteres, isso porquê o if sozinho apenas checa se é verdade e     #
# executa. Ele não se importa se outras condições acima dela já foram  # 
# cumpridas, pois como dito anteriormente ele inicia uma nova          #
# estrutura condicional.                                               #
#======================================================================#
# else                                                                 #
#======================================================================#

entrada = raw_input()
if 10 > len(entrada) > 5:
    print("TEM ENTRE 10 E 5 CARACTERES!")
else:
    print("NÃO TEM ENTRE 10 E 5 CARACTERES!")
if entrada == "cachorro":
    print("É UM CACHORRO! :D")
else:
    print("NÃO É UM CACHORRO... :c")
if entrada.islower():
    print("ESTÁ TODO EM MINUSCULO!")
if entrada.isdigit():
    print("É UM NÚMERO! :o")
else:
    print("NÃO É UM NÚMERO. :/")

#======================================================================#
# Neste exemplo, pode-se observar que apenas uma das duas opções entre #
# if e else é executada. Se estiver entre 10 e 5, executa o if, se não #
# executa o else.                                                      #
# Observa-se também que o else depende apenas das condições a partir   #
# do ultimo if antes dele (ou seja, da própria estrutura).             #
# Obs: o else só pode existir caso tenham ifs/elifs imediatamente      #
# antes dele, um else solto no código é um erro de sintaxe e irá       #
# quebrar seu programa.                                                #
#======================================================================#
# elif                                                                 #
#======================================================================#

entrada = raw_input()
if len(entrada) < 10:
    print("TEM MENOS DE 10 CARACTERES!")
elif len(entrada) < 20:
    print("TEM PELO MENOS 10 CARACTERES, MAS TEM MENOS DE 20!")
else:
    print("TEM PELO MENOS 20 CARACTERES!! :ooo")
if entrada == "cachorro":
    print("É UM CACHORRO!! :DDD")
elif entrada == "gato":
    print("É UM GATO!! :DDD")
elif entrada == "rato":
    print("É UM RATINHO!!! <3")
elif entrada == "trebuchet":
    print("Consegue arremessar um objeto de 90kg por mais de 300 metros")
elif entrada == "python":
    print("ruby >>>>>")
else:
    print("EU NÃO SEI OQ É :c")
if entrada.isdigit():
    print("É UM NÚMERO! :D")
elif entrada.islower():
    print("BEM, NÃO É UM NÚMERO MAS PELO MENOS TA TODO EM MINÚSCULO.")

#======================================================================#
# Como observado acima, o elif é utilizado após o if e, caso exista,   #
# antes do else. Também observa-se que diferente do if e else, você    #
# pode utilizar inúmeros elifs em uma mesma estrutura condicional.     #
# Observa-se porém que da mesma forma do else, o elif PRECISA ser      #
# precedido por um if ou outro elif, como dito anteriormente.          #
#======================================================================#