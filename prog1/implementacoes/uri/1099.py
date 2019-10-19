# -*- coding: utf-8 -*-

n = int(input())

soma_lista = []
for num in range(n):
    num = input().split()
    for i in range(len(num)):
        a = int(num[0])
        b = int(num[1])
        soma = 0
        if a >= b:        
            for i in range(b+1,a):
                if i % 2 == 1 and i > 0:
                    soma += i
        if b >= a:
            for i in range(a+1,b):
                if i % 2 == 1 and i > 0:
                    soma += i
    soma_lista.append(soma)
                    
for i in range(len(soma_lista)):
    print(soma_lista[i])
