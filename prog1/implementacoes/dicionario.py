# coding: utf-8

# EXEMPLO USUAL DA ESTRUTURA DICIONÁRIO
#
# O dicionário é uma coleção que serve
# para mapear pares de chave-valor. A
# chave pode ser qualquer tipo imutável,
# já o valor pode ser qualquer objeto de
# dados do Python.


professores = {}                                # Declara um dicionário professores
professores['prog1'] = 'Dalton'                 # Associa um nome à chave 'prog1'

professores = {'prog1': 'Dalton'}               # Declaração direta já fornecendo o par chave-valor anterior

# Iterando sobre os pares
# chave-valor do dicionario
# com a função items()
for chave, valor in professores.items():
    print "Chave:", chave                       # Imprime Chave: prog1
    print "Valor:", valor                       # Imprime Valor: Dalton

# Iterando somente sobre
# as chaves do dicionario
# com a função keys()
# OBS: é possível omitir a função
for chave in professores.keys():
    print "Chave:", chave                       # Imprime Chave: prog1
    print "Valor:", professores[chave]          # Imprime Valor: Dalton


professores['prog2'] = 'Gaudêncio'

# Iterando somente sobre
# os valores do dicionario
# com a função values()
for valor in professores.values():
    print "Valor:", valor                       # Imprime
                                                # Valor: Dalton
                                                # Valor: Gaudêncio

chaves = list(professores.keys())               # Cria uma lista com todas as chaves de professores e guarda em chaves
valores = list(professores.values())            # Cria uma lista com todos os valores de professores e guarda em valores

print chaves                                    # Imprime ['prog1', 'prog2']
print valores                                   # Imprime ['Dalton', 'Gaudêncio']

# Com a função get() é possível
# pegar o valor de uma chave
# especifica, passando a chave
# como parâmetro
# OBS: caso a chave não exista,
# é retornado None
professor_prog1 = professores.get('prog1')
professor_prog2 = professores.get('prog2')
professor_prog3 = professores.get('prog3')

print professor_prog1                           # Imprime Dalton
print professor_prog2                           # Imprime Gaudêncio
print professor_prog3                           # None

# É possível passar um segundo
# parâmetro para a função get()
# que é um valor alternativo para
# quando a chave não existe, ao
# invés de retornar None, retorna
# o valor do parâmetro
professor_prog3 = professores.get('prog3', 'Raquel')

print professor_prog3                           # Imprime Raquel
