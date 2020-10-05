---
title: Algoritmos Recursivos
---

# Análise de Algoritmos Recursivos

Algoritmos recursivos são solução que chamam a si mesmo durante a execução, portanto não podemos usar o método que vínhamos usando até o momento. Felizmente para tratar de algoritmos recursivos, temos duas opções: **Método da Árvore de Recursão** e **Teorema Mestre**, que analisa a **Relação de Recorrência**.

### Relação de Recorrência

Uma equação ou inequação que descreve uma função em termos dela mesmo considerando entradas menores. Exemplo: T(n) = T(n-1) + O(1)

### Método da Árvore de Recursão

Para calcular o custo da função, você simula sua execução em uma árvore, o topo é a entrada e as arestas representam a chamada recursiva. O custo total é calculado sabendo o custo de cada nível da árvore, mas para calcular o tempo de execução temos que somar o custo de cada nível,  e multiplicando pela a altura dela mais o custo inicial.

Portanto, fica = custoNiveis * altura + custoInicial

A altura da árvore corresponde ao caminho do topo até o fim, por isso não conta a primeira execução.

### Teorema Mestre

Algumas (muitas) relações de recorrência podem ser descritas como: T(n) = a * T(n/b) + f(n), com a ≥ 1, b > 1 e f(n) não negativo;

Nesses casos, podemos aplicar o Teorema Mestre, que determina de maneira direta que:

- Se f(n) < n ** log(b)a, então T(n) = theta(n ** log(b)a).
- Se f(n) = n ** log(b)a, então T(n) = theta(f(n) * log(b)n).
- Se f(n) > n ** log(b)a, então T(n) = theta(f(n)).