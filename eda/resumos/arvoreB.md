# Árvore B

## O que é?

É uma árvore balanceada que permite pesquisa, inserção e remoção em tempo logaritímico. Muito usado em sistemas de armazenamento que possuem grande volume de dados.

## Propriedades

- Todas as folhas estão no último nível
- Possui uma **ordem** que é o número máximo de filhos que cada nó pode ter
- Os nós são chamados de *páginas*

Sendo uma árvore de *ordem **m***:

- Cada nó tem no máximo **m** filhos
- Cada nó exceto a raíz tem no mínimo **m/2 - 1** filhos
- A raiz tem pelo menos dois filhos se não for folha
- Um nó interno com *k* filhos, possui *k-1* chaves
- As chaves de cada nó estão ordenados, e servem como separação

## Implementação

### Inserção

1. Insere nas folhas
2. Se a folha não estiver cheia, o elemento será inserido respeitando a ordem
3. Se estiver cheio, faz o split do nó
4. No split se escolhe o elemento da mediana dos elementos, criando um novo nó a esquerda com os elementos que estavam atrás da mediana, e um nó a direita com os elementos a frente. A mediana é inserida no pai
5. Se causou lotação no pai, repete o processo