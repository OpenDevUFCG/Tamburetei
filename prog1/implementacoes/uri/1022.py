def operacao(num1, dig1, opt, num2, dig2):
    if opt == '+':
        num = (num1 * dig2) + (num2 * dig1)
        dem = dig1 * dig2

    if opt == '-':
        num = (num1 * dig2) - (num2 * dig1)
        dem = dig1 * dig2

    if opt == '*':
        num = num1 * num2
        dem = dig1 * dig2

    if opt == '/':
        num = num1 * dig2
        dem = num2 * dig1

    return num, dem

def fatoramento(a, b):
    abs_a, abs_b = abs(a), abs(b)
    men = min(abs_a, abs_b)
    mai = max(abs_a, abs_b)
    divisor = men
    while divisor > 1:
        if (men % divisor) == 0:
            if (mai % divisor) == 0:
                return int(a/divisor), int(b/divisor)
        divisor -= 1
    return a, b


var = int(input())

for x in range(0, var):
    operacoes = input().strip().split(' ')
    n1, d1, op, n2, d2 = int(operacoes[0]), int(operacoes[2]), operacoes[3], int(operacoes[4]), int(operacoes[6])
    num, dem = operacao(n1, d1, op, n2, d2)
    simp_num, simp_dem = fatoramento(num, dem)
    print(f'{num}/{dem} = {simp_num}/{simp_dem}')
