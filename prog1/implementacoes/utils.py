# coding: utf-8

#======================================================================#
# Funçõe Úteis                                                         #
#======================================================================#
# Abaixo existem algumas funções já presentes em python que na         #
# disciplina você geralmente precisará implementar asua própria, pois  #
# a utilização das mesmas resultará em impugnação.                     #
#======================================================================#
#         IMPLEMENTAÇÕES                                               #
#======================================================================#
# mySplit                                                              #
#     Em algumas questões da disciplina você irá precisar separar uma  #
#     string em varias sub-strings que são armazenadas em uma lista.   #
#     infelizmente a função .split() padrão do python só pode ser      #
#     usado quando se trata de entrada.                                #
#     O mySplit irá percorrer a string s, e particioná-la toda vez que #
#     encontrar a string key, que por padrão será um espaço.           #
#======================================================================#

def mySplit(s, key=' '):
    result = []
    temp = ''
    for i in range(len(s)):
        if s[i] == key and len(temp) > 0:
            result.append(temp)
            temp = ''
        elif s[i] != key:
            temp += s[i]
    if len(temp) > 0:
        result.append(temp)
    return result

#======================================================================#
# mySum                                                                #
#     A função sum() simplesmente soma todos os valores de uma lista,  #
#     podendo também adicionar um valor opcional a tal soma.           #
#     (parâmetro start)                                                #
#======================================================================#

def mySum(l, start=0):
    end = start
    for i in l:
        end += i
    return end

#======================================================================#
# myInsert                                                             #
#     A função .insert() de python insere um valor a uma lista em um   #
#     determinado indice sem sobescrever o item que existia            #
#     previamente neste índice.                                        #
#======================================================================#

def myInsert(l, index, value):
    for i in range(index, len(l)):
        value, l[i] = l[i], value
    l.append(value)

#======================================================================#
# myReverse                                                            #
#     A função .reverse() inverte os valores de uma lista.             #
#======================================================================#

def myReverse(l):
    for i in range(len(l)/2):
        l[i], l[-i-1] = l[-i-1], l[i]

#======================================================================#
#         DEMONSTRAÇÃO                                                 #
#======================================================================#
# Abaixo você pode ver as funções sendo utilizadas.                    #
#======================================================================#

print(mySplit(' um ninho de     mafagafos   tem vinte mafagafinhos  '))
# saida:
# ['um', 'ninho', 'de', 'mafagafos', 'tem', 'vinte', 'mafagafinhos']

print(mySplit('16/11/2077','/'))
# saida: ['16', '11', '2077']

print(mySum([1, 1, 1, 1, 1]))
# saida: 5

print(mySum([1, 1, 1, 1, 1], 5))
# saida: 10

lista = ['um', 'dois', 'tres', 'quatro', 'cinco']
myInsert(lista, 2, 'NAO_SEI_CONTAR')
print(lista)
# saida: ['um', 'dois', 'NAO_SEI_CONTAR', 'tres', 'quatro', 'cinco']

lista = ['um', 'dois', 'tres', 'quatro', 'cinco']
myReverse(lista)
print(lista)
# saida: ['cinco', 'quatro', 'tres', 'dois', 'um']