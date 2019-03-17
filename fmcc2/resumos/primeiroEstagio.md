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
