dicio = dict()

try:
    nome = input()

    while True:
        dicio[(nome.upper())] = nome
        nome = input()
except:
    pass

chaves = list(dicio.keys())
chaves.sort()

print(dicio[chaves[-1]])