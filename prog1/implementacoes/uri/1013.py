v = input().split()
a, b, c = v
m = (int(a) + int(b) + abs(int(a) - int(b)))/2
maior = (int(m) + int(c) + abs(int(m) - int(c)))/2
print(int(maior), 'eh o maior')

