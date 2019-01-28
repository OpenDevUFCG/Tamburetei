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
    print instrumento                           # Imprime Guitarra
                                                # Imprime Bateria
                                                # Imprime Saxofone

# Outro uso bastante comum é
# iterar pelos índices de uma
# lista usando as funções auxiliares
# range() e len().
#
# Segue os links para as duas funções
# retirados da documentação oficial do
# python.
#
# .. [1] Função range, PythonDocs 2, PSF.
#        https://docs.python.org/2/library/functions.html#range
# .. [2] Função len, PythonDocs 2, PSF.
#        https://docs.python.org/2/library/functions.html#len
#
for indice in range(len(instrumentos)):
    print "O instrumento %s está no índice %d da lista." % (instrumentos[indice], indice)

# Seria o mesmo que executar
# o código abaixo, mas que não
# é nada amigável para listas
# com muitos elementos.
print "O instrumento %s está no índice %d da lista." % (instrumentos[0], 0)
print "O instrumento %s está no índice %d da lista." % (instrumentos[1], 1)
print "O instrumento %s está no índice %d da lista." % (instrumentos[2], 2)


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
    print contador,                             # Imprime 0 1 2 3 4
    contador = contador + 1                     # Adiciona 1 ao contador a cada iteração

# Outro exemplo bastante comum
# do uso de laços indefinidos é
# o emprego de valores booleanos
# na condição de parada, como pode
# ser visto no exemplo abaixo.
while True:
    print "Loop Infinito"

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
        print "Loop"
    else:                                       # Se contador não for menor que 5, para execução do laço
        break
    contador = contador + 1                     # Adiciona 1 ao contador a cada iteração

# Por fim, algo legal nos laços
# é que em muitos casos é possível
# utilizar as duas formas 'while' e 'for',
# embora existam situações em que
# um é mais conveniente que o outro
# para resolver o problema.
