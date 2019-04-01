#coding: utf-8

from Sort import Sort

__author__ = "Ionesio Junior"

class GnomeSort(Sort):
	
	''' Gnome sort class have many ways to implement gnome sort algorithm idea '''
	

	def sort(self,array ,leftIndex = 0,rightIndex = None):
        	'''Generic Sort
                algorithm.sort(array) -> return complete ordered array
                algorithm.sort(array,leftLimit,rightLimit) -> return partially ordered array
        	'''  
		if(rightIndex == None):
			rightIndex = len(array) - 1
		if self.__validateParams(array,leftIndex,rightIndex):
			#Choose the type of GnomeSort
                        self.__simpleGnomeSort(array,leftIndex,rightIndex)		
			#self.__recursiveGnomeSort(array,leftIndex,leftIndex + 1 ,rightIndex)
	
	
	
	def __simpleGnomeSort(self,array,leftIndex,rightIndex):
		''' Simple iteractive Gnome sort implementation '''
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
		''' Recursive Gnome Sort implementation '''
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
	        ''' This method verify if parameters are valid if some parameter is not valid the method returns false '''
		if(array == None or leftIndex < 0 or rightIndex > len(array) - 1 or leftIndex > rightIndex):
			return False
		else:
			return True
