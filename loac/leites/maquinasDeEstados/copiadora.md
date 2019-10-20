---
title: Copiadora
---

Implemente o circuito controlador de uma máquina copiadora.

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[7] |
| `ligar` | SWI[0] |
| `quantidade` | SWI[2:1] |
| `papel` | SWI[4] |
| `fora` | SWI[5] |
| `tampa` | SWI[6] |

- O `reset` deve ser assíncrono.
- O `clock` deve ter frequência de 1 Hz.
- O `ligar` indica que o usuário deseja iniciar a produção das cópias.
- A `quantidade` indica o número de cópias (entre 0 e 3, inclusive) a serem geradas.
- O `papel` representa o sinal de um sensor que indica a presença de papel no reservatório.
- O `fora` representa o sinal de um sensor que indica quando há papel enrolado dentro da copiadora.
- A `tampa` representa o sinal de um sensor que indica se a tampa da copiadora está aberta.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `copiando` | LED[0] |
| `falta` | LED[1] |
| `entupida` | LED[2] |

- A `copiando` indica que cópias estão sendo geradas pela copiadora atualmente.
- A `falta` indica a ausência de papel no reservatório na copiadora.
- A `entupida` indica se há entupimento no mecanismo da copiadora.

## Descrição

- O primeiro passo para utilizar essa copiadora é selecionar a quantidade de cópias a serem produzidas (usando o vetor de bits `quantidade`). O valor 0 indica que nenhuma cópia deve ser produzida.

- A seguir, o usuário deve ativar a chave `ligar` e mantê-la assim até que todas as cópias tenham sido produzidas. 

- A máquina copiadora é capaz de gerar apenas uma cópia a cada ciclo de *clock*.

- Em caso de falta de papel, a saída `falta` é ativada no momento em que deveria ser produzida uma cópia e a saída de cópias é suspensa até que haja recarga de papel na máquina.

- Se o papel dentro da copiadora ficar enrolado, o indicador de entupimento é ativado e a saída de cópias é suspensa.

- Para resolver o entupimento, o usuário deve seguir os seguintes passos:
  1. Abrir a tampa da máquina copiadora.
  2. Remover o papel enrolado.
  3. Fechar a tampa.
  
- Após esses passos, o indicador de entupimento é desativado e a máquina continuará fazendo cópias automaticamente.