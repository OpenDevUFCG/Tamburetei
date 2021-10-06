# Questão 1159 - Soma de Pares Consecutivos
# Link da questão - https://www.urionlinejudge.com.br/judge/pt/problems/view/1159

eh_zero = True # Flag para indicar se o ultimo numero encontrado é zero

while eh_par: # Enquanto encontrar numeros pares...
    numero = int(input()) # Pega um numero da entrada
    if numero != 0: # Se o numero é
        soma = 0
        for i in range(numero, numero+10): # Soma todos os números pares entre n e n+10
            if i % 2 == 0:
                soma += i
        print(soma)
    else:
        eh_zero = False # Caso seja zero, o loop deve parar

# Somamos dentro do intervalo determinado pelo for (entre n e n+10), pois queremos
# encontrar os 5 proximos numeros pares depois da nossa entrada, assim, como numeros
# pares alternam dois a dois em uma sequencia ordenada, temos a certeza de que em um
# intervalo de 10 numeros teremos exatamente 5 pares.