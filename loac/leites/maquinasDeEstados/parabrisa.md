---
title: Para-Brisa
---

Implemente o circuito de controle de um detector de chuva de um carro. Esse sensor é responsável por ligar automaticamente os limpadores de para-brisa.

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[7] |
| `chuva` | SWI[6:0] |

- O `reset` deve ser assíncrono.
- O `clock` deve ter frequência de 1 Hz.
- A `chuva` representa as gotas de chuva detectadas pelo sensor no ciclo atual do clock.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `limpador` | LED[1:0] |

- O `limpador` representa o estado atual dos limpadores de para-brisa do carro, podendo assumir três valores: 
  - **0:** Desligados.
  - **1:** Ligados em baixa velocidade.
  - **2:** Ligados em alta velocidade.

## Descrição

- No vetor de bits `chuva`, cada bit representa uma gota de chuva detectada. Suponha que a gota de chuva detectada evapora antes do próximo ciclo de *clock*. Assim, se uma das chaves **SWI** ficar ligada durante 2 ciclos de *clock*, significa que foi detectada uma gota no 1º ciclo e uma nova gota no 2º ciclo.

- Após o `reset`, os limpadores de para-brisa são desligados.

- Quando forem detectados mais do que 3 gotas por ciclo durante 3 ciclos de *clock*, os limpadores são ligados em baixa velocidade.

- Quando forem detectados mais do que 5 gotas por ciclo durante 2 ciclos de *clock*, os limpadores são ligados em alta velocidade.

- Com os limpadores ligados em alta velocidade, se forem detectados menos do que 5 gotas durante 1 ciclo de *clock*, a velocidade dos limpadores é reduzida para *"baixa velocidade"*.

- Se forem detectados menos do que 3 gotas durante 1 ciclo de *clock* em qualquer das velocidades, os limpadores são desligados.