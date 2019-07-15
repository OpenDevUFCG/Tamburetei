# Lista de Exercícios 3

- **Disciplina:** Teoria da Computação
- **Período:** 2017.1

## Questões

#### Questão 1 

Prove que as linguagens abaixo são decidíveis:

- **L1 =** *{<R, w> | R é uma expressão regular que gera a cadeia w}*
- **L2 =** *{<G> | G é uma Gramática Livre de Contexto e L(G) = ∅}*

#### Questão 2

Considere as linguagens L1 e L2 sendo linguagens reconhecíveis e as linguagens L3 e L4 sendo decidíveis. Informe se a linguagem resultante a cada operação abaixo é reconhecível ou decidível. Justifique.

**a)** `L1 ∩ L2`

**b)** `L1 ∩ L3`

**c)** `L3 ∪ L4`

**d)** `L1 ∪ L3`

**e)** `(L1 ∩ L2) ∪ L3`

**f)** `(L1 ∩ L3) ∪ Complemento(L3)`

#### Questão 3

Avalie as afirmações em verdadeiro ou falso, justificando as afirmações falsas.

**a)** ( ) Sendo as linguagens L1, L2 e L3 linguagens regulares ou livre-de-contexto, não é possível categorizá-las como decidíveis ou reconhecíveis apenas com estas informações.

**b)** ( ) A possibilidade de criação de um enumerador para uma linguagem nada implica sobre sua reconhecibilidade ou decidibilidade.

**c)** ( ) É possível criar uma máquina de Turing para qualquer linguagem livre-de-contexto ou regular.

**d)** ( ) Uma máquina de Turing multifita reconhece uma classe de linguagens maior do que uma máquina de Turing de uma fita só.

#### Questão 4

Prove que a linguagem **L =** *{<M1,M2> | M1 e M2 são máquinas de Turing e L(M1) = L(M2)}* é indecidível.
