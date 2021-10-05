---
title: Fila
---

## O que é?

É uma estrutura de dados do tipo **FIFO** (*first-in, first-out*). Os elementos são inseridos exclusivamente no fim da fila (chamada de *tail*) e removidos exclusivamente do início da fila (chamado de *head*).

## Representação

![alt](https://www.cos.ufrj.br/~rfarias/cos121/fila1.png)

## Operações

- `create()`: Criar uma fila vazia. 
- `enqueue()`: Inserir/Enfileirar elemento da fila, realizado em **O(1)**. 
- `dequeue()`: Remover elemento da fila, realizado em **O(1)**.
- `head()`: Acessar elemento da cabeça da fila, realizado em **O(1)**. 
- `isEmpty()`: Verificar se a fila está vazia, realizado em **O(1)**.
- `isFull()`: Verificar se a fila está cheia, realizado em **O(1)**.
