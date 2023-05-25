<h1>Matriz dos Cofatores</h1>

Embora esse conteúdo deixe algumas dúvidas sobre a sua aplicação na Álgebra Linear, o cofator tem aplicação direta para realização do cálculo de determinates de matrizes pelo método de Laplace.

Seja a matriz A, a matriz dos coeficientes:

$$A = \begin{bmatrix}
a11 & a12 & a13\\
a21 & a22 & a23\\
a31 & a32 & a33
\end{bmatrix}$$

Para se calcular a matriz dos cofatores, você deve-se calcular os cofatores de todos elementos da matriz, se você tiver uma matriz (NxN), então voce terá que calcular (NxN) cofatores.

Suponha a matriz acima e que queremos verificar a matriz dos cofatores de A.

A matriz dos cofatores de A será da seguinte forma:

$$Cof(A)= \begin{bmatrix}
Δ11 & Δ12 & Δ13\\
Δ21 & Δ22 & Δ23\\
Δ31 & Δ32 & Δ33
\end{bmatrix}$$

Para cada elemento da matriz dos cofatores valerá a seguinte relação:
Suponha que queremos descobrir o elemento Δ13. Assim, iremos fazer a seguinte relação: (-1)<sup>(1+3)</sup> vezes o determinte da matriz A mas excluindo a primeira linha e terceira coluna.

$$Δ13 = {(-1)^{(1+3)}} det
\begin{bmatrix}
a21 & a22\\
a31 & a32
\end{bmatrix}$$

Por definição, a base é (-1) mas o expoente sempre muda. O expoente é a soma dos índices de cada elemento da matriz, o primeiro índice nos indica o número da linha da matriz e o segundo índice nos indica o número da coluna da matriz no qual está aquele elemento que iremos trabalhar.
E assim,

### Δ11 seria a potência (1 + 1) e o determinante excluindo a primeira linha e primeira coluna.

$$Δ11 = {(-1)^{(1+1)}} det
\begin{bmatrix}
a22 & a23\\
a32 & a33
\end{bmatrix}$$

### Δ12 seria a potência (1 + 2) e o determinante excluindo a primeira linha e segunda coluna.

$$Δ12 = {(-1)^{(1+2)}} det
\begin{bmatrix}
a21 & a23\\
a31 & a33
\end{bmatrix}$$

### Δ13 seria a potência (1 + 3) e o determinante excluindo a primeira linha e terceira coluna.

$$Δ13 = {(-1)^{(1+3)}} det
\begin{bmatrix}
a21 & a22\\
a31 & a32
\end{bmatrix}$$

### Δ21 seria a potência (2 + 1) e o determinante excluindo a segunda linha e primeira coluna.

$$Δ21 = {(-1)^{(2+1)}} det
\begin{bmatrix}
a12 & a13\\
a32 & a33
\end{bmatrix}$$

### Δ22 seria a potência (2 + 2) e o determinante excluindo a segunda linha e segunda coluna.

$$Δ22 = {(-1)^{(2+2)}} det
\begin{bmatrix}
a11 & a13\\
a31 & a33
\end{bmatrix}$$

### Δ23 seria a potência (2 + 3) e o determinante excluindo a segunda linha e terceira coluna.

$$Δ23 = {(-1)^{(2+3)}} det
\begin{bmatrix}
a11 & a12\\
a31 & a32
\end{bmatrix}$$

### Δ31 seria a potência (3 + 1) e o determinante excluindo a terceira linha e primeira coluna.

$$Δ31 = {(-1)^{(3+1)}} det
\begin{bmatrix}
a12 & a13\\
a22 & a23
\end{bmatrix}$$

### Δ32 seria a potência (3 + 2) e o determinante excluindo a terceira linha e segunda coluna.

$$Δ32 = {(-1)^{(3+2)}} det
\begin{bmatrix}
a11 & a13\\
a21 & a23
\end{bmatrix}$$

### Δ33 seria a potência (3 + 3) e o determinante excluindo a terceira linha e terceira coluna.

$$Δ33 = {(-1)^{(3+3)}} det
\begin{bmatrix}
a11 & a12\\
a21 & a22
\end{bmatrix}$$

Em seguida, substitua cada cofator na matriz dos cofatores abaixo.

$$Cof(A)= \begin{bmatrix}
Δ11 & Δ12 & Δ13\\
Δ21 & Δ22 & Δ23\\
Δ31 & Δ32 & Δ33
\end{bmatrix}$$

**Além disso, caso queira calcular a adjunta "Adj(A)" da matriz A, basta apenas fazer a matriz transposta do cofator.**
**E caso queira a matriz inversa, basta fazer a seguinte operação**
$$Adj(A) = Cof(A)^{T}$$
$$A^{-1} = \frac{1}{det(A)} . Adj(A)$$

Lembrando que para calcular inversas, temos 3 métodos e uma delas usa a matriz dos cofatores.
