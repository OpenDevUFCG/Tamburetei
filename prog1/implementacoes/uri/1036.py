# Pedro Donato Coêlho Neto
# -*- coding: utf-8 -*-

a,b,c = input().split()
a,b,c = float(a),float(b),float(c)

d = b*b - 4*a*c
if (a == 0) or (d<0):
    print("Impossivel calcular")
else:
    r1 = (-b + (d)**(1/2))/(2*a)
    r2 = (-b - (d)**(1/2))/(2*a)
    print("R1 = %.5f" % (r1))
    print("R2 = %.5f" % (r2))
