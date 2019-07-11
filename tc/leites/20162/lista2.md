2º Exercício de Teoria da Computação                        
Prof. Andrey Brito

01. Converta os seguintes AFNDs em AFDs equivalentes:
**a.** M = ({q1,q2}, {a,b}, δ, q1, {q1}), onde:

| δ | a | b |
| --- | --- | --- |
| q1 | {q1,q2} | {q2} |
| q2 | ∅ | {q1} |


**b.** N = ({q1,q2,q3}, {a,b}, δ, q1, {q2}), onde δ:

| δ | a | b | λ |
| --- | --- | --- | --- |
| q1 | {q3} | ∅ | {q2}|
| q2 | {q1} | ∅ | ∅ |
| q3 | {q2} | {q2,q3}| ∅ |

1. Em cada caso, construa um autômato finito que reconhece a linguagem gerada pelas seguintes expressões regulares:
   1. (0 ∪ 1)*000(0 ∪ 1)*
   2. (((00)*(11))∪01)*
   3. Σ*aΣ*bΣ*aΣ*
   4. (a ∪ ba ∪ bb)Σ*
   5. ∅*

2. Dado que N1 e N2 são autômatos finitos e que L(N2) = L(N1)*, dê uma definição formal para N2 em termos de N1.

3. Avalie as seguintes alternativas em Verdadeiro (V) ou Falso (F), justificando os itens marcados como falso.

(     ) Se uma linguagem é regular então todas as suas palavras, sejam maiores ou menores que “p” (o comprimento do bombeamento), precisam ser bombeáveis. Ou seja, todas palavras precisam ter uma parte que seria processada em um loop no autômato.
(     ) O Lema do bombeamento é utilizado para confirmar que uma certa linguagem é regular.
(       ) A linguagem 0n1n não é regular (n>0)
(       ) As linguagens 0²1² e 0n1n (0<n<5) são regulares.
