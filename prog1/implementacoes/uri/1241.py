# Questão 1241 - Encaixa ou Não II
# Link da questão - https://www.urionlinejudge.com.br/judge/pt/problems/view/1241

n = int(input())

for i in range(n):
    n1, n2 = input().split()
    tamanho_n1 = len(n1)
    tamanho_n2 = len(n2)
    if tamanho_n1 >= tamanho_n2:
        if n1[-tamanho_n2:tamanho_n1] == n2:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
