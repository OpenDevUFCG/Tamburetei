# Fundamentos de Matemática para Ciência da Computação I 1
## Lógica

### Sumário
 - [Lógica Proposicional](#lógica-proposicional)
 - [Conectivos Lógicos](#conectivos-lógicos)
 - [Tabelas-Verdade](#tabelas-verdade)
 - [Definições Importantes](#definições-importantes)
 - [Lógica de Predicados](#lógica-de-predicados)


### Lógica Proposional
#### Proposição:
    Toda sentença afirmativa que pode ser classificada em verdadeiro ou falso.
      -  SIMPLES: apresenta apenas uma ideia.
      -  COMPOSTA: conjunto de proposições simples.
### Conectivos Lógicos
 **Operação**        | **Estrutura Lógica**  | **Conectivo**|
 |:---:|:---:| :---:|
 Conjunção           |           e           |      ^      
 Disjunção           |          ou           |      v
 Condicional         |      Se… então        |      → 
 Bicondicional       |   Se, e somente se    |     ↔
 Disjunção Exclusiva |       Ou… ou          |     ⊻
  
### Tabelas-Verdade


E:    

P | Q | P ^ Q
:---:|:---:|:--:|
T|T|T
T|F|F
F|T|F
F|F|F

OU:

P | Q | P v Q
:---:|:---:|:--:|
T|T|T
T|F|T
F|T|T
F|F|F

SE... ENTÃO:

P | Q | P → Q
:---:|:---:|:--:|
T|T|T
T|F|F
F|T|T
F|F|T

SE, E SOMENTE SE:

P | Q | P ↔ Q
:---:|:---:|:--:|
T|T|T
T|F|F
F|T|F
F|F|T

OU...OU...:

P | Q | P ⊻ Q
:---:|:---:|:--:|
T|T|F
T|F|T
F|T|T
F|F|F


 - **Precedência**: 
    1. Not
    2. E
    3. Ou
    4. Se... então
    5. Se, e somente se... 
    6. Ou..ou...
     - Se existirem dois iguais, então resolve pela ordem (o primeiro que aparecer).

### Definições Importantes
 - Tautologia
    - Uma proposição é sempre verdade.
 - Contradição
    - Uma proposição é sempre falsa.
 - Contingência
    - Admite ambos os valores lógicos (T e F)
 - Equivalência Lógica
    - Duas ou mais proposições com tabelas-verdade idênticas.
 - Argumento
    - É uma sequência finita de proposições que tem como resultado uma conclusão(q).
    1. Premissas : Hipóteses do argumento.
        p1,p2,...,pn implicam em q
    2. Valor lógico verdadeiro: chama-se válido.
    3. Valor lógico falso: chama - se inválido.
    4. Válido
        - A verdade das premissas implica na verdade da conclusão
    5. Inválido
        - Caso a conclusão seja falsa
   
 ### Lógica de Predicados
  - Permite expressar propriedades e relações entre objetos.
  
  quantificador | predicado/propriedade
  :---:|:---:
  quantos "sujeitos" tem | determinada propriedade
  
  - Quantificador Universal: **∀**(todos)
  - Quantificador Existencial: **∃**(pelo menos um)
  - Predicado: Sujeito representado por letras (x,y,..)
        - Propriedade por notação P(x)
  - Negação de Sentenças
  
  Negação | Equivalente
   :---:|:---:|
   ¬[(∃x)eF P(x)] | (∀x e F) ¬P(x)
  
  - Ordem dos Quantificadores **importa** na avaliação
    - Ex: **P(x)**: ser estudante **Q(x)**:ser sanfoneiro **x**: Todos presentes
        - (∀x e F) [P(x) v Q(x)] = Para qualquer pessoa na sala ou é estudante ou é sanfoneiro.
        - (∀x e F)P(x) v (∀x e F)Q(x) = Para qualquer pessoa na sala, ela é estudante ou para qualquer pessoa na sala ela é sanfoneira.
