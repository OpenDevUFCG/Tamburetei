# coding: utf-8
# URI 1144
# Sequência Lógica

def sequencia(num):
	matriz = []
	for i in range(num * 2):
		matriz.append([])
		for j in range(3):
			matriz[i].append([])

	for j in range(3):
		if j == 0:
			contador = 1
			for i in range(0, num * 2 - 1, 2):
				matriz[i][j], matriz[i + 1][j] = contador, contador
				contador += 1
		if j == 1:
			contador = 1
			for i in range(0, num * 2 - 1, 2):
				matriz[i][j], matriz[i + 1][j] = contador ** 2, contador ** 2 + 1
				contador += 1
		if j == 2:
			contador = 1
			for i in range(0, num * 2 - 1, 2):
				matriz[i][j], matriz[i + 1][j] = contador ** 3, contador ** 3 + 1
				contador += 1

	string = ""			
	for i in range(num * 2):
		for j in range(3):
			if j == 2 and i == num * 2 - 1:
				string += str(matriz[i][j])
			elif j == 2:
				string += str(matriz[i][j]) + "\n"
			else:
				string += str(matriz[i][j]) + " "


	return string


print sequencia(int(raw_input()))