# Fundamentos Matemáticos para Ciência da Computação II - Exercícios Resolvidos - Primeiro Estágio

## Questão 1 (Demonstração por casos)
Mostre que se *x* ou *y* forem inteiros pares, então *xy* é par.

- **i)** Temos que um número par *n* pode ser descrito como *n = 2k*, e um número ímpar *t* como *t = 2w + 1*;
- **ii)** Temos que: *x = 2k* e *y = 2w + 1*, então:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20xy%20%3D%202k%282w%20&plus;%201%29">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20xy%20%3D%204kw%20&plus;%202k">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20xy%20%3D%202%28kw%20&plus;%20k%29">
</p>
<br/>

- **iii)** Como a multiplicação e a soma entre inteiros resulta em um outro inteiro, então a afirmação se torna verdadeira;
- **iv)** Da mesma forma do item **i)**, temos que: *x = 2k + 1* e *y = 2w*, então:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20xy%20%3D%20%282k%20&plus;%201%29%282w%29">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20xy%20%3D%204kw%20&plus;%202w">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20xy%20%3D%202%282kw%20&plus;%20w%29">
</p>
<br/>

- **v)** Pela demosntração por casos, mostramos a veracidade da afirmativa.

## Questão 2 (Demonstração direta)
Dê uma demonstração direta ao teorema *"Se um inteiro é divisível por 6, então duas vezes esse inteiro é divisível por 4"*.

- **i)** Como *n|6*, temos que *n = 6k*, para *k* inteiro;
- **ii)** Atribuindo a condição do enunciado em ambos os lados da equação, temos:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cfrac%7B2n%7D%7B4%7D%20%3D%20%5Cfrac%7B2%286k%29%7D%7B4%7D%20%3D%203k">
</p>
<br/>

- **iii)** Por definição, a multiplicação entre inteiros resulta em um inteiro. Ou seja, existe um inteiro que multiplicado por *k* resultará em um *n*.

## Questão 3 (Demonstração por contraposição)
Prove que o número *n* é um inteiro ímpar se, e somente se, 
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%203n%20&plus;%205%20%3D%206k%20&plus;%208">
</p>
<br/>

para algum inteiro *k*.

- **i)** Note que se trata de uma implicação bicondicional, deve-se provar ambos os lados da implicação:
  - *Se n é um inteiro ímpar. então 3n + 5 = 6k + 8 para algum inteiro k*;
  - *Se 3n + 5 = 6k + 8 para algum inteiro k, então n é um inteiro ímpar*.
- **ii)** Podemos provar o primeiro caso por demosntração direta, substituindo *n*:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%203%282k%20&plus;%201%29%20&plus;%205%20%3D%206k%20&plus;%208">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%206k%20&plus;%208%20%3D%206k%20&plus;%208">
</p>

- **iii)** Na segunda condição, temos que:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20P%3A3n&plus;5%20%3D6k%20&plus;%208">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20Q%3A%20%5Ctextrm%7Bn%20eh%20impar%7D">
</p>

- **iv)** Por contraposição, temos:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20P%5Crightarrow%20Q%5Cequiv%20%5Cneg%20Q%20%5Crightarrow%20%5Cneg%20P">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cneg%20Q%3A%20%5Ctextrm%7Bn%20eh%20par%7D">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cneg%20P%3A%203n&plus;5%5Cneq%206k%20&plus;%208">
</p>

- **v)** Substituindo n, temos:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%203%282k%29&plus;5%20%5Cneq%206k%20&plus;%208%20%5CRightarrow%206k%20&plus;%205%20%5Cneq%206k%20&plus;%208">
</p>


- **vi)** Portanto, por contraposição, demonstra-se a segunda condição, verificando-se o teorema.

## Questão 4 (Demonstração por contradição)
Mostre por absurdo que <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20%5Csqrt%7B2%7D"> é um número irracional.

- **i)** Vamos supor que <img src="http://latex.codecogs.com/gif.latex?%5Cinline%20%5Csqrt%7B2%7D"> seja um número racional;
- **ii)** Um número racional é um número que pode ser escrito na forma *a/b*, sendo *a* um inteiro e *b* um inteiro diferente de 0;
- **iii)** Suponhamos que <img src="https://latex.codecogs.com/gif.latex?%5Cinline%20%5Csqrt%7B2%7D%20%3D%20%5Cfrac%7Ba%7D%7Bb%7D">;
- **iv)** Então, *a* e *b*, não podem ser ambos pares, pois se fossem, daria para simplificar;
- **v)** Elevando os dois lados ao quadrado, obtemos:
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%20%28%5Csqrt%7B2%7D%29%5E%7B2%7D%20%3D%20%28%5Cfrac%7Ba%7D%7Bb%7D%29%5E%7B2%7D%20%5CRightarrow%202%20%3D%20%5Cfrac%7Ba%5E%7B2%7D%7D%7Bb%5E%7B2%7D%7D">
</p>

- **vi)** Então, 
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%202b%5E%7B2%7D%20%3D%20a%5E%7B2%7D">
</p>

- **vii)** Por definição, temos que *a* é par. Então *b* não pode ser par;
- **viii)** Como *a* é par, pode ser escrito na forma de *a = 2k*:
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%202b%5E%7B2%7D%20%3D%20%282k%29%5E%7B2%7D%20%5CRightarrow%202b%5E%7B2%7D%20%3D%204k%5E%7B2%7D%20%5CRightarrow%20b%5E%7B2%7D%20%3D%202k%5E%7B2%7D">
</p>

- **ix)** Agora, pelos mesmos motivos do item *vii)*, temos que *b* também é par. O que se mostra um absurdo;
- **x)** Portanto, prova-se por contradição, a afirmação do enunciado.


## Questão 5 (Indução Fraca)
Mostrar para todo inteiro positivo *n*, 
<p align="center"> 
  <img src="https://latex.codecogs.com/gif.latex?%5Clarge%201%20&plus;%202%20&plus;%20...%20&plus;%20n%20%3D%20%5Cfrac%7Bn%28n&plus;1%29%7D%7B2%7D">
</p>

- **Passo 1:** Para demonstrar o caso base , vamos usar *n = 1*, assim temos:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cfrac%7B1%281%20&plus;%201%29%7D%7B2%7D%20%3D%20%5Cfrac%7B2%7D%7B2%7D%20%3D%201">
</p>

Para o caso base, a afirmação é verdadeira.

- **Passo 2:** Na hipótese indutiva, tomaremos a afirmação para *n = k* como verdadeira, ou seja:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%201%20&plus;%202%20&plus;%20...%20&plus;%20k%20%3D%20%5Cfrac%7Bk%28k&plus;1%29%7D%7B2%7D">
</p>

- **Passo 3:** Deve-se mostrar, para *n = k +1*, que
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%201%20&plus;%202%20&plus;%20...%20&plus;%20k%20&plus;%20%28k%20&plus;%201%29%20%3D%20%5Cfrac%7B%28k&plus;1%29%28%28k&plus;1%29&plus;1%29%7D%7B2%7D">
</p>

é verdadeira.

**i)** Utilizando a conjectura fornecida no passo **ii)**, temos que:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cfrac%7Bk%28k&plus;1%29%7D%7B2%7D%20&plus;%20k%28k&plus;1%29%20%3D%20%5Cfrac%7B%28k&plus;1%29%28k&plus;1&plus;1%29%7D%7B2%7D">
</p>

**ii)** Tornando os membros com o mesmo denominador na primeira parte da igualdade, temos que
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cfrac%7Bk%28k&plus;1%29%20&plus;%202%28k&plus;1%29%7D%7B2%7D%20%3D%20%5Cfrac%7B%28k&plus;1%29%28k&plus;2%29%7D%7B2%7D">
</p>

**iii)** Aplicando a distributiva entre os elementos em ambas as partes, temos que:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20%5Cfrac%7Bk%5E%7B2%7D%20&plus;%20k%20&plus;%202k%20&plus;%202%7D%7B2%7D%20%3D%20%5Cfrac%7Bk%5E%7B2%7D%20&plus;%20k%20&plus;%202k%20&plus;%202%7D%7B2%7D">
</p>

**iv)** Como demonstramos a veracidade da afirmação inicial para *n = k +1*, concluímos o **Passo 3** e provamos por indução a integridade desta mesma.


## Questão 6 (Demonstração Direta)
Prove que para todo a, b, c inteiros, se a|b e a|c então a|(b+c)

- **i)** Temos por definição que:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20a%7Cb%20%5CRightarrow%20b%20%3D%20a.x%2C%20x%20%5Cin%20%5Cmathbb%7BZ%7D">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20a%7Cc%20%5CRightarrow%20c%20%3D%20a.t%2C%20t%20%5Cin%20%5Cmathbb%7BZ%7D">
</p>

- **ii)** Seguindo a lógica do passo **i)**, temos que:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20a%7C%28b&plus;c%29%20%5CRightarrow%20b&plus;c%20%3D%20a.z%2C%20z%20%5Cin%20%5Cmathbb%7BZ%7D">
</p>

- **iii)** Substituindo os valores do passo **i)**:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20b%20&plus;%20c%20%3D%20a.x%20&plus;%20a.t%20%3D%20a.z">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20a.%28x&plus;t%29%20%3D%20a.z">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20x&plus;t%20%3D%20z">
</p>

- **iv)** Por definição, como a soma de dois inteiros resulta em um inteiro, então prova-se por demonstração direta que se a|b e a|c então a|(b+c).

## Questão 7 (Indução Forte)
Prove, usando indução forte, que é possível pagar qualquer quantia (inteira) maior que R$ 7 usando notas de R$ 3 (caso existissem) e de R$ 5.

- **Passo base:** Para *P(8)*, *P(9)*, *P(10)*, *P(11)*, temos que:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20P%288%29%20%3D%205%20&plus;%203%20%3D%208">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20P%289%29%20%3D%203%20&plus;%203%20&plus;%203%20%3D%209">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20P%2810%29%20%3D%205%20&plus;%205%20%3D%2010">
</p>
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Clarge%20P%2811%29%20%3D%203%20&plus;%203%20&plus;%205%20%3D%2011">
</p>

ou seja, para o caso base, a afirmação é verdadeira;

- **Passo indutivo:** *P(t)* é verdadeiro para *7 < t <= k*.
- Por essa hipótese, podemos concluir que *P(k - 2)* é verdadeiro, pois *k - 2 > 7*;
- Ou seja, podemos formar valores de *k - 2* reais utilizando apenas notas de 3 e 5 reais;
- E, para formar o valor de *k + 1* reais, basta adicionar mais uma nota de 3 à quantia de *k - 2* reais.
