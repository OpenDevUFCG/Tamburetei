# -*- coding: utf-8 -*-
a = int(input())
b = a/100
c = (a%100)/50
d = ((a%100)%50)/20
e = (((a%100)%50)%20)/10
f = ((((a%100)%50)%20)%10)/5
g = (((((a%100)%50)%20)%10)%5)/2
h = (((((a%100)%50)%20)%10)%5)%2

print a
print b, 'nota(s) de R$ 100,00'
print c, 'nota(s) de R$ 50,00'
print d, 'nota(s) de R$ 20,00'
print e, 'nota(s) de R$ 10,00'
print f, 'nota(s) de R$ 5,00'
print g, 'nota(s) de R$ 2,00'
print h, 'nota(s) de R$ 1,00'
