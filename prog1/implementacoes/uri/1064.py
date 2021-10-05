cont = 0
som = 0
for c in range(0, 6):
    v = float(input())
    if v > 0:
        cont += 1
        som += v
if cont != 0:
    print('{} valores positivos\n{:.1f}'.format(cont, som/cont))

