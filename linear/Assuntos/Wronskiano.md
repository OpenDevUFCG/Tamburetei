<h1>Aplicação com o Wronskiano</h1>

Seja
$$y^{'''} - y^{''} + y^{'} - y = e^{-t}sen(t)$$
 
Uma Equação Diferencial Ordinária de Ordem Superior.
Primeiro vamos escrever a equação homogênea asssociada:

$$y^{'''} - y^{''} + y^{'} - y = 0$$

Agora escrevemos o polinômio caracteristico da equação homogênea associada:

$$r^{3} - r^{2} + r - 1 = 0$$

Possíveis raizes (divisores comuns da nossa constante do polinômio): ±1

Para r = 1:

$$1^{3} - 1^{2} + 1 - 1 = 0 $$

$$0 = 0$$

Ou seja, r = 1 é raíz.

Usando o método de redução de ordem de Briott-Ruffini temos:

$$r^{3} - r^{2} + r - 1 = (r - 1)(r^{2} + 1)$$

$$r^{2} + 1 = 0 => r = ±i$$

$$Raizes: r1 = 1, r2 = i, r3 = -i$$

### Solução Geral da Equação Homogênea Associada:

$$y(t) = C1e^{t} + C2cos(t) + C3sen(t) + P(t)$$ 

Determinando a equação particular por variações de parâmetros.

Sendo 

$$y1 = e^{t}$$

$$y2 = cos(t)$$

$$y3 = sen(t)$$

Aplicando o Wronskiano:

$$
W[y1, y2, y3] = det \begin{bmatrix}
e^{t} & cos(t) & sen(t)\\
e^{t} & -sen(t) & cos(t)\\
e^{t} & -cos(t) & -sen(t)
\end{bmatrix} = 2e^{t}(sen^{2}(t) + cos^{2}(t)) = 2e^{t} ≠ 0$$

Ou seja, ela nunca se anula.

Sendo 

$$g(t) = e^{-t}sen(t)$$
Iremos determinar W1(t):

$$
W1(t) = det \begin{bmatrix}
0 & cos(t) & sen(t)\\
0 & -sen(t) & cos(t)\\
e^{-t}sen(t) & -cos(t) & -sen(t)
\end{bmatrix} = e^{-t}sen(t)cos^{2}(t) + e^{-t}sen^{3}(t)
$$

$$W1(t) = e^{-t}sen(t)(cos^{2}(t) + sen^{2}(t))$$

$$W1(t) = e^{-t}sen(t)$$

<li>Determinando u(t):</li>

$$u(t) = \int \frac {W1}{W} = \int \frac {e^{-t}sen(t)}{2e^{t}} dt$$

$$u(t) = \int \frac {W1}{W} = \frac{1}{2} \int e^{-2t}sen(t) dt$$



$$s = sen(t)$$

$$ds = cos(t) dt$$

$$dk = e^{-2t} dt$$

$$k = -e^{-2t}/2$$


$$u(t) = \frac{1}{2} \int e^{-2t}sen(t) dt = \frac{-sen(t)e^{-2t}}{2} + \frac{1}{2} \int e^{-2t}cos(t)dt$$


$$o = cos(t)$$

$$do = -sen(t) dt$$

$$dp = e^{-2t} dt$$

$$p = \frac{-e^{-2t}}{2}$$

$$u(t) = \frac{1}{2} \int e^{-2t}sen(t) dt = \frac{-sen(t)e^{-2t}}{2} + \frac{1}{2} (\frac{-e^{-2t}cos(t)}{2} - \frac{1}{2} \int e^{-2t}sen(t)dt)$$

$$u(t) = \frac{1}{2} \int e^{-2t}sen(t) dt = \frac{-sen(t)e^{-2t}}{2} -\frac{-e^{-2t}cos(t)}{4} - \frac{1}{4} \int e^{-2t}sen(t)dt$$

$$u(t) = \frac{3}{4} \int e^{-2t}sen(t) dt = \frac{-sen(t)e^{-2t}}{2} -\frac{-e^{-2t}cos(t)}{4}$$

$$u(t) = \int e^{-2t}sen(t) dt = \frac{4}{3} [\frac{-sen(t)e^{-2t}}{2} -\frac{-e^{-2t}cos(t)}{4}]$$

$$u(t) = \int e^{-2t}sen(t) dt = [\frac{2sen(t)e^{-2t}}{3} -\frac{-e^{-2t}cos(t)}{3}] + C$$

$$u(t) = [\frac{2sen(t)e^{-2t}}{3} -\frac{-e^{-2t}cos(t)}{3}] + C$$





### <li>Determinando W2(t):</li>

$$
W2(t) = det \begin{bmatrix}
e^{t} & 0 & sen(t)\\
e^{t} & 0 & cos(t)\\
e^{t} & e^{-t}sen(t) & -sen(t)
\end{bmatrix} = sen(t)(sen(t) + cos(t)) = sen^{2}(t) - sen(t)cos(t) ≠ 0
$$

$$
W2(t) = sen^{2}(t) - sen(t)cos(t)
$$

Determinando v(t):

$$
v(t) = \int \frac {W2}{W} dt =  \int \frac {sen^{2}(t) - sen(t)cos(t)}{2e^{t}} dt
$$

Sabemos que sen(2t) = 2sen(t)cos(t)
Assim,

$$\frac{sen(2t)}{2} = sen(t)cos(t)$$

$$v(t) = \int \frac {W2}{W} dt = \int \frac {(1 - cos(2t))}{4e^{t}} dt - \int \frac{sen(2t)}{4e^{t}} dt$$

$$v(t) = \int \frac {W2}{W} dt = \frac {1}{4} \int \frac{(1 - cos(2t)) - sen(2t)}{e^{t}} dt$$

$$v(t) = \int \frac {W2}{W} dt = \frac {1}{4} \int (1 - cos(2t) - sen(2t))e^{-t} dt$$

$$v(t) = \int \frac {W2}{W} dt = \frac {1}{4} \int (e^{-t} - e^{-t}cos(2t) - e^{-t}sen(2t)) dt$$

$$v(t) = \int \frac {W2}{W} dt = \frac {-e^{-t}}{4} - \frac{1}{4} \int e^{-t}cos(2t) dt - \frac{1}{4}\int e^{-t}sen(2t) dt$$

$$v(t) = \int \frac {W2}{W} dt = \frac {-e^{-t}}{4} - \frac{1}{4} g - \frac{1}{4}h$$

Resolvendo g:

$$g = \int e^{-t}cos(2t) dt$$

$$u = e^{-t}$$

$$du = -e^{-t}$$

$$dv = cos(2t)$$

$$g = \int cos(2t) dt = \frac{sen(2t)}{2} + C$$

$$g = \frac{1}{4} \int e^{-t}cos(2t) dt = \frac{e^{-t}sen(2t}{2} + \frac{1}{2} \int e^{-t}sen(2t) dt$$

$$a = e^{-t}$$

$$da = -e^{-t}$$

$$db = sen(2t)$$

$$b = \frac{-cos(2t)}{2}$$

$$g = \int e^{-t}cos(2t) dt= \frac{e^{-t}sen(2t)}{2} + \frac{1}{2} (\frac{-e^{-t}cos(2t)}{2} - \frac{1}{2}\int e^{-t}cos(2t) dt)$$

$$g = \int e^{-t}cos(2t) dt= \frac{e^{-t}sen(2t)}{2} + \frac{-e^{-t}cos(2t)}{4} - \frac{1}{4}\int e^{-t}cos(2t) dt$$

$$g = \frac{5}{4}\int e^{-t}cos(2t) dt= \frac{e^{-t}sen(2t}{2} + \frac{-e^{-t}cos(2t)}{4}$$

$$g = \int e^{-t}cos(2t) dt= \frac{4}{5}[\frac{e^{-t}sen(2t)}{2} + \frac{-e^{-t}cos(2t)}{4}] $$

$$g = \int e^{-t}cos(2t) dt= [\frac{2e^{-t}sen(2t)}{5} + \frac{-e^{-t}cos(2t)}{5}] $$

$$g = [\frac{2e^{-t}sen(2t)}{5} + \frac{-e^{-t}cos(2t)}{5}] $$

Determinando h:

$$h = \int e^{-t}sen(2t) dt$$

$$e = e^{-t}$$

$$de = -e^{-t}$$

$$df = sen(2t) dt$$

$$f = \int sen(2t) dt = \frac{-cos(2t)}{2} + C$$

$$h = \int e^{-t}sen(2t) dt = \frac{-e^{-t}cos(2t)}{2} - \frac{1}{2} \int cos(2t)e^{-t} dt$$

$$i = e^{-t}$$

$$di = -e^{-t}$$

$$dj = cos(2t) dt$$

$$j = \int cos(2t) dt = \frac{sen(2t)}{2} + C$$

$$h = \int e^{-t}sen(2t) dt = \frac{-e^{-t}cos(2t)}{2} - \frac{1}{2} (\frac{e^{-t}sen(2t)}{2} + \frac{1}{2}\int sen(2t)e^{-t}dt)$$

$$h = \int e^{-t}sen(2t) dt = \frac{-e^{-t}cos(2t)}{2} - \frac{e^{-t}sen(2t)}{4} -\frac{1}{4}\int sen(2t)e^{-t}dt$$

$$h = \frac{5}{4} \int e^{-t}sen(2t) dt = \frac{-e^{-t}cos(2t)}{2} - \frac{e^{-t}sen(2t)}{4}$$

$$h = \int e^{-t}sen(2t) dt = \frac{4}{5}[\frac{-e^{-t}cos(2t)}{2} - \frac{e^{-t}sen(2t)}{4}]$$

$$h = \int e^{-t}sen(2t) dt = [\frac{-2e^{-t}cos(2t)}{5} - \frac{e^{-t}sen(2t)}{5}] + C$$

$$h = [\frac{-2e^{-t}cos(2t)}{5} - \frac{e^{-t}sen(2t)}{5}]$$

Como 

$$v(t) = \int \frac {W2}{W} dt = \frac {-e^{-t}}{4} - \frac{1}{4} g - \frac{1}{4}h$$

$$v(t) = \frac {-e^{-t}}{4} - \frac{1}{4} ([\frac{2e^{-t}sen(2t)}{5} + \frac{-e^{-t}cos(2t)}{5}]) - \frac{1}{4}([\frac{-2e^{-t}cos(2t)}{5} - \frac{e^{-t}sen(2t)}{5}])$$

$$v(t) = [\frac {-e^{-t}}{4} - \frac{e^{-t}sen(2t)}{20} + \frac{3e^{-t}cos(2t)}{20}]$$

### <li>Achando w(t)</li>

$$
w3(t) = det \begin{bmatrix}
e^{t} & cos(t) & 0\\
e^{t} & -sen(t) & 0\\
e^{t} & -cos(t) & e^{-t}sen(t)
\end{bmatrix} = sen(t)(-sen(t) - cos(t)) = -sen^{2}(t) - sen(t)cos(t)
$$

$$w(t) = \int \frac{w3}{w} dt = \int [\frac{-sen^{2}(t)}{2e^{t}} - \frac{sen(t)cos(t)}{2e^{t}}] dt$$

$$w(t) = \int \frac{w3}{w} dt = \int [\frac{-(1 - cos(2t))}{4e^{t}} - \frac{sen(2t)}{4e^{t}}] dt$$

$$w(t) = \int \frac{w3}{w} dt = \frac{1}{4} \int [\frac{-(1 - cos(2t))}{e^{t}} - \frac{sen(2t)}{e^{t}}] dt$$ 

$$w(t) = \int \frac{w3}{w} dt = \frac{-1}{4} (\int [\frac{(1 - cos(2t))}{e^{t}} + \frac{sen(2t)}{e^{t}}] dt)$$ 

$$w(t) = \int \frac{w3}{w} dt = \frac{-1}{4} (\int -e^{-t} dt - \int \frac{cos(2t)}{e^{t}} dt+ \int \frac{sen(2t)}{e^{t}}dt)$$

$$w(t) = \int \frac{w3}{w} dt = \frac{-1}{4} (\int -e^{-t} dt - \int \cos(2t)e^{-t} dt + \int sen(2t)e^{-t} dt)$$ 

Como calculamos antes, 

$$\int e^{-t}cos(2t) dt = [\frac{2e^{-t}sen(2t)}{5} + \frac{-e^{-t}cos(2t)}{5}] $$

$$\int e^{-t}sen(2t) dt = [\frac{-2e^{-t}cos(2t)}{5} - \frac{e^{-t}sen(2t)}{5}] + C$$

$$w(t) = \int \frac{w3}{w} = \frac{-1}{4} (-e^{-t} - [\frac{2e^{-t}sen(2t}{5} + \frac{-e^{-t}cos(2t)}{5}] + [\frac{-2e^{-t}cos(2t)}{5} - \frac{e^{-t}sen(2t)}{5}])$$ 

$$w(t) = \int \frac{w3}{w} = \frac{e^{-t}}{4} + \frac{3e^{-t}sen(2t)}{20} + \frac{e^{-t}cos(2t)}{20}$$

$$w(t) = [\frac{e^{-t}}{4} + \frac{3e^{-t}sen(2t)}{20} + \frac{e^{-t}cos(2t)}{20}]$$

### Equação Particular da EDO:

$$Yp(t) = u(y1) + v(y2) + w(y3)$$

$$Yp(t) = [\frac{2sen(t)e^{-2t}}{3} -\frac{-e^{-2t}cos(t)}{3}].e^{t} + [\frac {-e^{-t}}{4} - \frac{e^{-t}sen(2t)}{20} + \frac{3e^{-t}cos(2t)}{20}].cos(t) + [\frac{e^{-t}}{4} + \frac{3e^{-t}sen(2t)}{20} + \frac{e^{-t}cos(2t)}{20}].sen(t)$$ 

$$y(t) = C1e^{t} + C2cos(t) + C3sen(t) + P(t)$$

### Solução Geral da nossa EDO:

$$y(t) = C1e^{t} + C2cos(t) + C3sen(t) + [\frac{2sen(t)e^{-2t}}{3} -\frac{-e^{-2t}cos(t)}{3}].e^{t} + [\frac {-e^{-t}}{4} - \frac{e^{-t}sen(2t)}{20} + \frac{3e^{-t}cos(2t)}{20}].cos(t) + [\frac{e^{-t}}{4} + \frac{3e^{-t}sen(2t)}{20} + \frac{e^{-t}cos(2t)}{20}].sen(t)$$


