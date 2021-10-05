# -*- coding: utf-8 -*-

dinheiro = int(float(input()) * 100)

notas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
resposta = [0,0,0,0,0,0,0,0,0,0,0,0]


for nota in range(len(notas)):
	while dinheiro >= notas[nota]:
		dinheiro -= notas[nota]
		resposta[nota] += 1

print ("NOTAS:")
print ("%d nota(s) de R$ 100.00" % (resposta[0]))
print ("%d nota(s) de R$ 50.00" % (resposta[1]))
print ("%d nota(s) de R$ 20.00" % (resposta[2]))
print ("%d nota(s) de R$ 10.00" % (resposta[3]))
print ("%d nota(s) de R$ 5.00" % (resposta[4]))
print ("%d nota(s) de R$ 2.00" % (resposta[5]))
print ("MOEDAS:")
print ("%d moeda(s) de R$ 1.00" % (resposta[6]))
print ("%d moeda(s) de R$ 0.50" % (resposta[7]))
print ("%d moeda(s) de R$ 0.25" % (resposta[8]))
print ("%d moeda(s) de R$ 0.10" % (resposta[9]))
print ("%d moeda(s) de R$ 0.05" % (resposta[10]))
print ("%d moeda(s) de R$ 0.01" % (resposta[11]))
