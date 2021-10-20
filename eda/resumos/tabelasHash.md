---
title: Tabelas Hash
---

## O que é?

Tabela hash é uma estrutura de dado bastante utilizada que mapeia chaves a valores para pesquisas altamente eficientes. 

## Representação

![alt](https://he-s3.s3.amazonaws.com/media/uploads/0e2c706.png)

## Implementação

Para implementação, pode-se utilizar um array de linked lists e uma função de código hash. Para inserir uma chave (que pode ser uma string ou qualquer outro tipo de dado) e um valor, devemos fazer da seguinte forma:

1. Primeiramente, calculamos o código hash da chave através da função de código hash.
2. Em seguida, mapeamos o cósigo hash para um índice do array. Isso pode ser feito assim: hash(key) % array_lenght. 
3. Duas chaves diferentes podem ser mapeadas para o mesmo índice. Uma forma de resolver isso é utilizando linked lists vinculas as chaves e aos valores. Dessa forma, teremos duas chaves diferentes apontando para o mesmo índice, e os valores vão sendo armazenados na linked list.


