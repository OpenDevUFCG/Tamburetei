# Questão 1026 - Carrega ou não Carrega?
# Link da questão - https://www.beecrowd.com.br/judge/pt/problems/view/1026

while True:
    try:
        a, b = [int(x) for x in input().strip().split(' ')]
        print(a ^ b)
    except EOFError:
        break