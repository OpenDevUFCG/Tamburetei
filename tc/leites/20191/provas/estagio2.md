---
title: 2ª Prova
---

- **Disciplina:** Teoria da Computação
- **Período:** 2019.1

## Aviso!

As questões apresentadas a seguir são descrições baseadas em relatos de um ou mais alunos que fizeram tal avaliação. Logo, não há garantia de que os enunciados sejam iguais aos originais, tampouco que estejam livres de erros. Esteja ciente dessas considerações ao utilizar esse material!

## Questões

#### Questão 1 

Transforme o AFND abaixo em uma ER.

![](https://user-images.githubusercontent.com/14113480/61055213-5fa55180-a3c7-11e9-8bf2-09ea4c07142f.png)

#### Questão 2 

Considerando a expressão regular definida por `R = (1 U (001)*)`, transforme-a em um AFND.

#### Questão 3 

Projete a gramática livre-de-contexto para a seguinte linguagem: `(0^k)(1^j)(2^k)`, onde `i = k`, `i > 0` e `j = 1`.

#### Questão 4

Responda as alternativas com verdadeiro ou falso, justificando a sua escolha.  

**a)** ( ) A linguagem **L =** *{ww | w E {0,1}\*}* é regular uma vez que é possível escolher a palavra `w = {(0^p)(0^p)}` que pertence à linguagem e bombeá-la com `x = λ`, `y = 00` e `z = (O^(p-2))(0^p)`. Assim, a palavra resultante ainda pertencerá a L.  

**b)** ( ) Intuitivamente a linguagem **L =** *{w E {0,1}\* | w tem a mesma quantidade de símbolos 0 e 1}* não é regular, pois um autômato não teria como contar e comparar a quantidade de símbolos 0 e símbolos 1. Pelo mesmo motivo, a linguagem L2, tal que **L2 =** *{w E {0,1}\* | w tem a mesma quantidade de ocorrências de substrings 01 e 10}* não é regular.
  
**c)** ( ) A gramática `S -> SS | (S) | ()` é ambígua. 

**d)** ( )  Algumas gramáticas livres-de-contexto podem ser convertidas em autômatos finitos.