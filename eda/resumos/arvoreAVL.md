---
title: Árvore AVL
---

## O que é?

É uma árvore binária de busca (**BST**) cujo objetivo é remover o problema do pior caso, onde a altura é O(n), evitando que a árvore fique *"pesando"* muito para um lado só.

## Propriedades

- Balanceamento
    - A altura das sub-árvores diferem no máximo em 1
    - Fator de balanceamento **FB = height(left)-height(right)**, se for:
        - $<$ 0 a árvore pesa para a direita
        - $>$ 0 a árvore pesa para a esquerda
        - = 0 a árvore está balanceada
  
## Implementação

Operações de inserção e remoção podem desbalancear a árvore, para isso usamos **operações de rotação**.

### Rotação

- Muda a estrutura sem alterar a ordem dos elementos
- Move um nó pra cima e um pra baixo
- O fator de balanceamento dirá pra que lado rotacionar
- Tipos:
    - Simples
        - Ocorre quando o filho do nó desbalanceado estiver no mesmo sentido
    - Dupla
        - Ocorre quando o filho do nó desbalanceado estiver no sentido inverso

- Casos
    - Left-Left
        - Rotação Simples
        - Raiz pesa pra esquerda e filho esquerdo pesa pra esquerda ou esta balanceado: rotação pra direita na raiz
    - Right-Right
        - Rotação Simples
        - raiz pesa pra direita e filho pesa pra direita ou esta balanceado: rotação pra esquerda na raiz
    - Left-Right
        - Rotação Dupla
        - raiz pesa pra esquerda e filho esquerdo pesa pra direita: rotacao esquerda no filho e direita no pai
    - Right-Left
        - Rotação Dupla
        - raiz pesa pra direita e filho direito pesa pra esquerda: rotacao direita no filho e esquerda no pai