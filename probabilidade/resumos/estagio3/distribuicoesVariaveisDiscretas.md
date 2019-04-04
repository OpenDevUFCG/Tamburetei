## Distribuição de Bernoulli

*Notação: X~Ber(p)*

Essa distribuição é usada quando estamos interessados em experimentos nos quais o resultado apresentam(sucesso) ou não(fracasso) uma característica. Por exemplo:

1. Uma moeda é lançada e o resultado é coroa ou não.
2. Uma peça é defeituosa ou não.

Assim, uma variável aleatória pode assumir:  
    **1** em caso de sucesso  
    **0** em caso de fracasso  

E sua função de probabilidade é dada por:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/6da22ccc121fa8b49e6a52fae06ed88a9e8582f3)

Em que:  
`p`, representa a prob. de sucesso.  
`1-p`, representa a prob. de fracasso.  

Propriedades:

*E(X): p*  
*VAR(X): p(1-p)*


## Distribuição Binomial

*Notação: X~B(n, p)*

Essa distribuição é usada quando fazemos `n` ensaios da anterior, ou seja, enquanto na de [Bernoulli](distribuicao-de-bernoulli), realizamos apenas um ensaio, nessa realizamos vários, com uma característica importante, cada um deles deve ser independente e sendo assim é necessário que **haja reposição**.

Da mesma forma que a Bernoulli, a probabilidade de sucesso é `p`, e a de fracasso `1-p`. O que difere aqui, além da quantidade de experimentos, é que como a probabilidade de sucesso/fracasso para cada experimento é a mesma(por serem independentes) o que interfere são as possíveis sequencias em que o sucesso ou fracasso ocorre e por isso surge a formula de combinatória.

Imagine a seguinte situação, você lança uma moeda quatro vezes e tem interesse em saber a probabilidade de que ocorra cara em 2 lançamentos. Uma situação possível é:  
`C C R R`  
Outra é:  
`C R C R`  
Além dessas, temos outras e como cada uma dessas representa uma possibilidade, precisamos considerá-las no nosso cálculo, assim sendo, a função de probabilidade da binomial é dada por:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/7a96d0dd9ee96319dacfbe372578fbcc29ffdefa)

Em que:  
`p`, representa a prob. de sucesso.  
`1-p`, representa a prob. de fracasso.  
`k`, representa a quantidade de sucessos.  
`n`, representa a quantidade de ensaios.


Propriedades:

*E(X): np*  
*VAR(X): np(1-p)*

## Distribuição Hipergeométrica

*Notação: X~hip(N, K, n)*

Essa distribuição é usada quando fazemos ensaios sem reposição, e os elementos da população são divididos entre aqueles que possuem um atributo A e aqueles possuem um B. A ideia também é muito similar a anterior o que você deve ficar atento é que **não há reposição**.

Dito isso, podemos definir a função de probabilidade dessa distribuição como sendo:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/cb1f04d4adc49785408d221abb404bfe5751b2c8)

Em que:  
`K`, representa a quantidade de elementos que possuem o atributo de interesse.  
`k`, representa a quantidade de elementos que queremos que tenha o atributo.  
`N`, representa a população.
`n`, representa a quantidade de elementos retirados ao acaso.

De maneira mais verborrágica, podemos traduzir essa fórmula, no seguinte, dada uma população de `N` objetos, sabemos que `K` contém um atributo A e `N-K` possuem um B. Desses objetos `n` são escolhidos ao acaso, sem reposição, e queremos saber a probabilidade de `k` elementos dessa amostra possuirem o atributo A.

Propriedades:

*E(X): np*  
*VAR(X): np(1-p)*[(N-n)/(N-1)]*


## Distribuição de Poisson

Essa distribuição é usada quando temos interesse num certo experimento seja contar o número de
ocorrência de um certo evento, o qual pode ocorrer durante um intervalo de tempo, ao
longo de uma superfície ou volume. Por exemplo:

1. Número de chamadas recebidas por um telefone durante 5 min.
2. Número de falhas de um computador durante um dia de operações.

A sua função de probabilidade é dada por:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/242598d54a92171cc45b49287a0332d4005e3eef)

Em que:

`λ`, representa a taxa de ocorrência por unidade medida.
`k`, quantidade de ocorrências do evento de interesse.

Propriedades:

*E(X): λ*  
*VAR(X): λ*
