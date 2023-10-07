hora = input().split()
ini, fim = int(hora[0]), int(hora[1])
if ini < fim:
    print(f"O JOGO DUROU {fim-ini:.0f} HORA(S)")
else:
    print(f"O JOGO DUROU {(24-ini) + fim:.0f} HORA(S)")