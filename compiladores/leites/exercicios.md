# Conjunto de exercicios para Compiladores

Esse documento trás exercicios feitos no semestre 2019.1, alguns são descrições de questões que caiu em prova, para estes, é marcado com "dois asteriscos" depois do número da questão.

## Primeiro Estágio


1) \*\* Um código em Java pequeno para achar erros léxicos e sintáticos

2) \*\* A partir da expressão regular ``(aa|bb)*a(a|b)*``, criar o DFA equivalente

![Questão 2 - parte 1](https://imgur.com/zkL7OdU.png)
![Questão 2 - parte 2](https://imgur.com/vaPuEU3.png)
![Questão 2 - parte 3](https://imgur.com/f54xuTV.png)

3) \*\* A partir de uma gramática dada, calcular os first, follow e gerar a tabela de acordo com o algoritmo de análise descedente.

![Questão 3 - parte 1](https://imgur.com/RgI4JaR.png)
![Questão 3 - parte 2](https://imgur.com/TIqZw5W.png)
![Questão 3 - parte 2](https://imgur.com/PKRuOHB.png)
![Questão 3 - parte 2](https://imgur.com/b2hHJFA.png)
![Questão 3 - parte 2](https://imgur.com/FseOCtj.png)

4) \*\* Para a mesma gramática da questão 3, calcular o closure e GOTO e preencher a primeira linha da tabela

5) Converta a expressão regular ``(aa|bb)*a(a|b)*`` (Sendo Σ = {a,b} o alfabeto considerado) para um NFA, usando o algoritmo McNaughton-Yamada-Thompson. Mostre o passo a passo da construção do NFA.

![Questão 5 - parte 1](https://imgur.com/gNr2ubX.png)

6) Converta a expressão regular ``bba*(a|b)`` (Sendo Σ = {a,b} o alfabeto considerado) diretamente em um DFA usando as funções firstpos , lastpos e followpos . Indique o cálculo de cada uma destas funções e sua aplicação para construir o DFA. Indique também o cálculo da função de transição construída para este DFA.

![Questão 6 - parte 1](https://imgur.com/3ZWSO4H.png)
![Questão 6 - parte 2](https://imgur.com/DqfhnPm.png)
![Questão 6 - parte 3](https://imgur.com/OIMnSs3.png)
![Questão 6 - parte 4](https://imgur.com/9N9EA7N.png)


## Segundo Estágio

7) \*\* DDS do Switch

![Questão 7 - parte 1](https://imgur.com/Zy96VWi.png)
![Questão 7 - parte 2](https://imgur.com/Ypfodn0.png)

8) \*\* Geração de código de 3 endereços com a[i][j]


9) \*\* Verificação de tipos para switch case

10) \*\* Otimização local e global de um código de 3 endereços

11) Especifique a verificação estática (verificação de tipos e de sintaxe) sobre Java, para uma atribuição envolvendo uma variável declarada anteriormente e uma expressão:
1. Aritmética envolvendo duas expressões.
2. Booleana envolvendo (i) duas expressões; ou (ii) uma expressão.
3. Relacional envolvendo duas expressões.

12) Especifique a verificação estática (verificação de tipos e de sintaxe) sobre Java, para uma atribuição envolvendo uma variável declarada anteriormente e uma chamada de método qualquer, cujo valor de retorno deve ser atribuído à variável.

12+1) Traduza a expressão aritmética ``a - (b + c) * d[i]`` para:
1. Quádruplas
2. Triplas

![Questão 13 - parte 1](https://imgur.com/f1pLeun.png)


14) Construa uma DDS capaz de gerar código 03 endereços para as seguintes construções de fluxo de controle:

a)

```
do {
  S1;
  S2;
} while(B)
```

![Questão 14 - parte 1](https://imgur.com/sSKhgXN.png)

b)

```
S1;
for (S2; B; S3 ){
  S4;
  S5;
}
```

![Questão 14 - parte 2](https://imgur.com/pjqqNO9.png)

15)  Gere o código 03 endereços para o código abaixo:

```
if (d[x] > 10){
    m1(); // chamada ao método m1() que retorna void
    z = z – 1;
} else { z = z + 1;}
```

![Questão 15 - parte 1](https://imgur.com/h03RAVD.png)

16) Dado o código em 03 endereços abaixo:
1. Construa o seu respectivo grafo de fluxo
2. Indique, caso exista(m), o(s) conjuntos de nós onde ocorre(m) loop(s) no grafo construído no item anterior
3. Otimize o código eliminando subexpressões comuns locais

```
i = 0
j = 0
L: t1 = i * 8
t2 = a[t1]
t3 = i * 8
t4 = b[t3]
t5 = i
i = t5 + 1
if t2 < t4 goto L
t6 = i * 8
t7 = a[t6]
t8 = b[t1]
x = t8
a[t1] = x
```
![Questão 16 - parte 1](https://imgur.com/rVSQvoS.png)
![Questão 16 - parte 1](https://imgur.com/mRm96aF.png)
![Questão 16 - parte 1](https://imgur.com/bzTRpvO.png)

## Terceiro Estágio

17) \*\* transformar para código objeto usando pilha

18) \*\* transformar para código objeto usando alocação de registradores

19) \*\* meta modelo Java e assembly

20) \*\* transformação com atl ou java

21) ``x = a + b * c``

1. Gere o código de 03 endereços para a entrada acima.
2. Gere o código de máquina a partir do código de 03 endereços gerado na questão anterior.
3. Para cada instrução de código de máquina gerada na questão anterior, indique as mudanças nos descritores de registradores e de endereços, mostrando-os após cada passo da geração de código.

22) Especifique, em ATL, uma transformação capaz de gerar um modelo Assembly a partir dos seguintes elementos em Java:

1. Comando de atribuição entre uma variável e um literal inteiro (Exemplo: x = 5)
2. Comando de atribuição entre uma variável e uma expressão de soma entre dois literais inteiros (Exemplo: x = 5 + 3)
3. Comando condicional que tem como expressão uma expressão relacional entre uma variável do tipo integer e um literal inteiro (Exemplo: if (x > 5) ...)

23) Crie uma gramática abstrata (meta-modelo) para Java – Classes, atributos, métodos e comandos

24) Gere serviços de interfaces sob encomenda e reflexivas para o meta-modelo construído na questão 06.

25) Construa uma gramática abstrata simplificada para Assembly e gere os serviços necessários para construir um gerador de código Assembly.

26) Construa, em pseudo-código, um gerador de código capaz de gerar código assembly a partir de código Java contendo comandos de atribuição, onde valores resultantes de operações aritméticas sejam atribuídos a uma dada variável. Use os serviços providos nas questões 07 e 0

27) Elabore uma arquitetura para um Compilador MDA, destacando todos os artefatos necessários para a sua construção, considerando que o Compilador use uma técnica de transformação baseada em templates , tendo XSLT como linguagem de transformação. Este compilador deve ser capaz de gerar código Assembly a partir de código Java, e, adicionalmente, aplicar algoritmos de otimização sobre DAGs geradas como representação intermediária no Compilador.
