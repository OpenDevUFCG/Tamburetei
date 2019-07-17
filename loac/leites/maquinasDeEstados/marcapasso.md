# Marca-Passo

Implemente o circuito de um aparelho marca-passo de um paciente cujo ritmo cardíaco precisa ser monitorado constantemente.

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[7] |
| `batida` | SWI[0] |

- O `reset` deve ser assíncrono.
- O `clock` deve ter frequência de 1 Hz.
- A `batida` representa a ocorrência de batimento cardíaco do paciente.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `pulso` | LED[0] |
| `alarme` | LED[1] |

- O `pulso` indica a presença de pulso cardíaco do paciente.
- O `alarme` indica a ocorrência de condições anormais.

## Descrição

- Após o `reset`, o marca-passo apenas verifica o número de ciclos até a próxima batida do coração do paciente.

- Caso se passem 3 ciclos de *clock* entre duas batidas de coração, o marca-passo não indica presença de pulsação.

- Caso se passem mais de 5 ciclos de *clock* entre duas batidas de coração, o marca-passo indica um pulso imediatamente.

- Se, por duas (ou mais) vezes, ocorre um intervalo maior que 5 ciclos de *clock* entre duas batidas de coração, o marca-passo indica um pulso novamente.

- Os pulsos emitidos são contabilizados como batidas de coração para a contagem do próximo intervalo de ciclos de *clock*.

- Se o número de ciclos de *clock* entre batidas de coração for menor do que 3, o alarme é ativado imediatamente.

- Depois de ativado, o alarme permanece assim até que o marca-passo sofra *reset*.