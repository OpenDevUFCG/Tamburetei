# -*- coding: utf-8 -*-
N = int(input())
string = ''
lista = []
medias = []
for num in range(N):
    num = input().split(' ')
    lista = num
    for valor in range(2,len(lista)):
        media = ((float(lista[0]))*2) + ((float(lista[1]))*3) + ((float(lista[2]))*5)
        media_final = media/10
        medias.append(media_final)
for valor in medias:
    print('{:.1f}'.format(valor))
