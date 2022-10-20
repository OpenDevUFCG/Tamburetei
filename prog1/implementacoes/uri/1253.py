n = int(input())

for i in range(n):
    palavra = input()
    deslocamento = int(input())

    resultado = ""

    for letra in palavra:
        
        letra_deslocada = ord(letra) - deslocamento
    
        if letra_deslocada not in range(ord('A'), ord('Z') + 1):
            letra_deslocada = ord('Z') - abs(ord(letra) - ord('A') - deslocamento) + 1

        resultado += chr(letra_deslocada)

    print(resultado)
        