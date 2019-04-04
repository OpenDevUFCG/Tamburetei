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

Propriedades:

**E(X): p**  
**VAR(X): p(1-p)**


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

Propriedades:

**E(X): np**  
**VAR(X): np(1-p)**

## Distribuição Hipergeométrica


## Distribuição de Poisson


