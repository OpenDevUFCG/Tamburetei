---
title: Conceitos iniciais
---

Feito baseando-se neste [slide](https://drive.google.com/file/d/10GVEsvGkBSQPMtB0i2p02zQO8D95QFHB/view) e [esse](https://drive.google.com/file/d/1j6BX4wBWKtZwoAHzoyYeraTwlRaMw56s/view).

## Tipos de experimentos

- **Experimentos determinísticos**: são experimentos que ao serem repetidos sob as mesmas condições possuem o mesmo resultado.
- **Experimentos aleatórios**: são os experimentos que ao que serem repetidos nas mesmas condições, refletem em resultados distintos.

## Conceitos iniciais

### Objetivo:
Desenvolver modelos que tem a possibilidade de serem utilizados para o estudo de experimentos aleatórios.

### Definições importantes (retrospectiva):

- **Espaço amostral**: 
É conjunto de todos os possíveis resultados de um experimento aleatório.
Notação: Ω

- **Evento**:
Seja Ω um espaço amostral associado ao evento estudado, logo, o evento é qualquer subconjunto desse espaço amostral.

### Bom lembrar:

- Dizemos que um evento A ocorre se resultado do experimento w pertencer ao evento A. Caso contrário, A não existe.
- Como os eventos do espaço amostral são conjuntos, toda o conceito aplicados em conjuntos pode ser relembrado por aqui.


## A e B são dois eventos, então:
- **A U B**: ocorrerá se, e somente se, A ocorrer, ou B ocorrer ou ambos ocorrerem.
- **A ∩ B**: ocorrerá se, e somente se, A e B ocorrerem simultaneamente.
- **Ac** são eventos que A não ocorre, logo:

### Leis de Morgan
**(A U B)c** | **(A ∩ B)c** 
--- | --- 
Ac ∩ Bc | Ac U Bc 

- A e B são ditos mutuamente excludentes (disjuntos) se eles NÃO puderem ocorrer simultaneamente, ou seja, A ∩ B = Ø 

## Definição de probabilidade frequentista e clássica:

### IMPORTANTE:
- **Fenômeno aleatório**
- Frequências de cada evento é importante. Em particular, as frequências relativas são estimativas de probabilidades de ocorrências de certos eventos de interesse.
- Com suposições adequadas, é possível modelar um fenômeno aleatório através de um modelo teórico que denominamos de modelo probabilístico.

### Passos:

1. Lançar o dado n vezes e depois contar o número ni de vezes em que ocorre a fase sucesso, sendo i = 1, 2, 3, 4, 5, 6. (finito)
2. As proporções(***ni/n***) determinam a distribuição de frequências do experimento realizado.
  - m != n traria uma distribuição diferente, mas bem parecida provavelmente
3. Quando o objeto a ser estudado estiver em condições normais, a probabilidade entre eles tende a ser igual ou bastante parecida.
  - a soma das frequências é igual a ***1***.   

- **Obs**:
- Um espaço onde seja feito de números de casos finitos e com a mesma probabilidade são conhecidos por:***Espaços finitos e equiprováveis***.

- Uma maneira de calcular a probabilidade de um evento é em termos de sua ***frequência relativa***.

***F(A) = n(A) / n****, sendo ***n(A)*** a quantidade de vezes que o evento A ocorreu e ***n*** o numéro de repetições.

## Definição frequentista de probabilidade

### quanto maior a quantidade de repetições, maior a veracidade da probabilidade.

***P(A) = lim n -> inf F(A)***;

### Observação:
1. 0 <= F(A) <= 1;
2. F(A) = 1, se, e somente se, A ocorrer em todas as n repetições.
3. F(A) = 0, quando A nunca ocorrer nas n repetições.
4. Se A e B forem dois eventos mutuamente excludentes, então:

***F(A U B) = F(A) + F(B).

- **Se  Ω for um espaço finito e equiprovável**
P(A) = número de casos favoráveis a A / número de casos possíveis = #A / # Ω, sendo #, a cardinalidade do evento.







