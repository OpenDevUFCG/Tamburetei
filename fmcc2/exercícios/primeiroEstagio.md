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
