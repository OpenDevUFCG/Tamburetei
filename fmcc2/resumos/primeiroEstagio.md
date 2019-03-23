# Fundamentos Matemáticos para Ciência da Computação II - Primeiro Estágio

## Conceitos

- **Prova:** estabelece a verdade das afirmações matemáticas.
- **Teorema:** é uma afirmação que pode ser mostrada verdadeira.
- **Lemma:** é normalmente um teorema auxiliar utilizado para provar outros teoremas.
- **Corolário:** é um teorema que pode ser estabelecido diretamente de um teorema que foi provado.
- **Conjectura:** é uma afirmação sendo proposta como verdade, mas que precisa ser provada para virar teorema.
- **Axioma:** premissa considerada necessariamente evidente e verdadeira, porém indemonstrável.

## Formas dos Teoremas:

- Muitos teoremas são apresentados na forma condicional <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20p%20%5Crightarrow%20q">.
- **Exemplo 1:** "se x > y, no qual x e y são números reais positivos, então x² > y²". O que esse teorema realmente significa é:

<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cforall_%7Bx%2Cy%7D%28P%28x%2Cy%29%5Crightarrow%20Q%28x%2Cy%29%29">
</p>

onde,

<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20P%28x%2Cy%29%20%5Ctherefore%20x%20%3E%20y">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20Q%28x%2Cy%29%20%5Ctherefore%20x%5E2%20%3E%20y%5E2">
</p>

- Teoremas também aparecem na forma condicional.
- A implicação deve ser demonstrada nas duas direções.

## Preliminares

- Considere as definições a seguir para os exemplos que seguem:
  - **Paridade de números inteiros:** um inteiro **n** é par se existe um inteiro **k** tal que *n = 2k*, e **n** é ímpar se existe um inteiro **k** tal que *n = 2k + 1*.
  - **Números racionais:** um número real **r** é dito racional se existem inteiros *p* e *q*, com *q* diferente de 0, tal que *r = p/q*.
  - **Potência perfeita:** um número inteiro **n** é dito uma potência perfeita se existem números inteiros *b > 1* e *k > 1* tais que <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20n%20%3D%20b%5E%7Bk%7D">.
  
## Demonstração exaustiva e por Contra-exemplo

- Verifica-se a verdade da conjectura para todos os elementos da coleção.
- Para provar a falsidade da conjectura, basta achar um contra-exemplo.
- **Exemplo 2:** Prove a conjectura *"Para todo inteiro positivo* <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20n%2C%20n%21%20%5Cleq%20n%5E2">*"*.
  - **Solução:** a conjectura é **falsa** pois não é verdade para todo *n*: é falsa para *n = 4*.
  
## Demonstração por casos:

- Uma prova por casos deve cobrir todos os casos possíveis que aparecem em um teorema.
- **Exemplo 3:** Prove que se *n* é um inteiro, então *n²* >= *n*.
  - **i)** Quando *n = 0*: Como *0² = 0*, então *n²* >= *n* é verdadeiro nesse caso;
  - **ii)** Quando *n >= 1*: Multiplicando os dois lados da inequação por *n*, obtemos *n.n >= n.1*. Isso implica que *n²* >= *n* para *n >= 1*;
  - **iii)** Quando *n <= -1*: Como *n² >= 0*, segue que *n² >= n*.

## Demonstração direta

- A demosntração direta de uma afirmação da forma <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20p%20%5Crightarrow%20q">:
  - **i)** assume que o antecedente *p* é verdadeiro e daí;
  - **ii)** deduz a conclusão *q*.
- Normalmente usa-se axiomas, definições, lemmas e teoremas, em conjuntos com regras de inferência, para mostrar que *q* também deve ser verdade.

- **Exemplo 4:** Prove o seguinte teorema: *se n é um número ímpar, então n² também é ímpar".
  - **i)** Como *n* é ímpar, *n = 2k + 1*, para <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20k%5Cin%20%5Cmathbb%7BZ%7D">;
  - **ii)** Elevando os dois lados da igualdade ao quadrado, *n² = (2k + 1)²*, temos:
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20n%5E%7B2%7D%20%3D%204k%5E%7B2%7D%20&plus;%204k%20&plus;%201">
</p>

rearranjando,
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20n%5E%7B2%7D%20%3D%202%282k%5E%7B2%7D%20&plus;%202k%29%20&plus;%201">
</p>

portanto, concluímos que *n²* também é ímpar.

## Demonstração por contraposição

- Uma conjectura da forma <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20p%20%5Crightarrow%20q"> pode ser provada mostrando-se a sua contrapostiva:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cneg%20q%20%5Crightarrow%20%5Cneg%20p">
</p>

- **Exemplo 5:** Mostre que se *3n + 2* é ímpar, então *n* é ímpar.
  - **i)** Primeiro assumimos que *n* é par (*a negação que n é ímpar*), ou seja, *n = 2k*;
  - **i)** Agora basta verificar que *3n + 2* também é par:
  <p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%203%282k%29%20&plus;%202%20%3D%206k%20&plus;%202%20%3D%202%283k%20&plus;%201%29">
</p>

  portanto, demonstra-se por contraposição que a afirmativa é verdadeira.
  
  
## Demonstração por contradição

- Para demonstrar *p*, assumimos *¬p* e mostramos que isso leva a uma contradição;
- Para provar <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20p%20%5Crightarrow%20q">, bastar mostrar <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20p%20%5Cwedge%20q%20%5Crightarrow%20F">.
- **Exemplo 6:** Mostre que se *3n + 2* é ímpar, então *n* é ímpar por contradição.
  - **i)** Vamos assumir que *3n + 2* é ímpar e *n* é par;
  - **ii)** Vimos que no *exemplo 5* que se *n* é par, então *3n + 2* é par;
  - **iii)** Por contradição, *n* tem que ser ímpar.
  
## Indução Matemática

- É usada para mostrar que uma dada afirmação é verdadeira para todos os inteiros positivos.
- Por exemplo, para todo <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20n%20%5Cin%20%5Cmathbb%7BZ%7D%5E%7B&plus;%7D">:
  - <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20n%21%20%5Cleq%20n%5E%7Bn%7D">;
  - <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20n%5E%7B3%7D%20-%20n"> é divisível por 3;
  - a soma dos primeiros *n* inteiros positivos é <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfrac%7Bn%28n&plus;1%29%7D%7B2%7D">.
  
## Indução fraca

- Primeiro princípio da indução: Para provar que *P(n)* é verdade para todo <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20n%20%5Cin%20%5Cmathbb%7BZ%7D%5E%7B&plus;%7D">, precisaremos provar o seguinte:
  - *P(1)* (Passo básico ou base da indução);
  - <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20%28%5Cforall_%7Bk%7D%20%5Cin%20%5Cmathbb%7BZ%7D%5E%7B&plus;%7D%29%28P%28k%29%20%5Crightarrow%20P%28k&plus;1%29%29"> (Passo indutivo).
  
- Demonstração usando o primeiro princípio da indução:
  - **i)** Prove a base da indução;
  - **ii)** Suponha *P(k)*;
  - **iii)** Prove *P(k + 1)*.
  
- **Exemplo 7:** Mostre que a equação *1 + 3 + 5 + ... + (2n - 1) = n²* é verdadeira para todo  <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20n%20%5Cin%20%5Cmathbb%7BZ%7D%5E%7B&plus;%7D">.
- **i)** Para *n = 1*, *1 = 1²* é verdadeiro. Agora supomos *P(k)* verdadeiro:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%201%20&plus;%203%20&plus;%205%20&plus;%20...&plus;%20%282k%20-1%29%20%3D%20k%5E%7B2%7D">
</p>
<br/>

- **ii)** Usando a hipótese da indução, queremos mostrar *P(k + 1)*, ou seja:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%201%20&plus;%203%20&plus;%205%20&plus;%20...&plus;%20%282k%20-%201%29&plus;%20%282%28k&plus;1%29%20-1%29%20%3D%20%28k&plus;1%29%5E%7B2%7D">
</p>
<br/>

- **iii)** Mostrando-se a penúltima parcela , procedemos como segue:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%201%20&plus;%203%20&plus;%205%20&plus;%20...&plus;%20%282k%20-%201%29&plus;%20%282%28k&plus;1%29%20-1%29%20%3D%20%28k&plus;1%29%5E%7B2%7D">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20k%5E%7B2%7D%20&plus;%202%28k&plus;1%29%20-%201%20%3D%20%28k&plus;1%29%5E%7B2%7D">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20k%5E%7B2%7D%20&plus;%202k%20&plus;%201%3D%20%28k&plus;1%29%5E%7B2%7D">
</p>


## Observações:
- Para uma maior fixação do assunto, recomenda-se a resolução *by yourself* dos exercícios propostos;
- Pode haver diferenças entre o conteúdo disponibilizado e o conteúdo programado da disciplina. Verifique com o professor e/ ou monitores.
