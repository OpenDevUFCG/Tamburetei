def checa_paridade_par(bits):
    
    quantidade_uns = bits.count("1")
    bit_paridade = ""
            
    if quantidade_uns % 2 == 0:
        bit_paridade = '0'
    else: 
        bit_paridade = '1'
        
    return bit_paridade


def verifica_paridade(bits):
    
    bit_paridade = bits[0]
    dados = bits[1:]
    paridade = True
    
    paridade_calculada = checa_paridade_par(dados)
    
    if(paridade_calculada != bit_paridade):
        paridade = False
        
    return paridade
    

bits_originais = input("Digite bit a bit, sem separá-los por espaços: ")
bit_paridade = checa_paridade_par(bits_originais)
dados_transmitidos = bit_paridade + bits_originais

print(f"Dados transmitidos: {dados_transmitidos}\n")

bits_corrompidos = input("Digite bit a bit, os dados supostamente corrompidos: ")
verificacao = verifica_paridade(bits_corrompidos)

if(verificacao):
    print(f"Não foi detectado erro de paridade.")
else:
    print(f"Erro de paridade detectado, os dados são incompatíveis.")

    
# Exemplo1:
#
# bits_originais = "101010"  
# bit_paridade = "1"
# Dados transmitidos: 1101010
# bits_corrompidos = "101010"
#
# Saída: "Não foi detectado erro de paridade."

# Exemplo2:
#
# bits_originais = "110011"  
# bit_paridade = "0"
# Dados transmitidos: 0110011
# bits_corrompidos = "0110010"
#
# Saída: "Erro de paridade detectado, os dados são incompatíveis."