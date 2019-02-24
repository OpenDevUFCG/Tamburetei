#coding: utf-8

from buscaBinariaIterativa import buscaBinariaIterativa
from buscaBinariaRecursiva import buscaBinariaRecursiva

# array ordenado
array = ['amanda', 'ana', 'carlos', 'gabriela', 'luana', 'lucas', 'marcos', 'pedro', 'stephanne', 'victor', 'vinicius']

# testando a busca binária iterativa
assert "stephanne" == buscaBinariaIterativa('stephanne', array)
assert "vinicius" == buscaBinariaIterativa('vinicius', array)
assert "ana" == buscaBinariaIterativa('ana', array)
assert "gabriela" == buscaBinariaIterativa('gabriela', array)
assert "lucas" == buscaBinariaIterativa('lucas', array)
assert "marcos" == buscaBinariaIterativa('marcos', array)
assert "victor" == buscaBinariaIterativa('victor', array)
assert "amanda" == buscaBinariaIterativa('amanda', array)

# testando a busca binária recursiva
assert "stephanne" == buscaBinariaRecursiva('stephanne', array)
assert "vinicius" == buscaBinariaRecursiva('vinicius', array)
assert "ana" == buscaBinariaRecursiva('ana', array)
assert "gabriela" == buscaBinariaRecursiva('gabriela', array)
assert "lucas" == buscaBinariaRecursiva('lucas', array)
assert "marcos" == buscaBinariaRecursiva('marcos', array)
assert "victor" == buscaBinariaRecursiva('victor', array)
assert "amanda" == buscaBinariaRecursiva('amanda', array)