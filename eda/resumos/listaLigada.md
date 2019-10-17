---
title: Lista Ligada
---

## O que é?

É uma estrutura de dado que arranja objetos em ordem linear. Cada objeto é chamado de nó e eles são interligados entre si através de ponteiros.
Cada nó contém uma referência para o proximo nó da lista até que seu proximo seja null, o que indicará o final da lista. Tem como características
sua alocação dinâmica, ou seja, não tem limite de tamanho, sua ordem é determinada pelo ponteiro e não por um indíce e seu acesso acontece de forma sequencial. Essa estrutura aceita duas formas de representação, a lista ligada simples e a lista duplamente ligada. Na simples, os
nós possuem apenas um apontador para o seu proximo elemento, enquando na duplamente ligada os nós possuem dois apontadores, um pra o elemento anterior e outro para seu próximo.

## Representação

![alt](https://miro.medium.com/max/615/1*iMYmkYDCSrXXdwpbqm-ekA.jpeg)

## Operações

* isEmpty()
* size()
* search(T element)
* insert(T element)
* remove(T element)
* toArray()

