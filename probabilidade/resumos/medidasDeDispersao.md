---
title: Medidas de Dispersão
---

Feito com basse nesse [slide](https://www.dropbox.com/s/5byiyz93n9fr0gj/Aula%205_Medidas_Dispers%C3%A3o.pdf?dl=0)

## Sumário
- [Medidas de Dispersão](#Medidas-de-dispersão)
    - [Sumário](#sum%C3%A1rio)
    - [Desvio Médio](#Desvio-médio)
    - [Variância](#Variância)
    - [Coeficiente de variação](#Coeficiente-de-variação)
        

## Desvio médio
Considere um conjunto de observações de uma variável *x*, dado por *x_{1}*, *x_{2}*, ..., *x_{k}* com respectivas frequências *n_{1}*, *n_{2}*, ..., *n_{k}*. Definimos o desvio médio de *x*, denotado por *dm(x)*, como sendo a medida:

Considere um conjunto de observações de uma variável *x*, dado por ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20x_%7B1%7D),  ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20x_%7B2%7D), . . . , ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20x_%7Bk%7D) com respectivas frequências ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20n_%7B1%7D), ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20n_%7B2%7D), . . . , ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20n_%7Bk%7D). Definimos o desvio médio de *x*, denotado por *dm(x)*, como sendo a medida:

<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20dm%28x%29%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bk%7D%7Bn_%7Bi%7D%7Cx_%7Bi%7D-%5Coverline%7Bx%7D%7C%7D%7D%7Bn%7D">
</p>

Equivalente, temos:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20dm%28x%29%3D%7B%5Csum_%7Bi%3D1%7D%5E%7Bk%7D%7Bf_%7Bi%7D%7Cx_%7Bi%7D-%5Coverline%7Bx%7D%7C%7D%7D">
</p>


## Variância
Considere um conjunto de observações de uma variável *x*, dado por ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20x_%7B1%7D),  ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20x_%7B2%7D), . . . , ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20x_%7Bk%7D) com respectivas frequências ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20n_%7B1%7D), ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20n_%7B2%7D), . . . , ![](http://latex.codecogs.com/gif.latex?%5Cinline%20%5Cfn_cm%20%5Csmall%20n_%7Bk%7D). Definimos o variância de *x*, denotado por *var(x)*, como sendo a medida:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20var%28x%29%3D%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bk%7Dn_%7Bi%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2%7D%7Bn%7D">
</p>

Equivalente, temos:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20var%28x%29%3D%7B%5Csum_%7Bi%3D1%7D%5E%7Bk%7Df_%7Bi%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E2%7D">
</p>

O **desvio padrão** de *x*, *dp(x)*, é definido como:
<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20dp%28x%29%3D%5Csqrt%7Bvar%28x%29%7D">
</p>

## Coeficiente de variação
É uma medida relativa de variabilidade. O seu valor é determinado por intermédio do quociente entre o desvio padrão e a média aritmética dos dados:

<p align="center"> 
  <img src="http://latex.codecogs.com/gif.latex?%5Cfn_cm%20%5Clarge%20Cv%28x%29%3D%5Cfrac%7Bdp%28x%29%7D%7B%5Cbar%7Bx%7D%7DX100">
</p>

  - Um critério de decisão sobre a representividade ou não da média, pode ser dada pela seguinte linha de corte:
    - Se ![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B100%7D%20%5Cfn_cm%20%5Csmall%20Cv%28x%29%5Cgeq%200.5) , a média **não** é representativa;
    - Se ![](http://latex.codecogs.com/gif.latex?%5Cdpi%7B100%7D%20%5Cfn_cm%20%5Csmall%20Cv%28x%29%3C%200.5) , a média é representativa.
