# coding: utf-8
#
# BUSCA BINÁRIA
#
#   A busca binária é um algoritmo de busca em vetores que segue o paradigma
# de divisão e conquista.
#   Ela parte do pressuposto de que o vetor está ordenado e realiza sucessivas
# divisões do espaço de busca comparando o elemento buscado (chave) com o
# elemento no meio do vetor. Se o elemento do meio do vetor for a chave,
# a busca termina com sucesso. Caso contrário, se o elemento do meio vier
# antes do elemento buscado, então a busca continua na metade posterior do
# vetor. E finalmente, se o elemento do meio vier depois da chave, a busca
# continua na metade anterior do vetor.

# @author: Vinicius Barbosa
# @tema: Busca binária
# @referências:
#     https://pt.wikipedia.org/wiki/Pesquisa_bin%C3%A1ria
#     https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
#     https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
#     https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/running-time-of-binary-search


def buscaBinariaIterativa(alvo, array):
    min = 0
    max = len(array) - 1
    while min <= max:
        mid = (min + max)/2
        if array[mid] == alvo:
            return mid
        else:
            if array[mid] < alvo:
                min = mid + 1
            else:
                max = mid - 1
    return -1


def buscaBinariaRecursiva(alvo, array):
    return buscaBinariaRecursivaAux(alvo, array, 0, len(array) - 1)


def buscaBinariaRecursivaAux(alvo, array, min, max):
    if min <= max:
        mid = (min + max)/2
        if array[mid] == alvo:
            return mid
        else:
            if array[mid] < alvo:
                return buscaBinariaRecursivaAux(alvo, array, mid + 1, max)
            else:
                return buscaBinariaRecursivaAux(alvo, array, min, mid - 1)
    else:
        return -1


# TESTES

array = ['amanda', 'ana', 'carlos', 'gabriela', 'luana', 'lucas',
         'marcos', 'pedro', 'stephanne', 'victor', 'vinicius']

# testa a busca binária iterativa
assert 8 == buscaBinariaIterativa('stephanne', array)
assert 10 == buscaBinariaIterativa('vinicius', array)
assert 1 == buscaBinariaIterativa('ana', array)
assert 3 == buscaBinariaIterativa('gabriela', array)
assert 5 == buscaBinariaIterativa('lucas', array)
assert 6 == buscaBinariaIterativa('marcos', array)
assert 9 == buscaBinariaIterativa('victor', array)
assert 0 == buscaBinariaIterativa('amanda', array)

# testa a busca binária recursiva
assert 8 == buscaBinariaRecursiva('stephanne', array)
assert 10 == buscaBinariaRecursiva('vinicius', array)
assert 1 == buscaBinariaRecursiva('ana', array)
assert 3 == buscaBinariaRecursiva('gabriela', array)
assert 5 == buscaBinariaRecursiva('lucas', array)
assert 6 == buscaBinariaRecursiva('marcos', array)
assert 9 == buscaBinariaRecursiva('victor', array)
assert 0 == buscaBinariaRecursiva('amanda', array)

# testa a busca binária com chave inexistente
result = buscaBinariaIterativa('joaope', array)
assert result == -1
result = buscaBinariaRecursiva('joaope', array)
assert result == -1
