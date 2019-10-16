---
title: Ar-Condicionado
---

Implemente o circuito controlador de uma máquina de ar-condicionado.

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[7] |
| `diminuir` | SWI[0] |
| `aumentar` | SWI[1] |

- O `reset` deve ser assíncrono.
- O `clock` deve ter frequência de 1 Hz.
- A `diminuir` representa o comando para diminuir a temperatura desejada em 1 grau Celsius.
- A `aumentar` representa o comando para aumentar a temperatura desejada em 1 grau Celsius.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `real` | LED[6:4] |
| `desejo` | LED[2:0] |
| `pingando` | LED[3] |

- O `real` representa a temperatura atual do ambiente.
- O `desejo` representa a temperatura desejada para o ambiente.
- O `pingando` indica que o ar-condicionado está gotejando atualmente.
- Tanto `real` quanto `desejo` representam valores entre 20 e 27 graus Celsius (inclusive).
   - Por exemplo, se `real` tem valor 3, o ambiente está a 23 graus Celsius.

## Descrição

- No reset, a temperatura desejada e temperatura real são colocadas imediatamente para 20 graus Celsius.

- Através das chaves `diminuir` e `aumentar`, o usuário diminui ou aumenta a temperatura desejada em 1 grau Celsius a cada ciclo de *clock*.

- As temperaturas real e desejada não podem ser menores que 20 graus Celsius, nem maiores que 27 graus Celsius.

- Caso nenhuma das chaves (`diminuir` e `aumentar`) estejam acionadas, a temperatura desejada permanece igual. O mesmo vale se as duas chaves forem acionadas ao mesmo tempo.

- A temperatura real tende a se igualar à temperatura desejada, mas só consegue aumentar ou diminuir em 1 grau Celsius a cada 2 ciclos de *clock*.

- O ar-condicionado começa a pingar 10 ciclos de *clock* após o reset.

- Para interromper o gotejamento, o usuário deve ter a temperatura real em 27 graus Celsius por, pelo menos, 4 ciclos de *clock*. Depois desse intervalo, o ar-condicionado irá parar de pingar.