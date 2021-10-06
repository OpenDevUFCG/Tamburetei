# Questão 1114 - Senha fixa
# Link da questão - https://www.urionlinejudge.com.br/judge/pt/problems/view/1114

correta = False # Flag que indica se a senha indicada foi a correta

while not correta:
    senha = str(input()) # Pega a senha da entrada
    if senha != '2002':
        print('Senha Invalida') # Se a senha difere da real
    else:
        print('Acesso Permitido') # Se a senha é correta
        correta = True # Mudamos o valor da flag para parar o loop
    