# Questão 1044 - Múltiplos
# Link da questão - https://www.beecrowd.com.br/judge/pt/problems/view/1044

a, b = map(float, input().split())
if a % b == 0 or b % a == 0:
	print ("Sao Multiplos")
else:
	print ("Nao sao Multiplos")