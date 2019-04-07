#coding: utf-8

from Sort import Sort

__author__ = "Ionesio Junior"

class GnomeSort(Sort):
	"""Implementação do algoritmo de Ordenação GnomeSort
        
        Classe para abstração do algoritmo de Ordenação GnomeSort implementado de forma iterativa e recursiva
        
        Complexidade do Algoritmo: O(n^2)
        """

	def sort(self,array ,leftIndex = 0,rightIndex = None):
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
			# Escolher a abordagem a ser utilizada (Interativa / Recursiva)
                        self.__iteractiveGnomeSort(array,leftIndex,rightIndex)		
			#self.__recursiveGnomeSort(array,leftIndex,leftIndex + 1 ,rightIndex)
	
	
	
	def __iteractiveGnomeSort(self,array,leftIndex,rightIndex):
		"""Implementação do método GnomeSort de forma iterativa
		   
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """
                pivot = leftIndex +1
		while(pivot <= rightIndex):
			if(array[pivot] >= array[pivot -1]):
				pivot = pivot +1
			else:
				array[pivot] , array[pivot -1] = array[pivot -1] , array[pivot]
				if(pivot > leftIndex + 1):
					pivot = pivot -1
				else:
					pivot = pivot + 1
	
	
	
	
	def __recursiveGnomeSort(self,array,leftIndex,pivot,rightIndex):
		"""Implementação do método GnomeSort de forma recursiva
		
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """
                if(pivot <= rightIndex):
			if(array[pivot] >= array[pivot - 1]):
				self.__recursiveGnomeSort(array,leftIndex,pivot + 1 , rightIndex)
			else:
				array[pivot] , array[pivot - 1] = array[pivot - 1] ,array[pivot]
				if(pivot > leftIndex + 1):
					self.__recursiveGnomeSort(array,leftIndex,pivot - 1 ,rightIndex)
				else:
					self.__recursiveGnomeSort(array,leftIndex,pivot + 1 ,rightIndex)

	
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
                if(array == None or leftIndex < 0 or rightIndex > len(array) - 1 or leftIndex > rightIndex):
			return False
		else:
			return True
