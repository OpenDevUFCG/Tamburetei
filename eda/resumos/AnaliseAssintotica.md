---
title: Análise Assintótica
---

   A gente utiliza o Método Analítico por ser simples e rápido mas algumas funções podem ser muito complicadas ou muito longas e aí o método analítico já não ajuda tanto. Por isso levamos em consideração outro método: a Análise Assintótica.

 O que acontece é que simplificamos ainda mais o resultado dado nas funções geradas dos métodos analíticos, como n^2 + 5 para grande entradas cresce de maneira **muito próxima** a n^2, dizemos que a função cresce como uma função n^2.

### Como que faz

  Para simplificar, ignoramos constantes e valores de menor magnitude.

- Eficiência assintótica:
    - Torna relevante apenas a ordem de crescimento do tempo de execução

### Por que?

- Ordem de crescimento:
    - Como a função se comporta com valores de entradas muito grande.

Porque usamos o conhecimento do desempenho para decidir qual o melhor algoritmo para determinada situação, e é muito mais fácil saber o comportamento de n^4 do que de uma expressão complexa com n^4.

Exemplo: Para um algoritmo de busca para entradas muito grandes. Entre um de Θ(log(n)) e Θ(n), é preferível o que cresce de maneira mais lenta no gráfico: Θ(log(n)). 

Não é tão fácil fazer a mesma comparação com Θ(5428 + (sin(90) * 120) * log(n)) e Θ(100* 589 + 9*n + 50000).

## Notação Assintótica: Θ

Determina o limite da função usando Teorema do Confronto visto em Calculo I. Para ver se f(n) pertence à Θ(g(n)), usamos a seguinte equação:

 0 ≤ c1 * g(n) ≤ f(n) ≤ c2 * g(n), ∀ n ≥ n0

- c1, c2 e n0 maiores que 0.
- A partir de uma determinada entrada sempre g(n) vai ser maior que f(n).

## Notação Assintótica: O

Big O é para determinar o limite superior para f(n). No pior caso, a função demorar o tempo y para concluir em comparação a g(n). Temos que f(n) é O(g(n)) com:

 0 ≤ f(n) ≤ c * g(n), ∀ n ≥ n0

- É a notação mais usada.

## Notação Assintótica: Ω

Ω é relacionado ao limite inferior. No melhor caso, o algoritmo não consegue ser mais veloz do que g(n). Temos que f(n) é Ω(g(n)) com:

0 ≤ c * g(n) ≤ f(n), ∀ n ≥ n0

## ozinho e ômegazinho

o é muito similar à O porém tem o intervalo aberto, ou seja, não inclui a função. 

ω do mesmo jeito é muito similar a Ômega mas não inclui o próprio conjunto.

Exemplo: O(n^2) inclui n^2, mas o(n^2) não, entretanto inclui n.