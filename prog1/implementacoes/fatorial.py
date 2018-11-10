# coding: utf-8

def iterative_factorial(number):
    """ Calcula o fatorial de um número.

    Realiza o cálculo do fatorial do número passado por parâmetro e o re-
    torna. O fatorial de um número é dado pelo produto de todos os núme-
    ros positivos menores ou iguais a esse número, excetuando-se 0, cujo
    fatorial tem valor 1. Essa função utiliza uma abordagem iterativa
    para a realização do cálculo.

    Parameters
    ----------
    number : int
        O número cujo fatorial será calculado.
    
    Return
    ------
    factorial : int
        O valor do fatorial calulado.
    """
    assert (number >= 0) # Fatorial só pode ser calculado para não-negativos

    factorial = 1
    if (number != 0):
        for n in range(1, number + 1):
            factorial *= n
    return factorial

def recursive_factorial(number):
    """ Calcula o fatorial de um número.

    Realiza o cálculo do fatorial do número passado por parâmetro e o re-
    torna. O fatorial de um número é dado pelo produto de todos os núme-
    ros positivos menores ou iguais a esse número, excetuando-se 0, cujo
    fatorial tem valor 1. Essa função utiliza uma abordagem recursiva
    para a realização do cálculo.

    Parameters
    ----------
    number : int
        O número cujo fatorial será calculado.
    
    Return
    ------
    factorial : int
        O valor do fatorial calulado.
    """
    assert (number >= 0) # Fatorial só pode ser calculado para não-negativos

    if (number == 0):
        return 1
    else:
        return (number * recursive_factorial(number - 1))


# DEMONSTRAÇÃO
#
# O código abaixo pode ser executado para observação do funcionamento
# das funções implementadas anteriormente.

print "ABORDAGEM ITERATIVA\n"
print "O fatorial de 0 é", iterative_factorial(0)
print "O fatorial de 1 é", iterative_factorial(1)
print "O fatorial de 2 é", iterative_factorial(2)
print "O fatorial de 5 é", iterative_factorial(5)
print "O fatorial de 15 é", iterative_factorial(15)

print "\nABORDAGEM RECURSIVA\n"
print "O fatorial de 0 é", recursive_factorial(0)
print "O fatorial de 1 é", recursive_factorial(1)
print "O fatorial de 2 é", recursive_factorial(2)
print "O fatorial de 5 é", recursive_factorial(5)
print "O fatorial de 15 é", recursive_factorial(15)
