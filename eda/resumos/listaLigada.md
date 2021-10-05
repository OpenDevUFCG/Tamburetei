---
title: Lista Ligada
---

## O que é?

É uma estrutura de dados que arranja objetos em ordem linear. Cada objeto é chamado de nó e eles são interligados através de ponteiros. Cada nó contém uma referência para o proximo nó da lista até que seu proximo seja *null* (ou *NIL*), o que indicará o final da lista.

As principais características são a alocação dinâmica (sem limite de tamanho), a ordenação determinada por ponteiros e o acesso de forma sequencial. Essa estrutura aceita duas formas de representação: a lista ligada simples e a lista duplamente ligada. Na simples, os nós possuem apenas um apontador para o seu próximo elemento. Na lista duplamente ligada os nós possuem dois ponteiros: um pra o elemento anterior e outro para o próximo elemento.

## Representação

![alt](https://miro.medium.com/max/615/1*iMYmkYDCSrXXdwpbqm-ekA.jpeg)

## Operações

- `insert(T element)`: Inserir um elemento em um nó no final da lista, realizado em **O(1)**.
- `remove(T element)`: Remover um elemento que está contido na lista, realizado em **O(n)**.
- `search(T element)`: Verificar se um elemento está contido na lista, realizado em **O(n)**.
- `isEmpty()`: Verificar se a lista está vazia, realizado em **O(1)**.
- `size()`: Verificar o tamanho atual da lista, realizado em **O(n)**.
- `toArray(T element)`: Representar a lista ligada em um *array*, realizado em **O(n)**.

