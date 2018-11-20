# coding: utf-8

# CONDICIONAIS
#
# Os condicionais são estruturas responsáveis por causar desvio de flu-
# xo a partir do valor de uma expressão lógica. Em outras palavras, é o
# valor de uma condição (verdadeira ou falsa) que determinará se um blo-
# co de código será ou não executado. Em Python, os condicionais são IF,
# ELIF e ELSE.
# 
# O IF é uma estrutura condicional simples e sua sintaxe é da forma "if 
# (condição):". Caso a condição seja verdadeira, o bloco de código após
# os dois pontos será executado, caso contrário, não. Em termos de algo-
# ritmo representa "SE condição ENTÃO FAÇA isso".
#
# O ELIF é uma estrutura condicional aninhada e sua sintaxe é da forma
# "if (condição1): {...} elif (condição2):". O bloco de código após os
# dois pontos do ELIF será executado se, e somente se, a condição1 for
# falsa e a condição2 for verdadeira. O ELIF só pode ser utilizado em
# aninhamento com um IF. Em termos de algoritmo, teríamos "SE condição1
# ENTÃO FAÇA isso SENÃO SE condição2 FAÇA aquilo".
#
# O ELSE é uma estrutura condicional composta e, tal como o ELIF, somen-
# te pode ser utilizada em associação com um IF. Sua sintaxe é da forma
# "if (condição1): {...} else:", devendo estar após todos os IFs e ELIFs
# de uma estrutura condicional. O bloco de código após os dois pontos do
# else será executado se, e somente se, todas as condições anteriores fo-
# rem falsas. Em termos de algoritmo, teríamos "SE condição ENTÃO FAÇA 
# isso SENÃO FAÇA aquilo".

# DEMONSTRAÇÃO
#
# O código abaixo pode ser executado para melhor compreensão do funcio-
# namento dos condicionais.

value = int(raw_input("Insira um número: "))

if (value > 1):
    print "O número digitado é maior que um."
if (value > 10):
    print "O número digitado é maior que dez."
if (value > 100):
    print "O número digitado é maior que cem."


if (value < 0):
    print "O número digitado é negativo."
elif (value > 0):
    print "O número digitado é positivo."


if ((value % 2) == 0):
    print "O número digitado é par."
else:
    print "O número digitado é ímpar."


if (0 <= value < 10):
    print "O número digitado está entre 0 e 10."
elif (10 <= value < 20):
    print "O número digitado está entre 10 e 20."
elif (20 <= value <= 100):
    if (20 <= value < 50):
        print "O número digitado está entre 20 e 50."
    else:
        print "O número digitado está entre 50 e 100."
else:
    print "O número não está entre 0 e 100."
