# Árvore PV

## O que é

É uma árvore binária de busca(*BST*) que irá conter uma informação extra em cada nó, **cor**. A cor ajuda a árvore a ter um balanceamento bom, mas não perfeito(bem menos que a *AVL*). Suas operações de pesquisa, inserção e remoção são feitas em **O(log n)**. E altura(*h*) em **h <= 2.lg(n+1)**

## Invariantes

Suas propriedades são:

- Todo nó possui cor **PRETA** ou **VERMELHA**
- Todo folha NIL é *preta*
- A raiz é *preta*
- Todos os filhos de um nó *vermelho* são *pretos*
- A altura de um filho **nunca** é mais que o dobro da altura de outro filho
- Possui **black-height**
    - Número de nós *pretos* encontrados em um caminho que leva de um nó a outro
    - Não conta os nós NIL(folhas)
    - Black-height da raíz é a Black-height da árvore