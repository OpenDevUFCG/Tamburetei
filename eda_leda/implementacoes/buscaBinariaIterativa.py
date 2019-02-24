# coding: utf-8

'''
Implementação do algoritmo de Busca Binária
Obs: A busca binária é útil para encontrar, de maneira bastante eficiente, um item em uma lista ordenada de itens.

*** Note que a lista deve ser ordenada, caso contrário o algoritmo não funcionará.

@author: Vinicius Barbosa
@tema: Busca binária
@referências:
    https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search
    https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
    https://pt.khanacademy.org/computing/computer-science/algorithms/binary-search/a/running-time-of-binary-search
'''

def buscaBinariaIterativa(alvo, array):
	min = 0
	max = len(array) - 1
	while min <= max:
		mid = (min + max)/2
		if array[mid] == alvo:
			return array[mid]
		else :
			if array[mid] < alvo: # Eliminamos os numeros a esquerda de mid da nossa busca
				min = mid + 1
			else: 				  # Eliminamos os números a direita de mid da nossa busca
				max = mid - 1

