# Questão 1060 - Números Positivos
# Link da questão - https://www.beecrowd.com.br/judge/pt/problems/view/1060

y = 0
for x in range(1,7):
    a = float(input())
    if a > 0:
        y = y + 1
print('{} valores positivos'.format(y))