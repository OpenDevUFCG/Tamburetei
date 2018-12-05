# Heap Binária

## O que é

Árvore binária que possui as propriedades:

- Está completa até pelo menos seu *penúltimo nível*
- Se o seu último nível não está completo, todos os nós do *último nível* deverão estar agrupados a *esquerda*
- Possui dois tipos:
    - Max heap: O valor de todos os nós é menor que o nó **pai**. A raíz irá conter o maior elemento.
    - Min heap: O valor de todos os nós é maior que o nó **pai**. A raíz irá conter o menor elemento.

## Representação

Pode ser representada por uma estrutura de Array.

Exemplo de *Min-Heap*:
![alt](https://codigocomcafe.files.wordpress.com/2010/09/heap1.png)

Para obter pai, filhos usamos os índices do Array para obter, onde vai ser:

- `parent(i) return i/2`
- `left-son(i) return 2i`
- `right-son(i) return 2i + 2`

Pode verificar isso na imagem acima, pegando por exemplo **4** que está na posição **i=1**, para sabemos seu filho a esquerda, fazemos **2*i=2** que é o elemento **9**


## Implementação

- Para manter a invariância da raíz, se for Max-heap sempre deve ser o maior elemento, Min-heap o menor. É preciso uma operação de **HEAPIFY** que verifica cada nó e vai subindo a árvore


## Aplicações
- Priority Queue: Heap é usada para implementar uma fila que possui uma certa ordem de prioridade e ordenação, sendo usada para a classe Java **PriorityQueue**
