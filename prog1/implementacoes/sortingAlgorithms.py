# coding: utf-8
import random

#======================================================================#
# Algoritmos de ordenação                                              #
#======================================================================#
# Frequentemente quando se trabalha com estruturas de dados (como por  #
# exemplo lista e dicionário, que são os que vocês vê-em em Prog1)     #
# você precisará ordenar os valores dentro delas.                      #
# Os códigos abaixo servem justamente para essa funcionalidade:        #
# ordenação. A diferença entre cada um deles é basicamente o quão      #
# rápido ele é, porém esse conhecimento ainda não é necessário no      #
# primeiro período. Porém caso tenha interesse, estão ai os mais       #
# comumente utilizados.                                                #
#======================================================================#
#         IMPLEMENTAÇÕES                                               #
#======================================================================#
# Bubble Sort                                                          #
#     O algoritmo a seguir é um dos mais simples. Ele sai comparando   #
#     valores vizinhos e jogando os maiores até o final da lista       #
#     diversas vezes, até que todos os valores tenham sido comparados  #
#     entre si.                                                        #
#======================================================================#

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

#======================================================================#
# Insertion Sort                                                       #
#     O algoritmo a seguir é relativamente mais complexo que o Bubble, #
#     porém um pouco mais eficiente. Ele "particiona" a lista salvando #
#     um valor chave (a variável key) que vai delimitar a divisão      #
#     entre a lista ordenada (na esquerda da chave) e a lista não      #
#     ordenada (da chave em diante). E então ela insere o valor chave  #
#     na nova lista já em uma posição ordenada. A chave então avança   #
#     para o próximo índice e o ciclo se repete.                       #
#======================================================================#

def insertion_sort(lista):
    for i in range(1,len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and lista[j] > key:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            j -= 1

#======================================================================#
# Selection Sort                                                       #
#     O algoritmo a seguir é mais simples de compreender que o         #
#     anterior, e possui uma complexidade e eficiência semelhante. Ele #
#     basicamente seleciona o menor valor da lista e insere-o no       #
#     inicio, depois o segundo menor e insere-o na segunda posição, e  #
#     assim sucessivamente até que todos os valores estejam em sua     #
#     determinada posição.                                             #
#======================================================================#

def selection_sort(lista):
    for i in range(len(lista)):
        n = i
        for j in range(i,len(lista)):
            if lista[j] < lista[n]:
                n = j
        lista[i], lista[n] = lista[n], lista[i]

#======================================================================#
# Quick Sort                                                           #
#     O algoritmo a seguir possui uma boa eficiência, no entanto, em   #
#     seu pior caso tem complexidade O(n^2). Ele funciona fazendo      #
#     sucessivos particionamentos com uso de recursão. O               #
#     particionamento basicamente pega um valor pivô e move todos      #
#     valores menores para trás dele e todos os maiores para depois,   #
#     dessa forma o pivô ficará posicionado corretamente. Já a recursão# 
#     atua fazendo sucessivos particionamentos nas sublistas antes e   #
#     depois de cada pivô particionado até chegar em sublistas com     #
#     menos que 2 elementos.                                           #
#======================================================================#

def quick_sort(lista):
    quick_sort_recursion(lista,0,len(lista)-1) 

def quick_sort_recursion(lista, low, high):
    if (low < high):
        p = partition(lista, low, high)
        quick_sort_recursion(lista, low, p - 1)
        quick_sort_recursion(lista, p + 1, high)

def partition(lista, low, high):
    pivot = lista[high]
    i = (low - 1) 
    for j in range(low,high):
        if (lista[j] <= pivot):
            i+= 1
            lista[i],lista[j] = lista[j],lista[i]
    lista[i+1],lista[high] = lista[high],lista[i+1]
    return i + 1


#======================================================================#
#         DEMONSTRAÇÃO                                                 #
#======================================================================#
# Abaixo você pode ver os algoritmos sendo utilizados e funcionando,   # 
# com um algoritmo simples de bônus caso tenha interesse.              #
#======================================================================#

def random_list(size,max_value):            #função auxiliar para
    temp = []                               #gerar listas com valores
    for i in range(size):                   #inteiros aleatórios.
        temp.append(random.randint(0,max_value))
    return temp

# Bubble Sort
print("Bubble Sort")
lista = random_list(10, 1000)     #cria lista aleatória
print(lista)                      #imprime não-ordenada
bubble_sort(lista)                #ordena
print(lista)                      #imprime ordenada

# Insertion Sort
print("\nInsertion Sort")
lista = random_list(10, 1000)     #cria lista aleatória
print(lista)                      #imprime não-ordenada
insertion_sort(lista)             #ordena
print(lista)                      #imprime ordenada

# Selection Sort
print("\nSelection Sort")
lista = random_list(10, 1000)     #cria lista aleatória
print(lista)                      #imprime não-ordenada
selection_sort(lista)             #ordena
print(lista)                      #imprime ordenada

# Quick Sort
print("\nQuick Sort")
lista = random_list(10, 1000)     #cria lista aleatória
print(lista)                      #imprime não-ordenada
quick_sort(lista)                 #ordena
print(lista)                      #imprime ordenada