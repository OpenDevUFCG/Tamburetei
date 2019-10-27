# coding: utf-8
# URI 1151
# Fibonacci Fácil

def fibonacci_facil(num):
	valores = [0, 1]
	for i in range(2,num):
		valores.append(valores[i - 1] + valores[i - 2])
	string = "0 1"
	for i in range(2, num):
		string += " " + str(valores[i])
	return string

print(fibonacci_facil(int(input())))
