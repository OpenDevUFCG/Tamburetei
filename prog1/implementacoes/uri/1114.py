correta = False # Flag que indica se a senha indicada foi a correta

while not correta:
    senha = str(input()) # Pega a senha da entrada
    if senha != '2002':
        print('Senha Invalida') # Se a senha difere da real
    else:
        print('Acesso Permitido') # Se a senha é correta
        correta = True # Mudamos o valor da flag para parar o loop
    