# -*- coding: utf-8 -*-
#Teste de Seleção 1

valores = input()
valores = valores.split()


c1 = int(valores[1]) > int(valores[2])
c2 = int(valores[3]) > int(valores[0])
c3 = int(valores[2]) + int(valores[3]) > int(valores[0]) + int(valores[1])
c4 = int(valores[2]) > 0
c5 = int(valores[3]) > 0 
c6 = int(valores[0]) / 2 == int(valores[0]) //2

if c1 and c2 and c3 and c4 and c5 and c6:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
