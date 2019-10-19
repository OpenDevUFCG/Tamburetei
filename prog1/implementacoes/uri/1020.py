n = int(input())

anos = n // 365
meses = (n % 365) // 30
dias = (n % 365)%30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
