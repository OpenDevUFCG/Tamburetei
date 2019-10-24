# Pedro Donato Coêlho Neto
# -*- coding: utf-8 -*-

c = {'1':"4.00",'2':'4.50','3':'5.00','4':'2.00','5':'1.50'}
l = input().split()
print("Total: R$ %.2f" % (float(c[l[0]])*int(l[1])))
