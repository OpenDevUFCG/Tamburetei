---
title: Fechadura de Cofre
---

Implemente o circuito de controle de uma fechadura de cofre. O cofre abrirá se, e somente se, o usuário acionar três chaves na sequência correta. 

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[7] |
| `chave` | SWI[2:0] |

- O `reset` deve ser síncrono.
- O `clock` deve ter frequência de 1 Hz.
- A `chave` é o conjunto de três chaves que são usadas para destravar a fechadura do cofre.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `iniciar` | LED[0] |
| `cofre_aberto` | LED[1] |
| `tentativas_erradas` | LED[3:2] |

- O `iniciar` indica que o usuário já pode inserir uma sequência para tentar abrir o cofre.
- O `cofre_aberto` indica que o cofre está atualmente aberto.
- O `tentativas_erradas` indica o número de vezes que o usuário inseriu uma sequência incorreta.

## Descrição

- Após o `reset`, o cofre é fechado, a sequência (chave) da fechadura é inicializada para a sequência **0-1-2** e a contagem de tentativas erradas é zerada.

- Exatamente 1 ciclo de *clock* depois do `reset`, a saída `iniciar` é ativada e o usuário pode inserir uma sequência para tentar abrir o cofre. Para isso, nos 3 ciclos de *clock* seguintes, o usuário deve levantar uma das chaves (0, 1 ou 2) em cada ciclo. Ao término da inserção da sequência, todas as chaves devem ser levantadas.

- Se o usuário acerta a sequência da fechadura, o cofre é aberto e a saída `iniciar` é desativada. Se, no ciclo de *clock* seguinte, o usuário colocar todas chaves para 0 e inserir uma nova sequência nos 3 ciclos de *clock* a seguir (**2-1-0**, por exemplo), esta será a nova sequência da fechadura e o cofre será fechado automaticamente.

- Se o usuário não desejar redefinir a sequência, o cofre será fechado no ciclo de *clock* seguinte. Após mais 1 ciclo de *clock*, a saída `iniciar` é ativada novamente e tudo se repete.

- Se o usuário não acertar a sequência, o cofre não abre e, após 2 ciclos de *clock*, a saída `iniciar` será ativada novamente. Após 2 tentativas erradas, a saída `iniciar` só será ativada novamente quando o circuito sofrer `reset`.