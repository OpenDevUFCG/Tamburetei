# Sistemas de Numeração
Conjunto de símbolos utilizados para representação de quantidades e de regras que definem a forma de apresentação. 

Cada sistema de numeração é apenas um método diferente para representar quantidades. _**As quantidades em si não mudam, apenas a forma de representá-las**_

| Sistema| Base | Algarismos | 
| ------ | ------ | ------ |
| Binário | 2 | 0,1 |
| Octal | 8 | 0,1,2,3,4,5,6,7|
| Decimal | 10 | 0,1,2,3,4,5,6,7,8,9|
| Hexadecimal | 16 | 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F |

Tabela Comparativa

| Decimal | Binário | Octal | Hexadecimal |
| ------ | ------ | ------ |------ |
| 0 | 0000        | 0 |     0 |
| 1 | 0001      | 1|     1 |
| 2 | 0010       | 2|   2 |
| 3 | 0011       | 3 |  3 |
| 4 | 0100       | 4 |  4 |
| 5 | 0101       | 5 |  5 |
| 6 | 0110       | 6 |  6 |
| 7 | 0111       | 7 |  7 |
| 8 | 1000       | 10 |  8 |
| 9 | 1001       | 11 |  9 |
| 10 | 1010       | 12 |  A |
| 11 | 1011       | 13 |  B |
|12 |  1100       | 14 |  C |
| 13 | 1101       | 15 |  D |
| 14 | 1110       | 16 |  E |
| 15 | 1111       | 17 |  F |


## Conversão entre Sistemas de Numeração

### Decimal para Qualquer base númerica :

  - Para realizar a conversão de decimal para binário, realiza-se a _**divisão sucessiva pela base de destino**_ (_Ex: se for hexadecimal, deve-se dividir por 16_). O resultado da conversão será dado pelo último quociente (MSB) e o agrupamento dos restos de divisão será o número na base de destino.
  Por exemplo, vamos converter o número 45 em binário:

![Imagem 1](https://www.embarcados.com.br/wp-content/uploads/2016/07/decimal-bin%C3%A1rio.jpg)

A leitura do resultado é feita do último quociente para o primeiro resto. Sendo assim, o resultado da conversão do número 45 para binário é: **101101**(2).

Exemplo 2 : 
Decimal para Hexadecimal 

![Imagem 2](http://www.mecaweb.com.br/eletronica/content/image/conv_dh_2.png)


## Outro sistema  ->   Decimal :

- Deve-se utilizar notação polinomial

  ![Imagem 3](https://image.slidesharecdn.com/03stcunidadesdeinformacaosistemasnumericos-150303110419-conversion-gate01/95/unidades-de-informacao-sistemas-numericos-39-638.jpg?cb=1425402323)
  
- Exemplo : 
  ![Imagem 4](https://rvalentim.files.wordpress.com/2010/01/hexadec-decimal.jpg)


## Octal / Hexadecimal para Binário (e vice-versa): 

  - Deve-se utilizar **Agrupamento de Bits**
Associar 3 bits ou 4 bits (quando octal ou hexadecimal, respectivamente) e vice-versa.

- Exemplo 1: 

![Imagem 5](http://mundoprojetado.com.br/wp-content/uploads/2019/01/Conversao-de-octal-hexa-para-binario.png)

- Exemplo 2 (Binario para Octal / Hexadecimal):

![Imagem 6](http://mundoprojetado.com.br/wp-content/uploads/2019/01/Conversao-de-bin%C3%A1rio-em-octal-hexa.png)

## Octal para Hexadecimal (e vice-versa):
- A conversão não é realizada diretamente, **requer o uso de uma base intermediária (base binária)**

- _**1 ° Etapa**_ : Converter o número na base octal (hexadecimal) para binário
- _**2 ° Etapa**_ : Converter o resultado binṕario em hexadecimal (octal).
Exemplo : 
(**175**) 8 = (**?**) 16
(**175**) _8_ = (**1111101**) _2_ =  (**7D**) _16_  
