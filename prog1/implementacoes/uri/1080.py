mai = men = x = 0
lista = list()
for c in range(0, 100):
    v = int(input())
    lista.append(v)
    if c == 0:
        mai = v
        men = v
    else:
        if v < men:
            men = v
        if v > mai:
            mai = v
            x = lista.index(v) + 1
print(mai)
print(x)

