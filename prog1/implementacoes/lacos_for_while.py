# coding: utf-8

# LAÇOS DEFINIDOS (FOR)
#
# Os laços definidos iteram
# sobre coleções, repetindo
# o bloco de código até o
# último item da coleção.
#
# A estrutura sintática
# dos laços definidos é
# formada pelas palavras
# reservadas 'for' e 'in',
# por uma variável de controle,
# uma coleção e pelo bloco
# de código a ser executado
# para cada item.
#
# SINTAXE:
# for <variável_de_controle> in <coleção>:
#     <bloco_de_código>
#

instrumentos = ["Guitarra", "Bateria", "Saxofone"]

# No exemplo abaixo, o for itera
# sobre a lista instrumentos,
# imprimindo todos os seus elementos.
for instrumento in instrumentos:
    print (instrumento)                           # Imprime Guitarra
                                                # Imprime Bateria
                                                # Imprime Saxofone

# Outro uso bastante comum é
# iterar pelos índices de uma
# lista usando as funções auxiliares
# range() e len().

# range()
""" Gera uma lista de números inteiros

A função range é nativa do python e
é utilizada quando há a necessidade
de se gerar uma sequência de números.
Por padrão, a sequência começa do 0 e
vai até o número anterior ao passado
como parâmetro (stop), incrementando
de 1 em 1.

Parameters
----------
start : int, optional
    Número inteiro que especifica a posição inicial
stop : int
    Número inteiro que especifica a posição final
step : int, optional
    Número inteiro que especifica o pulo ou incremento

Return
------
numbers : list
    Lista contendo a sequência de números
"""

# len()
""" Retorna o comprimento de um objeto

A função len é nativa do python e
é utilizada quando há a necessidade
de retornar o comprimento de um objeto.
No caso do objeto ser uma string, é
retornado a quantidade de caracteres
que a string possui. No caso de uma
coleção, é retornado a quantidade de
elementos que contém.

Parameters
----------
object : sequence | collection
    Objeto que se quer saber o comprimento

Return
------
length : int
    Comprimento do objeto dado como parâmetro
"""

for indice in range(len(instrumentos)):
    print ("O instrumento %s está no índice %d da lista." % (instrumentos[indice], indice))

# Seria o mesmo que executar
# o código abaixo, mas que não
# é nada amigável para listas
# com muitos elementos.
print ("O instrumento %s está no índice %d da lista." % (instrumentos[0], 0))
print ("O instrumento %s está no índice %d da lista." % (instrumentos[1], 1))
print ("O instrumento %s está no índice %d da lista." % (instrumentos[2], 2))


# LAÇOS INDEFINIDOS (WHILE)
#
# Os laços indefinidos iteram
# baseados em uma condição que
# define se o bloco vai ou não
# ser executado.
#
# A estrutura sintática
# dos laços indefinidos é
# formada pela palavra
# reservada 'while', por
# uma condição de execução
# e pelo bloco de código a
# ser executado caso a condição
# seja atendida.
#
# SINTAXE:
# while <condição>:
#     <bloco_de_código>
#

# No exemplo abaixo, enquanto
# o contador for menor do que
# cinco (condição), o próprio
# contador é impresso (bloco).
contador = 0
while contador < 5:
    print (contador)                             # Imprime 0 1 2 3 4
    contador = contador + 1                     # Adiciona 1 ao contador a cada iteração

# Outro exemplo bastante comum
# do uso de laços indefinidos é
# o emprego de valores booleanos
# na condição de parada, como pode
# ser visto no exemplo abaixo.
while True:
    print ("Loop Infinito")

# Como a condição é sempre verdadeira,
# o bloco é executado infinitas vezes.
#
# No entanto, existe uma maneira de
# parar a execução infinita do bloco,
# utilizando a palavra reservada 'break'.
#
# OBS: O break pode ser utilizado tanto nos laços
# definidos, como também nos laços indefinidos.
contador = 0
while True:
    if contador < 5:                            # Se contador for menor que 5, imprime Loop
        print ("Loop")
    else:                                       # Se contador não for menor que 5, para execução do laço
        break
    contador = contador + 1                     # Adiciona 1 ao contador a cada iteração

# Por fim, algo legal nos laços
# é que em muitos casos é possível
# utilizar as duas formas 'while' e 'for',
# embora existam situações em que
# um é mais conveniente que o outro
# para resolver o problema.
