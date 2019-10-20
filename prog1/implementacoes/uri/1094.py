# -*- coding: utf-8 -*-
N = int(input())
total = 0
coelhos = 0
ratos = 0
sapos = 0
for valor in range(N):
    valor = input().split()
    if valor[1] == 'C':
        coelhos += int(valor[0])
        total += int(valor[0])
    if valor[1] == 'S':
        sapos += int(valor[0])
        total += int(valor[0])
    if valor[1] == 'R':
        ratos += int(valor[0])
        total += int(valor[0])  
perc_coelhos = coelhos * 100 / total
perc_ratos = ratos * 100 / total
perc_sapos = sapos * 100 / total      
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(perc_coelhos))
print('Percentual de ratos: {:.2f} %'.format(perc_ratos))
print('Percentual de sapos: {:.2f} %'.format(perc_sapos))
