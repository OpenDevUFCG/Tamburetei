## Decidibilidade

Esse tópico concentra-se em demonstrar que problemas são soluvéis ou não, isto é, quais problemas um computador consegue resolver e quais não.  

Você pode pensar que não é útil saber quais problemas o computador não consegue resolver, mas você verá que isso o ajudará a concentrar seus esforços na simplificação e alteração de problemas que você sabe que não são resolvíveis para todos os casos. Além disso, isso o ajuda a compreender melhor a computação, uma vez que você entende seus limites.

## Linguagens Decidiveis

Uma linguagem é dita **decidível**, se existe uma máquina de turing que a decide. Isto significa que existe um programa que consegue resolver o problema, e para cada entrada do mesmo, consegue retornar um resultado, seja ele de aceitação ou de rejeição(você pode pensar em uma exceção, por exemplo). Lembre-se que em uma máquina de turing, um dos possíveis estados é não responder nada e assim ficar em loop, quando uma linguagem é decidível, esse cenário **nunca** ocorre.

O livro busca representar os problemas decidiveis, por meio de linguagens, isso porque, como desde o ínicio da disciplina estamos fazendo autômatos para o reconhecimento das mesmas, então será fácil pra você se a mesma linha de raciocínio for seguida, mas cada linguagem citada abaixo equivale a um problema e o autômato(a.k.a. programa), a solução.

Para provar que uma linguagem é decidível, só precisamos discutir, qual seria o procedimento necessário para resolver o problema, geralmente, usando pseudo-código, esse tópico diferente dos outros não exigirá a criação dos autômatos.

### Polinômio com uma raiz inteira

**`L = { p | p é um polinômio sobre x com raiz inteira }`**

O problema do polinômio com uma raiz inteira num primeiro momento, pode parecer que não é decidivel, já que se tivermos um polinômio com múltiplas raízes, precisamos testar usando a abordagem de **força bruta**, e assim o computador pode ficar executando indefinidamente, como consequência o problema não consegue ser decidível. No entanto, no caso de um polinômio com uma única raiz inteira conseguimos fazer ele ser decível, porque conseguimos limitar a quantidade de casos que precisamos testar.

O [teorema das raizes racionais](https://pt.wikipedia.org/wiki/Teorema_das_ra%C3%ADzes_racionais) afirma que se o polinômio possui uma raiz ela está entre dois valores, e assim a procura tem fim. Dessa forma, conseguimos afirmar que o problema é decidível, uma vez que também conseguiremos responder quando o polinômio não tem uma raiz, diferentemente do problema inicial.

Um questionamento que pode surgir é:
> "Se eu tiver um polinômio com múltiplas variavéis e conseguir manipular a equação de modo a tornar ele em função de uma única, o problema será decidivel?"

A resposta é **sim**. Entende por quê? Conseguiriamos usar o programa anterior pra resolver o novo.

### Grafo não-direcionado conexo

**`L = { <G> | G é um grafo não-direcionado convexo }`**

Um gráfico é dito conexo, se todo nó consegue ser atingido por qualquer outro. Isto é. existe um caminho pra chegar a um nó, a partir de qualquer nó.

Para resolver usamos um sistema de **marcação**. Iniciamos o programa ou autômato, recebendo o grafo, marcando o nó inicial, a cada novo estado percorrido a partir do que foi marcado, marcamos ele também, se ao final da execução, todos os nós estiverem marcados, isso indica que conseguimos obedecer a propriedade do grafo convexo e portanto aceitamos, se houve pelo menos um nó que não foi marcado, rejeitamos.

### Pertinência a uma linguagem

**`A(afd) = { <B, w> | B é um afd que aceita w }`**

O teste de pertinência, verifica se dado um autômato finito, ele consegue aceitar alguma palavra. Um autômato finito determínistico, como o próprio nome sugere, possui um conjunto de passos finitos, então é de se imaginar que o problema seja decidível. Foi visto que as **maquinas de turing**(mt) podem ser usadas para simular algum comportamento, essa capacidade é muito útil aqui, pois o que fazemos é simular a execução do autômato com a entrada w, na mt, de modo a verificar se é possível chegar ao estado final de aceitação.

Para tal. a máquina de turing possui 3 fitas, em que uma guarda a lista de estados, outra a função de transição, e a ultima que é usada para salvar a entrada e  executar a simulação.

Iniciamos no estado inicial, observamos a fita da função de transição para definir o próximo estado a partir do símbolo corrente da entrada, e assim vamos para ele, se no final de tudo, o estado em que estivermos for de aceitação, aceitaremos, caso contrário, rejeitamos.

### Vacuidade

**`E(afd) = { <A> | A é um afd que L(A) = vazia }`**

O teste da vacuidade tem como objetivo, verificar se um dado autômato não aceita nenhuma palavra. Isso também pode ser interpretado como, dado um estado inicial não existe um caminho para um estado final de aceitação. Se imaginarmos o problema dessa segunda maneira, conseguimos usar uma abordagem similar ao do grafo convexo.

Ao invés de nós, temos estados. Iniciamos marcando o estado inicial, continuamos para os estados que são alcançados pelo primeiro, se ao final da execução o estado final de aceitação não foi marcado, não conseguimos chegar até ele, logo aceitamos, senão, rejeitamos.

### Reconhecimento da mesma linguagem

**`EQ(afd) = { <A, B> | A e B são AFDS e L(A) = L(B) }`**

Esse problema é um dos mais interessantes, pela criatividade necessária para resolver ele. O problema se propõe a testar se duas linguagens aceitam as mesmas palavras, você pode achar que precisaríamos testar todas as palavras desses autômatos para só então confirmar se essas linguagens são iguais, o que seria um problema caso a linguagem fosse infinita, mas isso não é necessário.

O que fazemos é utilizar propriedades de conjuntos, pense no seguinte, se os dois autômatos são iguais, se estivéssemos interessados em saber palavras que pertencem ao primeiro autômato, mas não ao segundo e vice-versa, esse conjunto de palavras deve ser vazio, certo?
Então, usamos isso ao nosso favor. Isso pode ser transcrito como:
`L(C) = [L(A) inter ~L(B)] U [~L(A) inter L(B)] = vazio`

Do primeiro capítulo, vimos que os autômatos são fechados para todas as operações, então tendo em mão o autômato da linguagem C, basta executarmos o autômato do teste da vacuidade, se o mesmo aceita, aceitaremos e se o mesmo rejeita, rejeitaremos. A linguagem consegue ser decídivel, porque apenas manipulamos os estados do autômato, não simulamos uma execução com infinitas palavras, devido a isso conseguimos garantir a resposta.


