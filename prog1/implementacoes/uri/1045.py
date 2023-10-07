num = input().split()

for i in range(len(num)):
    for j in range(0, len(num) -1 -i):
        if float(num[j]) < float(num[j+1]):
            num[j], num[j+1] = num[j+1], num[j]

a, b ,c =  float(num[0]), float(num[1]), float(num[2])

if a >= b + c:
    print("NAO FORMA TRIANGULO")

else:

    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")
