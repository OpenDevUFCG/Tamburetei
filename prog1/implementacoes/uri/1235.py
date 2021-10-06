# Questão 1235 - De Dentro para Fora
# Link da questão - https://www.urionlinejudge.com.br/judge/pt/problems/view/1235

n = int(input())

lista = list()

for c in range(0, n):
    palavra = str(input())

if len(palavra) % 2 == 0:
        palavra1 = palavra[:int(len(palavra)/2)]
        palavra_1 = palavra1[::-1]
        palavra2 = palavra[int(len(palavra)/2):]
        palavra_2 = palavra2[::-1]
        palavra0 = palavra_1 + palavra_2
        lista.append(palavra0)

for k in lista:
    print(k)
