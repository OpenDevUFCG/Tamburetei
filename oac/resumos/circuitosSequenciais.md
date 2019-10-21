---
title: Circuitos Sequenciais
---

<p align = "justify">Um <b>circuito sequencial</b> é aquele cuja saída é função não somente dos valores de entrada atuais, mas também dos valores de entrada no instante de tempo anterior.</p>

## Memórias

<p align = "justify">As memórias constituem o tipo de circuito sequencial mais importante, uma vez que o desenvolvimento computacional e das comunicações digitais só foi possível a partir de sua concepção. Nelas, o conceito de tempo está associado a pulsos de um relógio (<i>clock</i>). Existem dois tipos de memórias, os <b>latches</b> (sensíveis ao nível do sinal do clock) e os <b>flip-flops</b> (sensíveis à transição do sinal do clock).</p>


<p align = "justify">A seguir, as tabelas-verdade simplificadas de alguns latches e flip-flops. O valor <b>Qa</b> representa o valor da saída Q no instante anterior de tempo. Também é possível que existam entradas adicionais (SET e RESET/CLEAR) que, quando ativas, forçam o circuito para estados específicos (Q = 1 e Q = 0, respectivamente).</p>

---

## Latches

<p align = "justify">Os valores das saídas Q e Q' são atualizados sempre que o <i>clock</i> estiver no nível adequado (normalmente em 1).</p>

### Latch RS
**R** | **S** | **Q**  | **Q'** |
:---: | :---:| :---: | :---: |
0 | 0 | Qa | Qa' |
0 | 1 | 0 | 1 |
1 | 0 | 1 | 0 |
1 | 1 | Erro | Erro |

### Latch D
**D** | **Q**  | **Q'** |
:---: | :---:| :---: |
0 | 0 | 1 |
1 | 1 | 0 |

---

## Flip-Flops

<p align = "justify">Os valores das saídas Q e Q' são atualizados sempre que o <i>clock</i> transiciona adequadamente (normalmente de 0 para 1, chamada "subida de clock").</p>

### Flip-Flop JK
**J** | **K** | **Q**  | **Q'** |
:---: | :---:| :---: | :---: |
0 | 0 | Qa | Qa' |
0 | 1 | 0 | 1 |
1 | 0 | 1 | 0 |
1 | 1 | Qa' | Qa |

### Flip-Flop D
**D** | **Q**  | **Q'** |
:---: | :---:| :---: |
0 | 0 | 1 |
1 | 1 | 0 |

### Flip-Flop T (Toggle)
**T** | **Q**  | **Q'** |
:---: | :---:| :---: |
0 | Qa | Qa' |
1 | Qa' | Qa |

---

## Contadores

<p align = "justify">Um <b>contador</b> é um circuito sequencial, construído a partir de flip-flops, que varia por uma sequência pré-determinada de estados sob comando de um <i>clock</i>. Apesar da nomenclatura, esses circuitos são usados não só para contagens, mas também para gerar palavras, dividir frequências, etc. Podem ser classificados por tipo de <b>controle</b> (síncrono ou assíncrono), tipo de <b>contagem</b> (crescente ou decrescente) e por tipo de <b>código</b> (binário, decimal, hexadecimal, etc).</p>

<p align = "justify">Um contador <b>síncrono</b> é aquele em que todos os flip-flops mudam de estado simultaneamente, pois utilizam o mesmo <i>clock</i>. Já em um contador <b>assíncrono</b>, é comum que um flip-flop X use a saída de um flip-flop Y como <i>clock</i>, tornando esse tipo de contador mais lento.</p>

---

### Registradores

<p align = "justify">Um <b>registrador</b> é um circuito sequencial, constituído basicamente por flip-flops, que é utilizado para armazenamento e manipulação de dados. Os registradores <b>paralelos</b> são um conjunto de memórias que podem ser lidas ou escritas simultaneamente, enquanto nos registradores <b>de deslocamento</b> essas operações são realizadas de maneira serial (bit a bit).</p>
