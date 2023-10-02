def calcular_paridade(bits):
    paridade = [0, 0, 0]
    paridade[0] = bits[0] ^ bits[1] ^ bits[3]
    paridade[1] = bits[0] ^ bits[2] ^ bits[3]
    paridade[2] = bits[1] ^ bits[2] ^ bits[3]
    return paridade


def adicionar_paridade(bits):
    if len(bits) != 4:
        raise ValueError("Apenas sequências de 4 bits são suportadas.")
    
    paridade = calcular_paridade(bits)
    bits_com_paridade = bits + paridade
    return bits_com_paridade


def corrigir_erro(bits_com_paridade):
    if len(bits_com_paridade) != 7:
        raise ValueError("Apenas sequências de 7 bits com paridade são suportadas.")
    
    paridade_calculada = calcular_paridade(bits_com_paridade[:-3])
    paridade_recebida = bits_com_paridade[-3:]
    erro = 0
    
    for i in range(3):
        if paridade_calculada[i] != paridade_recebida[i]:
            erro += 2 ** i

    if erro != 0:
        bits_com_paridade[erro - 1] = 1 - bits_com_paridade[erro - 1]
        
    return bits_com_paridade[:-3]


# Solicita que o usuário insira os bits de dados originais
bits_originais = []
for i in range(4):
    bit = int(input(f"Digite o bit {i + 1} (0 ou 1): "))
    bits_originais.append(bit)

bits_com_paridade = adicionar_paridade(bits_originais)  # Adiciona bits de paridade (7 bits)
print(f"\nBits originais:, {bits_originais}")
print(f"Bits com paridade:, {bits_com_paridade}\n")

# Solicitar que o usuário introduza um erro opcionalmente
introduzir_erro = input("Deseja introduzir um erro nos bits? (S/N): ")
if introduzir_erro.upper() == 'S':
    erro_bit = int(input("Digite o índice do bit a ser alterado (0 a 6): "))
    bits_com_erro = bits_com_paridade.copy()
    bits_com_erro[erro_bit] = 1 - bits_com_erro[erro_bit]

    bits_corrigidos = corrigir_erro(bits_com_erro)
    print("Bits com erro:", bits_com_erro)
    print("Bits corrigidos:", bits_corrigidos)
else:
    print("Nenhum erro foi introduzido.")


# Exemplo1:
#
# bits_originais = [1, 0, 1, 1]  # Bits de dados originais (4 bits)
# bits_com_paridade = adicionar_paridade(bits_originais)  # Adiciona bits de paridade (7 bits)
# print("Bits originais:", bits_originais)
# print("Bits com paridade:", bits_com_paridade)
#
# Saída:
# Bits originais: [1, 0, 1, 1]
# Bits com paridade: [1, 0, 1, 1, 0, 0, 0]
#
# bits_corrigidos = corrigir_erro(bits_com_paridade)
# print("Bits com erro:", bits_com_paridade)
# print("Bits corrigidos:", bits_corrigidos)
#
# Saída :
# Bits com erro: [1, 0, 1, 1, 0, 0, 0]
# Bits corrigidos: [1, 0, 1, 1]

# Exemplo2:
#
# bits_originais = [0, 1, 1, 0]  # Bits de dados originais (4 bits)
# bits_com_paridade = adicionar_paridade(bits_originais)  # Adiciona bits de paridade (7 bits)
# print("Bits originais:", bits_originais)
# print("Bits com paridade:", bits_com_paridade)
# 
# Saída:
# Bits originais: [0, 1, 1, 0]
# Bits com paridade: [0, 1, 1, 0, 1, 1, 0]
# 
# bits_com_erro = bits_com_paridade.copy()
# bits_com_erro[3] = 1 - bits_com_erro[3]  # Introduz erro nos bits
# 
# bits_corrigidos = corrigir_erro(bits_com_erro)
# print("Bits com erro:", bits_com_erro)
# print("Bits corrigidos:", bits_corrigidos)
# Saída:
# Bits com erro: [0, 1, 1, 1, 1, 1, 0]
# Bits corrigidos: [0, 1, 1, 0]
