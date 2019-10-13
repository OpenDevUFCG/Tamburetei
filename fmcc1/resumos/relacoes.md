# Fundamentos de Matemática para Ciência da Computação I
## Relações e Funções

### Sumário
 - [Relações](#relações)
 - [Relação Binária](#relação-binária)
 - [Funções](#funções)
 - [Módulo](#módulo)
 - [Busca Incremental](#busca-incremental)
 
### Relações
 - Par: todo conjunto de 2 elementos.
      - Ordenando: (a, b) e (c, d)
      - Igualdade: a=c e b=d.
  - Produto cartesiano: todos os pares ordenados de 2 conjuntos.
      - A = {3, 5} e B = {2,4}
      - AxB = {(3, 2), (3, 4), (5, 2), (5, 4)}
      - BxA = {(2, 3), (2, 5), (4, 3), (4, 5)}
  - Conjunto vazio:
      - AxØ = Ø, ØxB = Ø ou ØxØ = Ø
 
### Relação Binária
- Todo subconjunto R de AxB.
    - R = {(x, y)| condição }
- Domínio: x; Imagem: y.
- Relação Inversa:
    - R = {(2, 3), (4, 5)}
    - R⁻¹ = {(3, 2), (5, 4)}
      
 ### Funções
 - Todo elemento de D tem um associado na Imagem (Contradomínio).
 - Iguais:
      - Domínio: A=C Contradomínio: B=D.
 - Constantes:
      - ∀x ∈ R associa sempre ao mesmo valor c ∈ R.
 - Identidade:
      - ∀x∈R associa o prṕrio x. f(x) = x.
 - Linear
      - ∀x associa-se a ax, a != 0.
 - Afim
      - ∀x ∈ R associa-se a R, a != 0 e b ∈ R.
            - coeficiente a = angular.
            - coeficiente b = linear.
 - Zero da função
      - Imagem nula com x = -b/a
 - Crescente
      - y = f(x) com x1 > x2 e f(x1) < f(x2).
 - Decrescente
      - y = f(x) com x1 < x2 e f(x1) > f(x2)
 - Exponencial
      - f(x) = a^x com a > 0 e a != 1.
 - Teto e Piso
      - Piso: menor inteiro
      - Teto: maior inteiro
 ### Módulo
 #### Várias Sentenças Abertas
      f(x) definida por:
      
      f(x) = x, se x >= 0
            -x, se x < 0
 - Propriedades:
    1. |x| >= 0, ∀x ∈ R
    2. |x| = 0 ⇔ x=0
    3. |x| * |y| = |xy|
    4. |x|² = x², ∀x ∈ R
    5. x < |x|, ∀x ∈ R
    6. |x + y| <= |x| + |y|
    7. |x - y| >= |x| - |y|
    8. |x| <= a e a > 0 ⇔ -a <= x <= a
    9. |x| >= a e a > a ⇔ x <= -a ou x >= a
 - Equações Modulares
    1. |ax² + bx + c| = 1
       ax² + bx + c = 1 e ax² + bx + c = -1
    2. |a| = |b| ⇔ a = b ou a = -b
    
 ### Busca Incremental
 - Alternativa para obter uma raiz quadrada aproximada
 #### Método da Bisseção
    O intervalo é dividido na metade.
    xc = (x1 + x2)/2
 #### Método da Falsa Posição
    Interseção usando uma reta de f(x1) a f(x2).
    xr = x2 - f(x2) * [(x1 - x2)/ ( f(x1) - f(x2) )]
