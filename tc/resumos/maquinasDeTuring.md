---
title: Máquinas de Turing
---

> Conheça mais sobre Alan Turing [aqui](https://pt.wikipedia.org/wiki/Alan_Turing).

Os autômatos (finitos ou de pilha) são bons modelos para alguns dispositivos, mas muito restritos para modelar computadores reais. Para este objetivo, utiliza-se as **máquinas de Turing**, capazes de resolver todos os problemas que os computadores conseguem resolver. Consequentemente, os problemas que não podem ser resolvidos por máquinas de Turing estão além dos limites teóricos da computação.

 Ainda que possuam diversas semelhanças com os autômatos, as máquinas de Turing possuem memória infinita (e irrestrita) através de uma fita infinita. Além dessa, as principais diferenças entre esses dois tipos de máquina são:
 
 - A capacidade de ler e escrever na fita infinita.
 - Os estados de aceitação e rejeição têm efeito imediato.
 - O cabeçote da máquina pode se mover em ambas as direções.
 - É possível que o processamento não se encerre nunca (*loop*).

 A definição formal de uma **máquina de Turing (MT)** é uma 7-tupla **<Q, Σ, Γ, δ, q0, qA, qR>**, tal que:

- **Q** é o conjunto de estados.
- **Σ** é o alfabeto da entrada (não contém B).
- **Γ** é o alfabeto da fita, onde B ∈ Γ e Σ ⊂ Γ.
- **δ: Q × Γ → Q × Γ × {E, D}** é a função de transição da máquina de Turing.
- **q0** ∈ Q é o estado inicial da máquina de Turing.
- **qA** ∈ Q é o estado de aceitação da máquina de Turing.
- **qR** ∈ Q é o estado de rejeição da máquina de Turing.

Uma maneira informal de descrever o **funcionamento** de uma máquina de Turing é imaginar que, inicialmente, a fita infinita contém apenas a cadeia de entrada e os demais espaços são "branco" (denotado por **B** ou **ν**). A medida que o processo ocorre, a máquina poderá não só reagir aos símbolos lidos, mas também escrever símbolos na fita caso necessite armazenar informações.

Dá-se o nome de **configuração** ao conjunto de três informações que representam o *status* atual de uma máquina de Turing: o estado atual, o conteúdo da fita e a posição atual do cabeçote. Ainda, diz-se que uma configuração C1 **produz** uma configuração C2 se a máquina de Turing for capaz alcançar C2 a partir de C1 em um único passo.

A coleção de cadeias que uma máquina de Turing M aceita é chamada de **linguagem de M** e denotada por **L(M)**.

Uma linguagem pode ser **Turing-reconhecível** ou **Turing-decidível** se existir uma máquina de Turing que a reconheça ou a decida, respectivamente. A distinção entre essas características se dá pelo fato de um decisor garantir que haverá fim no processamento (aceitação/rejeição), enquanto o reconhecedor pode entrar em *loop*. Portanto, uma linguagem decidível é reconhecível, mas o inverso não é garantido.

## Variações

As **variações** de máquinas de Turing são ambundantes, mas todas reconhecem a mesma classe de linguagens, diz-se então que possuem a mesma **robustez**. Um exemplo simples que permite a percepção dessa característica é garantir ao cabeçote a capacidade de permanecer parado durante uma transição. Ainda que seja uma nova capacidade, ela não adiciona poder à máquina de Turing, dado que seria possível realizar as mesmas tarefas com duas transições distintas.

### Calculadora de Função

É o tipo de variação em que a máquina de Turing não se limita a responder *"sim"* (aceitação) ou *"não"* (rejeição), mas realiza algo a mais. Geralmente a cadeia escrita na fita ao final do processamento é de mais interesse do que a própria aceitação.

### Multifitas

É o tipo de variação em que a máquina de Turing não possui apenas uma fita infinita, mas várias delas (que são utilizadas simultaneamente). É importante compreender que, para toda MT multifita, existe uma máquina MT de fita única equivalente. Na máquina de Turing de fita única, a fita será a concatenação das fitas originais com um símbolo (geralmente **#**) que identifica a divisão entre elas. Ainda, para monitorar a posição do cabeçote em cada fita, é adicionada uma marca ao símbolo atual de cada uma delas.

### Não-Determinística

Assim como nos autômatos finitos, a adição do não-determinismo não representa aumento de poder. É importante compreender que, para toda MT não-determinística, existe uma máquina MT multifita equivalente. Na máquina de Turing equivalente haverão 3 fitas: 

- A primeira fita armazena a cadeia de entrada original, que será copiada para a segunda fita a cada execução. 
- A segunda fita é a memória de trabalho. É nela que serão realizadas as operações referentes à execução em curso.
- A terceira fita atua como registro dos caminhos não-determinísticos que já foram tomados e de qual será seguido na execução em curso.

### Enumerador

Informalmente, um enumerador é uma máquina de Turing com um *"impressora"* acoplada, através da qual são impressas as cadeias que são aceitas. O enumerador irá imprimir a lista de todas as cadeias que compõem sua linguagem, porém, essa listagem não segue nenhuma ordem específica e não está livre de repetições, o que pode levar a um tempo de processamento infinito.

Sua característica mais importante é que uma linguaguem é Turing-reconhecível se, e somente se, existir um enumerador que a enumere.

## Algoritmos

A **Tese de Church-Turing** é uma hipótese sobre a natureza de computadores e sobre que tipo de **algoritmos** eles podem executar. Ela descreve algoritmos através das seguintes características:

- Um algoritmo é um conjunto finito de instruções simples e precisas, que são descritas com um número finito de símbolos.
- A execução do algoritmo não requer inteligência além da necessária para entender e executar as instruções.
- Um algoritmo sempre produz resultado em um número finito de passos.

A partir da tese acima, é possível mostrar que todo algoritmo pode ser representado por uma máquina de Turing. Além disso, tanto as máquinas de Turing quanto os algoritmos podem ser descritos em três níveis:

- **Baixo:** Utiliza a descrição formal e/ou o diagrama de estados.
- **Médio:** Utiliza a descrição de implementação, apresentando o movimento do cabeçote, os símbolos, a gerência da fita e a codificação da entrada.
- **Alto:** Ignora o cabeçote e os símbolos, além de assumir que a entrada pode ser codificada. Dessa forma, apresenta uma ideia mais geral de como funciona a máquina de Turing.