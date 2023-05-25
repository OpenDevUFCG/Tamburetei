# Números Inteiros

## Algoritmo da divisão
toda divisão pode ser expressa no seguinte formato:
    **a = bq + r** 

*Onde,
    a = dividendo
	b = divisor
	q = quociente
	r = resto*

*Obs. r pertence a N; q e r são únicos; 0 <= r <= |b|*

## Divisibilidade
Tendo a e b pertencentes a Z e b != 0, b divide a ( b|a ), se a = bk, com k pertencente a Z. Assim, representamos:

- b | a  → b divide a // a é divisível por b
- b ∤ a → b não divide a // a não é divisível por b

### MDC
- É definido como o maior divisor comum entre dois números inteiros;
- mdc(a,b) = c, c é o maior divisor em comum entre a e b, isso significa que:<br>
    - c|a e c|b;
    - se d|a e d|b, então d|c, para um d inteiro qualquer;
</br>
- Para calcular o mdc, temos duas opções:

```txt
    - Se b | a, mdc(a,b) = b
    - Se b ∤ a, faz-se algoritmo de Euclides
```

#### Algoritmo de Euclides
É um algoritmo para encontrar o mdc, que consiste em divisões sucessivas até encontrar o resto 0. 

*Ex1.* mdc(14,90)

**90** = **14** x 6 + 6 
**14** = **6** x 2 + 2
**6** = **2** x 3 + 0 

- Quando chegamos no resto 0, podemos parar o algoritmo.
- O mdc será o último resto diferente de zero, nesse exemplo, mdc(14,90) = 2

*Ex2.* mdc(200,144)

**200** = **144** x 1 + 56
**144** = **56** x 2 + 36
**56** = **36** x 1 + 20
**36** = **20** x 1 + 16
**20** = **16** x 1 + 4
**16** = **4** x 4 + 0 

mdc(200,144) = 4

## Números primos

- São números divisíveis por 1 e ele mesmo;
- Todo número ou é primo ou é composto por primos.

- **Como saber se um número é primo sem precisar fatorá-lo?**
	- ir até a raíz quadrada do número, dividindo-o pelos primos no intervalo (2-raíz quadrada do número)

*Ex1.* 21 é primo?
<p align="left"> 
  <img src="https://latex.codecogs.com/gif.download?4%3C%5Csqrt%7B21%7D%3C5">
</p>

- primos até 5: 2;3;5

2|21? não
3|21? sim → logo 21, não é primo, por 3 é um divisor dele

*Ex2.* 29 é primo?
<p align="left"> 
  <img src="https://latex.codecogs.com/gif.download?5%3C%5Csqrt%7B29%7D%3C6">
</p>

- primos até 6: 2,3,5

2|29? não
3|29? não
5|29? não
Logo, 29 é primo.
