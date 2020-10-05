---
title: Forma Normal Conjuntiva
---

# Pra quê serve

CNF é a representação mais simples de uma fórmula proposicional. Sendo apenas várias conjunções(^) de disjunções(v). 

Exemplo: (p v q) ^ (q v ¬p) ^ ....

Ela serve para verificar **validade**.

Se um disjunção tem o par de literal complementar: a v ¬a, ela vai ser sempre verdadeira. A fórmula só é válida se **todas** as disjunções tiverem um par de literal complementar.

### Transformando em CNF

Normalmente, a informação é dada através de tabela verdade e traduzimos da seguinte forma:

- Cada linha é uma disjunção;
- Se p é F, então fica *p*.
- Se p é T, fica *¬p*.

Exemplo: T | T | F → ¬p v ¬q v r

Para transformar para o formato CNF, devemos seguir 3 passos:

1. Remover implicação ( p→q ⇒ ¬p v q)
2. Remover negações complexas ( ¬¬p → ¬(p v q) ⇒ p → ¬p ^ ¬q )
3. Aplicar Distributiva ( (p v q) v (¬p ^ ¬q) ⇒ (p v q v ¬p) ^ (p v q v ¬q) )