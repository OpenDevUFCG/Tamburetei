# coding: utf-8

# SOMAR DIAGONAL PRINCIPAL DE UMA MATRIZ
#
# Na cadeira de Programação 1,
# mais especificamente na unidade 9,
# são estudadas as Matrizes.
# Existem diversas formas de
# representar uma matriz no Python,
# mas a unidade é trabalhada com a
# representação em lista de listas.
#
# Uma lista de listas nada mais é do
# que uma lista que contém outras
# listas como elementos.

matriz = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]          # A lista matriz contém três listas de tamanhos iguais.

# Uma observação importante é que
# toda matriz na unidade 9 é uma
# lista de listas, mas nem toda
# lista de listas é uma matriz. Um
# exemplo pode ser visto abaixo.

nao_eh_matriz = [[1, 2, 3],
                 [4, 5, 6, 7, 8, 9]]     # A lista nao_eh_matriz contém duas listas de tamanhos diferentes.

# Para operar uma lista de listas
# o mais comum é utilizar duas
# estruturas de iteração.

linhas = len(matriz)                                # Guarda o comprimento da matriz (quantidade de linhas)
colunas = len(matriz[0])                            # Guarda o comprimento da primeira lista da matriz (quantidade de colunas)

soma_diagonal_principal = 0                         # Declara uma variável para somar a diagonal principal da matriz
for linha in range(linhas):
    for coluna in range(colunas):
        if linha == coluna:                         # Se o indice da linha for igual ao da coluna, soma o número
            soma_diagonal_principal += matriz[linha][coluna]

print (soma_diagonal_principal)                       # Imprime a soma total da diagonal principal: 0 + 4 + 8 = 12
