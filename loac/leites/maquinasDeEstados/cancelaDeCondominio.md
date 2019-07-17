# Cancela de Condomínio

Implemente o circuito de controle de cancelas para entrada de carros em um condomínio. Existem 2 cancelas, uma para moradores e outra para visitantes, mas a estrutura do condomínio não permite a entrada de dois carros simultaneamente.

##  Entradas

| Entrada | Onde? |
| :--: | :--: |
| `clock` | LED[7] |
| `reset` | SWI[0] |
| `chega_morador` | SWI[1] |
| `identifica_morador` | SWI[2] |
| `entrando_morador` | SWI[3] |
| `chega_visitante` | SWI[5] |
| `identifica_visitante` | SWI[6] |
| `entrando_visitante` | SWI[7] |

- O `reset` deve ser síncrono.
- O `clock` deve ter frequência de 1 Hz.
- O `chega_morador` indica a chegada de um carro na frente da cancela dos moradores.
- O `chega_visitante` indica a chegada de um carro na frente da cancela dos visitantes.
- O `identifica_morador` indica que o morador se identificou através de um sensor de digital.
- O `identifica_visitante` indica que o visitante se identificou para o porteiro do condomínio.
- O `entrando_morador` indica que um carro está passando pela cancela dos moradores em direção ao condomínio.
- O `entrando_visitante` indica que um carro está passando pela cancela dos visitantes em direção ao condomínio.

## Saídas

| Saída | Onde? |
| :--: | :--: |
| `cancela_morador` | LED[0] |
| `cancela_visitante` | LED[1] |
| `alarme` | LED[2] |

- A `cancela_morador` indica que a cancela dos moradores está aberta (quando ativada).
- A `cancela_visitante` indica que a cancela dos visitantes está aberta (quando ativada).
- O `alarme` indica a ocorrência de condições anormais.

## Descrição

- Após o `reset`, ambas as cancelas são fechadas imediatamente.

- Para a cancela de moradores:

  - Quando um carro chega em frente à cancela dos moradores, o condutor do carro se identifica através de um sensor de digital. A seguir, o morador tira o dedo do sensor e, caso não haja visitante passando pela cancela, a cancela se abre. A cancela irá esperar que o carro inicie e termine sua passagem por ela. Em seguida, se fechará.

  - Se houver um carro passando pela cancela dos visitantes, a cancela dos moradores só se abrirá quando o visitante passar completamente.

- Para a cancela de visitantes:

  - Quando um carro chega em frente à cancela dos visitantes, o condutor do carro se identifica para o porteiro. A seguir, caso não haja morador passando pela cancela, a cancela se abre. A cancela irá esperar que o carro inicie e termine sua passagem por ela. Em seguida, se fechará.
  
  - Se houver um carro passando pela cancela dos moradores, a cancela dos visitantes só se abrirá quando o morador passar completamente.

- Por simplicidade, suponha que a identificação de moradores e visitantes sempre tenha um resultado positivo.

- Se um carro demorar menos do que 1 ou mais do que 3 ciclos de *clock* para passar completamente por uma das cancelas, o alarme é ativado.

- Se um carro passa por uma das cancelas enquanto ela está fechada, o alarme é ativado imediatamente.

- Depois de ativado, o alarme permanece assim até que o circuito das cancelas sofra *reset*.
