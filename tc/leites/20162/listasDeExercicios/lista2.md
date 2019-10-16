---
title: Lista de Exercícios 2
---

- **Disciplina:** Teoria da Computação
- **Período:** 2016.2

## Questões

#### Questão 1 

Converta os seguintes AFNDs em AFDs equivalentes:

**a)** **M =** *({q1,q2}, {a,b}, δ, q1, {q1})*, onde:

| *δ* | a | b |
| --- | --- | --- |
| q1 | {q1,q2} | {q2} |
| q2 | *∅* | {q1} |


**b)** **N =** *({q1,q2,q3}, {a,b}, δ, q1, {q2})*, onde *δ*:

| *δ* | a | b | *λ* |
| --- | --- | --- | --- |
| q1 | {q3} | *∅* | {q2}|
| q2 | {q1} | *∅* | *∅* |
| q3 | {q2} | {q2,q3}| *∅* |

#### Questão 2 

Em cada caso, construa um autômato finito que reconhece a linguagem gerada pelas seguintes expressões regulares:

**a)** `(0 ∪ 1)*000(0 ∪ 1)*`

**b)** `(((00)*(11))∪01)*`

**c)** `Σ*aΣ*bΣ*aΣ*`

**d)** `(a ∪ ba ∪ bb)Σ*`

**e)** `∅*`

#### Questão 3 

Dado que N1 e N2 são autômatos finitos e que **L(N2) = L(N1)\***, dê uma definição formal para N2 em termos de N1.

#### Questão 4

Avalie as seguintes alternativas como verdadeiro (V) ou falso (F), justificando os itens marcados como falso.

**a)** (  ) Se uma linguagem é regular então todas as suas palavras, sejam maiores ou menores que "p" (o comprimento do bombeamento), precisam ser bombeáveis. Ou seja, todas palavras precisam ter uma parte que seria processada em um loop no autômato.  

**b)** (  ) O lema do bombeamento é utilizado para confirmar que uma certa linguagem é regular.  

**c)** (  ) A linguagem `(0^n)(1^n)`, onde `n > 0` não é regular.  

**d)** (  ) As linguagens `0²1²` e `(0^n)(1^n)`, sendo `0 < n < 5`, são regulares.  
