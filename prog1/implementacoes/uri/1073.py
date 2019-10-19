# -*- coding: utf-8 -*-
N = int(input())
pares = []

for valor in range(N+1):
    if valor % 2 == 0:
        pares.append(valor)
for valor in pares:
    if valor != 0:
        a = valor**2
        print('{}^2 = {}'.format(valor,a))
