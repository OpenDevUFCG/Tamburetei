1. Dadas as seguintes gramáticas:  

  | Gramática I | Gramática II |
  | --- | --- |
  | A → 0B| G2= (V, Σ, R, S) |
  | B → A1| V = {A, B} Σ = {0,1, #} |
  | A→lambda| R = {A → 0B0 | 1B1 | B, B → 0,1, lambda}, S = A |  

a. Quais das gramáticas acima são linear (à direita ou à esquerda)? Determine o AF equivalente para elas.  
b. Descreva a linguagem gerada pela Gramática II.  
c. Utilizando a árvore sintática, exiba a derivação para no mínimo duas palavras de sua escolha (de tamanhos diferentes e tamanho mínimo igual a 1) a partir da gramática II.  
d. A intersecção das linguagens geradas pelas gramáticas acima é uma linguagem regular? Justifique.  

2. Classifique as afirmações abaixo em Verdadeiro ou Falso. Justifique as
afirmações falsas.  
a. ( ) É possível gerar um AFD equivalente para qualquer gramática.  
b. ( ) Nem toda sentença gerada por uma gramática deve
necessariamente começar pelo símbolo de partida.  
c. ( ) Toda gramática consegue gerar uma linguagem regular.  
d. ( ) Uma cadeia w é derivada ambiguamente na gramática livre-do-contexto G se ela tem duas ou mais derivações à direita.  
e. ( ) Toda gramática livre-do-contexto pode ser convertida na forma
normal de Chomsky.
3. Verifique se a seguinte gramática é ambígua ou não, justificando sua
resposta.  
G = (V, Σ, R, S)  
V = {A} Σ = {0,1} R = {A → AA | 0A0 | 1A1 | lambda} S = A

4. Converta a seguinte GLC em uma GLC equivalente na forma normal de
Chomsky.  
A → BAB | B | lambda B →00 | lambda
