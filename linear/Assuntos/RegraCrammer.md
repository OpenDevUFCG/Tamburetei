---
title: Regra de Crammer
---

### O que é a Regra de Crammer?

A Regra de Crammer é uma das formas de achar os valores dos coeficeintes em um sistema linear usando determinantes.

### Como é utilizado?

Considere o sistema de equações a seguir:

$$
\begin{cases} `a11x+a12y+a13z=u\\\\a21x+a22y+a23z=v\\\\a31x+a32y+a33z=w` \end{cases}
$$

Dado o sistema, iremos chamar a <r>**matriz dos coeficientes**</r> de A: 

$$A = \begin{bmatrix}
a11 & a12 & a13\\
a21 & a22 & a23\\
a31 & a32 & a33
\end{bmatrix}$$

E seja B a matriz dos termos indepedentes:

$$B = \begin{bmatrix}
u\\
v\\
w
\end{bmatrix}$$

### Primeiro, devemos fazer o determinante da Matriz dos coeficientes:
Seja Δ o determinante da matriz A.

$$Δ = det\begin{vmatrix}
a11 & a12 & a13\\
a21 & a22 & a23\\
a31 & a32 & a33
\end{vmatrix} = $$

```Δ = a11 . a22 . a33 + a12 . a23 . a31 + a13 . a21 . a32 - a31 . a22 . a13 - a32 . a23 . a11 - a33 . a21 . a12```

Ao determinar o valor de Δ através do determinante da matriz dos coeficientes, vamos fazer a seguinte operação:

Substitua a matriz dos termos independentes de B na primeira coluna da matriz dos coeficientes e em seguida, calcule o determinante.
Seja Δx 

$$Δx = det\begin{vmatrix}
u & a12 & a13\\
v & a22 & a23\\
w & a32 & a33
\end{vmatrix} = $$

```Δx = u . a22 . a33 + a12 . a23 . w + a13 . v . a32 - w . a22 . a13 - a32 . a23 . u - a33 . v . a12```


Determinando x:

$$x = \frac{Δx}{Δ}$$

Substitua a matriz dos termos independentes de B na segunda coluna da matriz dos coeficientes e em seguida, calcule o determinante.
Seja Δy 

$$Δy = det\begin{vmatrix}
a11 & u & a13\\
a21 & v & a23\\
a31 & w & a33
\end{vmatrix} = $$

```Δy = a11 . v . a33 + u . a23 . a31 + a13 . a21 . w - a21 . v . a13 - w . a23 . a11 - a33 . a21 . u```


Determinando y:

$$y = \frac{Δy}{Δ}$$

Substitua a matriz dos termos independentes de B na terceira coluna da matriz dos coeficientes e em seguida, calcule o determinante.
Seja Δz 

$$Δz = det\begin{vmatrix}
a11 & a12 & u\\
a21 & a22 & v\\
a31 & a32 & w
\end{vmatrix} = $$

```Δz = a11 . a22 . w + a12 . v . a31 + u . a21 . a32 - a21 . a22 . u - a32 . v . a11 - w . a21 . a12```

Determinando z:

$$z = \frac{Δz}{Δ}$$

E assim, determinamos x, y e z de tal modo que satisfaça o nosso sistema de equações.

**Lembre-se de que para até o R³ (espaço euclidiano tridimensional) você pode usar a Regra de Sarrus e para para qualquer espaço euclidiano, você pode usar o método de Laplace para calcular o determinante.**
