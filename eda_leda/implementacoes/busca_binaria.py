# coding: utf-8
#
# BUSCA BINÁRIA
#
# A busca binária é um algoritmo de busca em vetores que segue o paradigma
# de divisão e conquista.
# 
# Ela parte do pressuposto de que o vetor está ordenado e realiza sucessivas
# divisões do espaço de busca comparando o elemento buscado (chave) com o
# elemento no meio do vetor. Se o elemento do meio do vetor for a chave,
# a busca termina com sucesso. Caso contrário, se o elemento do meio vier
# antes do elemento buscado, então a busca continua na metade posterior do
# vetor. E finalmente, se o elemento do meio vier depois da chave, a busca
# continua na metade anterior do vetor.
#
# @author: Vinicius Barbosa

def buscaBinariaIterativa(alvo, array):
    """ Retorna o índice do array em que o elemento alvo está contido.

    Considerando a coleção recebida como parâmetro, identifica e retor-
    na o índice em que o elemento especificado está contido. Caso esse
    elemento não esteja presente na coleção, retorna -1. Utiliza uma
    abordagem iterativa.

    Parameters
    ----------
    alvo : ?
        Elemento cujo índice está sendo buscado
    array : list
        A lista cujo índice do elemento deve ser identificado
    
    Return
    ------
    index : int
        O índice em que o elemento alvo está armazenado
    """
    min = 0
    max = len(array) - 1
    while (min <= max):
        mid = (min + max) // 2
        if (array[mid] == alvo):
            return mid
        else:
            if (array[mid] < alvo):
                min = mid + 1
            else:
                max = mid - 1
    return -1

def buscaBinariaRecursiva(alvo, array):
    """ Retorna o índice do array em que o elemento alvo está contido.

    Considerando a coleção recebida como parâmetro, identifica e retor-
    na o índice em que o elemento especificado está contido. Caso esse
    elemento não esteja presente na coleção, retorna -1. Utiliza uma
    abordagem recursiva.

    Parameters
    ----------
    alvo : ?
        Elemento cujo índice está sendo buscado
    array : list
        A lista cujo índice do elemento deve ser identificado
    
    Return
    ------
    index : int
        O índice em que o elemento alvo está armazenado
    """
    return buscaBinariaRecursivaAux(alvo, array, 0, len(array) - 1)

def buscaBinariaRecursivaAux(alvo, array, min, max):
    """ Método auxiliar para buscaBinariaRecursiva(alvo, array) """
    if (min <= max):
        mid = (min + max) // 2
        if (array[mid] == alvo):
            return mid
        else:
            if (array[mid] < alvo):
                return buscaBinariaRecursivaAux(alvo, array, mid + 1, max)
            else:
                return buscaBinariaRecursivaAux(alvo, array, min, mid - 1)
    else:
        return -1



# DEMONSTRAÇÃO
#
# O código abaixo pode ser executado para observação do funcionamento
# das funções implementadas anteriormente.

array = ['amanda', 'ana', 'carlos', 'gabriela', 'luana', 'lucas',
         'marcos', 'pedro', 'stephanne', 'victor', 'vinicius']

# Busca binária iterativa
assert 1 == buscaBinariaIterativa('ana', array)
assert 3 == buscaBinariaIterativa('gabriela', array)
assert 5 == buscaBinariaIterativa('lucas', array)
assert 9 == buscaBinariaRecursiva('victor', array)

# Busca binária recursiva
assert 0 == buscaBinariaRecursiva('amanda', array)
assert 6 == buscaBinariaRecursiva('marcos', array)
assert 8 == buscaBinariaIterativa('stephanne', array)
assert 10 == buscaBinariaRecursiva('vinicius', array)

# Busca binária com chave inexistente
assert -1 == buscaBinariaIterativa('joaope', array)
assert -1 == buscaBinariaRecursiva('joaope', array)
