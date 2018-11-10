# coding: utf-8

# FUNÇÕES ÚTEIS
#
# Na disciplina de Programação 1, existem algumas funções de Python
# cuja utilização direta é proibida. Entretanto, é permitido ao aluno
# que implemente sua própria versão dessas funções e utilize-as. Abaixo
# você encontrará algumas dessas implementações úteis.

def my_split(text, delimiter = ' '):
    """ Particiona uma string a cada ocorrência do delimitador.

    Considerando a string e o delimitador passados como parâmetro, cada
    ocorrência do delimitador gera um novo particionamento da string. As
    partições são armazenadas numa lista que será retornada. O espaço em
    branco (' ') é o delimitador padrão.

    Parameters
    ----------
    text : str
        A string a ser particionada
    delimiter : str, optional
        O delimitador das partições geradas (default ' ')
    
    Return
    ------
    splitted : list
        Lista contendo as partições geradas pelo algoritmo
    """
    splitted = []
    partition = ''
    
    for i in range(len(text)):
        if (text[i] == delimiter):
            if (partition != ''):
                splitted.append(partition)
                partition = ''
        else:
            partition += text[i]
    
    if (len(partition) > 0):
        splitted.append(partition)
    
    return splitted

def my_sum(values):
    """ Soma os elementos de uma lista.

    Soma os valores contidos em uma lista e retorna o resultado da soma.
    O retorno dessa função pode ser do tipo int ou float, de acordo com
    os valores contidos na lista a ser somada.

    Parameters
    ----------
    values : list
        A lista cujos elementos serão somados
    
    Return
    ------
    result : int | float
        Resultado da soma dos elementos da lista
    """
    result = 0
    for i in range(0, len(values)):
        result += values[i]

    return result

def my_insert(values, element, index = 0):
    """ Insere um elemento num índice específico de uma lista.

    Considerando o elemento, o índice e a lista recebidos como parâme-
    tros, insere tal elemento no índice especificado da lista sem que
    haja sobrescrita do elemento previamente armazenado neste índice.
    Por padrão, a inserção será realizada no início da lista.

    Parameters
    ----------
    values : list
        A lista em que a inserção será realizada
    element : ?
        O elemento a ser inserido na lista
    index : int
        O índice em que a inserção será realizada (default 0)
    """
    values.append(element)
    for i in range(len(values) - 1, index, -1):
        values[i], values[i - 1] = values[i - 1], values[i]

def my_reverse(values):
    """ Inverte a ordenação atual dos elementos em uma lista.

    Considerando a lista recebida como parâmetro, inverte a ordenação
    atual dos elementos nela contida. Desse modo, o último elemento tor-
    na-se o primeiro, o penúltimo torna-se o segundo e, assim, sucessi-
    vamente. Essa função modificará diretamente a lista.

    Parameters
    ----------
    values : list
        A lista cuja ordenação de elementos será invertida
    """
    for i in range(len(values) / 2):
        copy = values[i]
        values[i] = values[len(values)-1 - i] 
        values[len(values)-1 - i] = copy

def my_max(values):
    """ Retorna o elemento máximo de uma lista.

    Considerando a lista recebida como parâmetro, identifica e retorna
    o elemento máximo nela contido.

    Parameters
    ----------
    values : list
        A lista cujo elemento máximo deve ser identificado
    
    Return
    ------
    maximum : ?
        O elemento máximo da lista
    """
    maximum = values[0]
    for i in values:
        if (i > maximum):
            maximum = i
    return maximum

def my_min(values):
    """ Retorna o elemento mínimo de uma lista.

    Considerando a lista recebida como parâmetro, identifica e retorna
    o elemento mínimo nela contido.

    Parameters
    ----------
    values : list
        A lista cujo elemento mínimo deve ser identificado
    
    Return
    ------
    minimum : ?
        O elemento mínimo da lista
    """
    minimum = values[0]
    for i in values:
        if (i < minimum):
            minimum = i
    return minimum


# DEMONSTRAÇÃO
#
# O código abaixo pode ser executado para observação do funcionamento
# das funções implementadas anteriormente.

print my_split(' part1 part2 part3     part4   part5 part6 part7  ')

print my_split('00/00/0000', '/')

print my_sum([1, 2, 3, 4])

digits = [1, 2, 3, 4, 6, 7, 8, 9]
my_insert(digits, 5, 4)
print digits
my_insert(digits, 0)
print digits

my_reverse(digits)
print digits
my_reverse(digits)
print digits

values = [3, 7, 7, 5, 4, 6, 2, 1]
print my_max(values)
print my_min(values)