# Pedro Donato Coêlho Neto
# -*- coding: utf-8 -*-

a,b,c,d = input().split()
a,b,c,d = float(a),float(b),float(c),float(d)

m = (a*2 + b*3 + c*4 + d)/10

if m >= 7:
    print("Media: %.1f" % (m))
    print("Aluno aprovado.")
elif m < 5:
    print("Media: %.1f" % (m))
    print("Aluno reprovado.")
elif 5 <= m <= 6.9:
    n = float(input())
    print("Media: %.1f" % (m))
    print("Aluno em exame.")
    print("Nota do exame: %.1f" % (n))
    nm = (n+m)/2
    if nm >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % (nm))
if med < 5:
    print('Aluno reprovado.')
if 5 <= med < 7:
    print('Aluno em exame.')
    ex = round(float(input()), ndigits=1)
    print('Nota do exame: {:.1f}'.format(ex))
    medf = (med+ex)/2
    if medf >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(medf))
