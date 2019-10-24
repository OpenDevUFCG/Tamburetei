# coding: utf-8
# URI 1048
# Aumento de Salário

def reajuste(salario):
	if (salario <= 400.0):
		novo_salario = salario + salario * 0.15
		reajuste = novo_salario - salario
		percentual = 15
	elif (salario > 400.0 and salario <= 800.0):
		novo_salario = salario + salario * 0.12
		reajuste = novo_salario - salario
		percentual = 12
	elif (salario > 800.0 and salario <= 1200.0):
		novo_salario = salario + salario * 0.1
		reajuste = novo_salario - salario
		percentual = 10
	elif (salario > 1200.0 and salario <= 2000.0):
		novo_salario = salario + salario * 0.07
		reajuste = novo_salario - salario
		percentual = 7
	else:
		novo_salario = salario + salario * 0.04
		reajuste = novo_salario - salario
		percentual = 4

	return "Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: %i %%" %(novo_salario, reajuste, percentual)


print reajuste(float(raw_input()))