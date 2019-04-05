#coding: utf-8
from Sort import Sort

__author__ = "Ionesio Junior" 

class SelectionSort(Sort):
        """Implementação do algoritmo de Ordenação SelectionSort
        
        Classe para abstração do algoritmo de Ordenação SelectionSort implementado de forma iterativa e recursiva
        Complexidade do Algoritmo: O(n^2)
        """

	def sort(self, array, leftIndex = 0 , rightIndex = None):
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
			# Escolher a abordagem a ser utilizada (Iterativa/ Recursiva | Padrão / Bidirecional)
			#self.__simpleSelectionSort(array,leftIndex,rightIndex)
			#self.__bidirectionalSelectionSort(array,leftIndex,rightIndex)
			self.__recursiveSimpleSelectionSort(array,leftIndex,rightIndex)
			#self.__recursiveBidirectionalSelectionSort(array,leftIndex,rightIndex)
	
	
	def __simpleSelectionSort(self, array, leftIndex, rightIndex):
                """Implementação do método SelectionSort de forma iterativa
                   
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """		
		while(leftIndex < rightIndex):
			minIndex = leftIndex
			for i in range(leftIndex + 1, rightIndex + 1):
				if(array[minIndex] > array[i]):
					minIndex = i
			array[minIndex], array[leftIndex] = array[leftIndex], array[minIndex]
			leftIndex = leftIndex + 1
	

	def __bidirectionalSelectionSort(self,array,leftIndex,rightIndex):
                """Implementação do método SelectionSort de forma iterativa e bidirecional
                   
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """
		while(leftIndex < rightIndex):
			minIndex = leftIndex
			for i in range(leftIndex + 1 ,rightIndex +1):
				if(array[minIndex] > array[i]):
					minIndex = i		
			array[minIndex], array[leftIndex] = array[leftIndex], array[minIndex]
			leftIndex = leftIndex +1
			
			maxIndex = rightIndex
			for i in range(rightIndex - 1 , leftIndex - 1, -1):
				if(array[maxIndex] < array[i]):
					maxIndex = i
			array[maxIndex], array[rightIndex] = array[rightIndex], array[maxIndex]
			rightIndex = rightIndex - 1

	
	def __recursiveSimpleSelectionSort(self,array,leftIndex,rightIndex):
                """Implementação do método SelectionSort de forma recursiva
                
                Parametros:
                    array: Lista a ser ordenada
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """
		if(leftIndex < rightIndex):
			self.__recursiveGetMin(array, leftIndex, rightIndex, leftIndex, leftIndex)
			self.__recursiveSimpleSelectionSort(array,leftIndex + 1,rightIndex)

	
	def __recursiveBidirectionalSelectionSort(self,array,leftIndex,rightIndex):
                """Implementação do método SelectionSort de forma recursiva e bidirecional
                
                Parametros:
                    array: Lista a ser ordenada    
                    leftIndex(Opcional): Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex(Opcional): Índice limítrofe a direita do array para ordenação parcial
                """		
		if(leftIndex < rightIndex):
			self.__recursiveGetMax(array, leftIndex, rightIndex, rightIndex, rightIndex)
			self.__recursiveGetMin(array, leftIndex, rightIndex, leftIndex, leftIndex)
			self.__recursiveBidirectionalSelectionSort(array, leftIndex + 1, rightIndex - 1)

	
	def __recursiveGetMax(self, array, leftIndex, rightIndex, maxValue, index):
		""" Método auxiliar de recursão
		Este método pega o maior elemento do array e troca de posição com o indíce a direita
		
		Parametros:
                    array: Lista a ser ordenada    
                    leftIndex: Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex: Índice limítrofe a direita do array para ordenação parcial
		    maxValue: Maior valor encontrado entre os limites esquerdo e direito
		    index: Índice do elemento a ser comparado
		"""
		if(index >= leftIndex):
			if(array[maxValue] < array[index]):
				maxValue = index
			self.__recursiveGetMax(array, leftIndex, rightIndex, maxValue, index - 1)
		else:
			array[maxValue], array[rightIndex] = array[rightIndex] , array[maxValue]


	def __recursiveGetMin(self,array,leftIndex,rightIndex,minValue,index):
                """ Método auxiliar de recursão
                Este método pega o menor elemento do array e troca de posição com o indíce a esquerda
                
                Parametros:
                    array: Lista a ser ordenada    
                    leftIndex: Índice limítrofe a esquerda do array para ordenação parcial
                    rightIndex: Índice limítrofe a direita do array para ordenação parcial
                    minValue: Menor valor encontrado entre os limites esquerdo e direito
                    index: Índice do elemento a ser comparado
                """		
		if(index <= rightIndex):
			if(array[minValue] > array[index]):
				minValue = index
			self.__recursiveGetMin(array, leftIndex, rightIndex, minValue, index + 1)
		else:
			array[minValue] ,array[leftIndex] = array[leftIndex] , array[minValue]

	
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
		if(array == None or leftIndex < 0 or rightIndex > len(array) - 1 or leftIndex >= rightIndex):
			return False
		else:
			return True
