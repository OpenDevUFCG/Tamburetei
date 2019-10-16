---
title: Porta de Enrolar
---

Implemente o circuito de controle de uma porta de enrolar de uma loja. Portas de enrolar (também chamadas de portas de rolo) são feitas de lâminas de metal e, diferente das portas comuns que abrem e fecham, são enroladas/desenroladas no topo de seu vão para permitir/impedir a passagem. Normalmente utilizadas em estabelecimentos comerciais, esse tipo de porta é aberta no início do expediente e fechada em seu término. Em muitas lojas, esse processo é feito com o uso de um motor. 

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[7] |
| `fechar` | SWI[0] |
| `abrir` | SWI[1] |
| `em_baixo` | SWI[2] |
| `no_meio` | SWI[3] |
| `em_cima` | SWI[4] |
| `prog` | SWI[6:5] |

- O `reset` deve ser síncrono.
- O `clock` deve ter frequência de 1 Hz.
- O `abrir` é a chave utilizada para acionar o motor e abrir a porta de enrolar.
- O `fechar` é a chave utilizada para acionar o motor e fechar a porta de enrolar.
- O `em_cima` representa o sinal do sensor que indica que a porta está completamente aberta.
- O `em_baixo` representa o sinal do sensor que indica que a porta está completamente fechada.
- O `no_meio` representa o sinal do sensor que indica que a porta não está completamente aberta, nem completamente fechada.
- O `prog` representa uma chave de programação que permite atrasar o acionamento do motor.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `motor_abrindo` | LED[0] |
| `motor_fechando` | LED[1] |
| `alarme` | LED[3] |

- A `motor_abrindo` indica que o motor está acionado para abrir a porta de enrolar.
- A `motor_fechando` indica que o motor está acionado para fechar a porta de enrolar.
- O `alarme` indica a ocorrência de condições anormais.

## Descrição

- Após o `reset`, o motor deve ser acionado para fechar a porta de enrolar. Se ela já estiver fechada, o motor não deve ser acionado.

- Para testar o circuito de controle, você deve fazer o papel do dono da loja (usando as chaves `abrir` e `fechar`), mas também fazer o papel dos sensores da porta (com as chaves `em_baixo`, `no_meio` e `em_cima`).

- Se as chaves `abrir` e `fechar` forem acionadas simultaneamente, a porta deve se manter parada no ponto atual.

- Quando o usuário acionar a chave para abrir a porta, ela deve ser enrolada (aberta), a não ser que a porta já esteja completamente aberta.

- Quando o usuário acionar a chave para fechar a porta, ela deve ser desenrolada (fechada), a não ser que a porta já esteja completamente fechada.

- Se a porta estava completamente fechada ou completamente aberta, ela levará pelo menos 1 ciclo de *clock* para passar no meio do vão. Caso contrário, o alarme deve ser ativado e o motor deve ser desligado.

- Se a porta estava no meio do vão, ela precisa demorar mais do que 1 e menos do que 3 ciclos de *clock* para ser completamente aberta. Caso contrário, o alarme deve ser ativado e o motor deve ser desligado. 

- Se a porta estava no meio do vão, ela precisa demorar mais do que 1 e menos do que 3 ciclos de *clock* para ser completamente fechada. Caso contrário, o alarme deve ser ativado e o motor deve ser desligado.

- Se o vetor de bits `prog` tiver um valor maior do que 0 (digamos X) quando o usuário acionar uma das chaves para abrir ou fechar a porta de enrolar, o motor só deve ser acionado depois de um atraso de X ciclos de *clock*.