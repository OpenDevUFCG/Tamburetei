---
title: Definição axiomática, probabilidade condicional e independência
---

Feito com base neste [slide](https://drive.google.com/file/d/16xZUxh5myoZMejHGkduMg2iyrn_G0qur/view) e [esse](https://drive.google.com/file/d/1-ZuWC2Ix2gmukjkP4BYoydTcuIJDDrKc/view).

- **Sobre retrospectiva de espaço amostral**:
- Para cada evento A do espaço amostral Ω, associaremos um número real, representado por P(A) e denominado de probabilidade de A que satisfaça os três axiomas a seguir:

1. Axioma 1: 0 <= P(A) <= 1.
2. Axioma 2: P(Ω) = 1.
3. Axioma 3: Se A1, A2, An... é uma sequência de eventos 2 a 2 mutuamente excludentes(disjuntos), ou seja, A1 ∩ A2 = Ø, para todo i != j, então:
- **P(A1 U A2...) = P(A1) + P(A2)...P(An)**.

## Propriedades
- P1: Se Ø denota o conjunto vazio, então P(Ø) = 0.
- P2: Se Ac, então P(Ac) = 1 - P(A).
- P3: Se A C B ( C é o símbolo de contém), então P(A) <= P(B).
- P4: Se A e B são 2 eventos quaisquer, P(A U B) = P(A) + P(B) - P(A ∩ B).
- P5: Se A e B são eventos quaisquer, então:

- ***P(A ∩ Bc) = P(A) - P(A ∩ B)***.
- ***P(Ac ∩ B) = P(B) - P(A ∩ B)***.

- P6: Se A, B e C forem 3 eventos quaisquer, então:

- ***P(A U B U C) = P(A) + P(B) + P(C) - P(A ∩ B) - P(A ∩ C) - P(B ∩ C) + P(A U B U C)***.

### Observações:

- Em algumas situações, a probabilidade de ocorrência de um certo evento pode ser afetada se tivermos alguma informação sobre a ocorrência ou não do outro evento.

- ***P(A / B) --> Probabilidade de A em ocorrência de B***. Sendo assim, o espaço amostral diminuiu!

### Passo a passo para calcular a probabilidade condicional sem diminuir o espaço amostral.

- **P(B / A) = P(A ∩ B) / P(A)**, ou
- **P(A / B) = P(A ∩ B) / P(B)**.

### A cada evento A C Ω associamos dois números.
- P(A), a probabilidade não condionada de A, chamada de probabilidade ***A PRIORI*** de A.
- P(A / B), a probabilidade condicionada de A, desde que algum outro evento B (para qual P(B) > 0) tenha ocorrido, chamando-se de probabilidade ***A POSTERIORI*** de A dado B.

- ***OBSERVAÇÕES***.

- [Propriedades](#Propriedades)
- **As propriedades condionais satisfazem os axiomas das propriedades comuns**.


## Regra do produto de probabilidades

- P(A ∩ B) = P(B) x P(A / B), se P(B) > 0 ou - P(A ∩ B) = P(A) x P(B / A), se P(A) > 0.

### Generalização da regra do produto

- **P(A1 ∩ A2 ∩ A3... An) =  P(A1) x P(A2 / A1) x P(A3 / A1 ∩ A2) x ... P(An / A1 ∩ A2... An-1)**.

## Eventos independentes

- **Dois eventos são independentes se, e somente se:
P(A / B) = P(A) ou P(B / A) = P(B)

### Equivalência

- **P(A ∩ B) = P(A) x P(B)
- **P(Ac ∩ B) = P(Ac) x P(B)
- **P(A ∩ Bc) = P(A) x p(Bc)

Dizemos que eventos aleatórios A, B e C são( coletivamente) independentes se, e somente se:
- P(A ∩ B) = P(A) x P(B)
- P(A ∩ C) = P(A) x P(C)
- P(B ∩ C) = P(B) x P(C), se apenas essas condições forem atendidas, são independentes ***aos pares***.
- P(A ∩ B ∩ C) = P(B) x P(B) x P(C).



