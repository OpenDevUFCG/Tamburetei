#coding: utf-8

from Sort import Sort

__author__ = "Ionesio Junior"

class InsertionSort(Sort):
	"""Implementação do algoritmo de Ordenação InsertionSort
        
        Classe para abstração do algoritmo de Ordenação InsertionSort implementado de forma iterativa e recursiva
        Complexidade do Algoritmo: O(n^2)
        """
	
	def sort(self,array=None,leftIndex = 0,rightIndex = None):
                """Método genérico de interface para aplicar 
                   o algoritmo de ordenação no array por completo ou usando limites
                
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limitrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limitrofe a direita do array para ordenação parcial

                Exemplo de execução:
                    algorithm.sort(array): Retorna a lista completamente ordenada
                    algorithm.sort(array,leftLimit,rightLimit): Retorna a lista parcialmente ordenada
                """		
                if(rightIndex == None):
			rightIndex = len(array) - 1
		if self.__validateParams(array,leftIndex,rightIndex):
			# Escolher a abordagem a ser utilizada (Iterativa / Recursiva)
                        #self.__simpleInsertionSort(array,leftIndex,rightIndex)
			 self.__recursiveInsertionSort(array,leftIndex,rightIndex,leftIndex +1)
	

	def __simpleInsertionSort(self,array,leftIndex,rightIndex):
                """Implementação do método InsertionSort de forma iterativa
                   
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """
                for i in range(leftIndex,rightIndex+1):
			j = i
			while(j > leftIndex and array[j] < array[j-1]):
				array[j] , array[j -1] = array[j -1] , array[j]
				j = j - 1
	
	def __recursiveInsertionSort(self,array,leftIndex,rightIndex,pivot):
                """Implementação do método InsertionSort de forma recursiva
                
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """		
                if(pivot <= rightIndex):
			self.__recursiveSwitchBack(array,leftIndex,pivot)
			self.__recursiveInsertionSort(array,leftIndex,rightIndex,pivot+1)
	

	def __recursiveSwitchBack(self,array,leftIndex,pivot):
                """ Método auxiliar de recursão
                Método responsável por verificar e trocar elementos caso estes sejam menores que o pivô
                Parametros:
                    leftIndex: Índice limite a esquerda
                    pivot: Pivô usado como referência para comutar elementos
                """
		if(pivot > leftIndex  and array[pivot] < array[pivot -1]):
			array[pivot] , array[pivot - 1] = array[pivot -1] , array[pivot]
			self.__recursiveSwitchBack(array,leftIndex,pivot - 1)
	
		
	def __validateParams(self,array,leftIndex,rightIndex):
                """Verificação da validade dos parametros de limite passados
                
                Este método busca evitar entradas inválidas para o algoritmo de ordenação, tais como: índices negativos,
                índice direito menor que o esquerdo, índice direito superior ao tamanho do array.

                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial

                Retorna:
                    Boolean: Indicando se os parâmetros são ou não válidos
                """
                if(array == None or leftIndex < 0 or rightIndex > len(array)-1 or leftIndex >= rightIndex):
			return False
		else:
			return True
