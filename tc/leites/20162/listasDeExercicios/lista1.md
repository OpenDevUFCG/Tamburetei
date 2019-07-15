# Lista de Exercícios 1

- **Disciplina:** Teoria da Computação
- **Período:** 2016.2

## Questões

#### Questão 1 

Construa um autômato finito determinístico (AFD), cujo alfabeto é **Σ =** *{a, b}*, que aceita qualquer palavra que tenha `bbaba` como sub-cadeia.

#### Questão 2 

Dê o diagrama de estados dos autômatos finitos não-determinísticos que reconhecem a estrela das seguintes linguagens:

**a)** **L1 =** *{w| w contém pelo menos três 1s}*

**b)** **L2 =** *{w| w contém pelo menos dois 0s e no máximo um 1}*

#### Questão 3

Prove que todo AFND com mais de um estado de aceitação pode ser convertido para um outro AFND equivalente que tem um único estado de aceitação.

#### Questão 4

Construa um autômato que reconhece números binários que são múltiplos de 3. **Exemplo:** a palavra `100` que representa o número decimal 4 não é aceita pelo AFD, enquanto que palavras como `011` e `0110` (representações binárias dos números decimais 3 e 6, respectivamente) são aceitas pelo AFD.

#### Questão 5

Com base no procedimento para a união de autômatos finitos determinísticos, mostre como seria o procedimento para fazer o autômato que reconhece a diferença de duas linguagens (A - B), nas seguintes situações:

**a)** O alfabeto da linguagem A é menor que o alfabeto da linguagem B (pode assumir que **ΣA =** *{0,1}* e **ΣB =** *{0,1,2}*).

**b)** O alfabeto da linguagem A é maior que o alfabeto da linguagem B (pode assumir que **ΣA =** *{0,1,2}* e **ΣB =** *{0,1}*).
