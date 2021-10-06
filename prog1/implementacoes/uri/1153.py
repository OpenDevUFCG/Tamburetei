# Questão 1153 - Fatorial Simples
# Link da questão - https://www.urionlinejudge.com.br/judge/pt/problems/view/1153

# Calculo de fatorial utilizando abordagem iterativa

n = int(input()) # Dado um numero da entrada...

fact = 1 # Iniciamos o valor do fatorial com 1, pois 0! = 1
for i in range(1, n+1): # Iteramos no intervalo de [1, n]...
    fact *= i # Multiplicando os valores de i uma a um

print(fact)

'''
Este problema também pode ser resolvido com o uso de recursão:

def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)

n = int(input())
print(fact(n))
'''