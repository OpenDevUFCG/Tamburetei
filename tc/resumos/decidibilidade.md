## Decidibilidade

Esse tópico concentra-se em demonstrar que problemas são solucionáveis ou não, isto é, quais problemas um computador consegue resolver e quais não.  

Você pode pensar que não é útil saber quais problemas o computador não consegue resolver, mas você verá que isso o ajudará a concentrar seus esforços na simplificação e alteração de problemas que você sabe que não são resolvíveis para todos os casos. Além disso, isso o ajuda a compreender melhor a computação, uma vez que você entende seus limites.

## Linguagens Decidiveis

Uma linguagem é dita **decidível**, se existe uma máquina de turing que a decide. Isto significa que existe um programa que consegue resolver o problema, e para cada entrada do mesmo, consegue retornar um resultado, seja ele de aceitação ou de rejeição (você pode pensar em uma exceção, por exemplo). Lembre-se que em uma máquina de turing, um dos possíveis estados é não responder nada e assim ficar em loop, quando uma linguagem é decidível, esse cenário **nunca** ocorre.

O livro busca representar os problemas decidiveis, por meio de linguagens, isso porque, como desde o ínicio da disciplina estamos fazendo autômatos para o reconhecimento das mesmas, então será fácil pra você se a mesma linha de raciocínio for seguida, mas cada linguagem citada abaixo equivale a um problema e o autômato(também conhecido como programa), a solução.

Para provar que uma linguagem é decidível, só precisamos discutir, qual seria o procedimento necessário para resolver o problema, geralmente, usando pseudo-código, esse tópico diferente dos outros não exigirá a criação dos autômatos.

### Polinômio com uma raiz inteira

**`L = { p | p é um polinômio sobre x com raiz inteira }`**

Num primeiro momento, um polinômio com uma única raiz pode parecer não decidível. Já que, quando temos um polinômio com múltiplas raízes, por exemplo, caso em que precisamos testar usando a abordagem de **força bruta**, corre-se o risco do computador ficar executando indefinidamente, o que faz com que o problema não seja decidível. No entanto, no caso de um polinômio com uma única raiz inteira, conseguimos fazer ele ser decídivel, porque podemos limitar a quantidade de casos que precisamos testar.

O [teorema das raizes racionais](https://pt.wikipedia.org/wiki/Teorema_das_ra%C3%ADzes_racionais) afirma que se o polinômio possui uma raiz, ela está entre dois valores, e assim a procura tem fim. Dessa forma, conseguimos afirmar que o problema é decidível, uma vez que também conseguiremos responder quando o polinômio não tem uma raiz, diferentemente do problema inicial.

Um questionamento que pode surgir é:
> "Se eu tiver um polinômio com múltiplas variavéis e conseguir manipular a equação de modo a tornar ele em função de uma única, o problema será decidivel?"

A resposta é **sim**. Entende por quê? Seria possível usar o programa anterior pra resolver o novo.

### Grafo não-direcionado conexo

**`L = { <G> | G é um grafo não-direcionado conexo }`**

Um gráfico é dito conexo, se todo nó consegue ser atingido por qualquer outro. Isto é. existe um caminho pra chegar a um nó, a partir de qualquer nó.

Para resolver, usamos um sistema de **marcação**. Iniciamos o programa ou autômato, recebendo o grafo e marcando o nó inicial. A cada novo estado percorrido a partir do que foi marcado, marcamos ele também. Se ao final da execução, todos os nós estiverem marcados, isso indica que conseguimos obedecer a propriedade do grafo conexo e, portanto, aceitamos. Se houve pelo menos um nó que não foi marcado, rejeitamos.

### Pertinência a uma linguagem

**`A(afd) = { <B, w> | B é um afd que aceita w }`**

O teste de pertinência verifica se um autômato finito consegue aceitar alguma palavra. Um autômato finito determinístico, como o próprio nome sugere, possui um conjunto de passos finitos, então é de se imaginar que o problema seja decidível. Foi visto que as **máquinas de Turing**(mt) podem ser usadas para simular algum comportamento, e essa capacidade é muito útil aqui, pois o que fazemos é simular a execução do autômato com a entrada w, na mt, de modo a verificar se é possível chegar ao estado final de aceitação.

Para tal, a máquina de Turing possui 3 fitas, em que uma guarda a lista de estados, outra, a função de transição, e a última é usada para salvar a entrada e executar a simulação.

Iniciamos no estado inicial e observamos a fita da função de transição para definir o próximo estado a partir do símbolo corrente da entrada, e assim vamos para ele. Se, no final de tudo, o estado em que estivermos for de aceitação, aceitaremos, caso contrário, rejeitaremos.

### Vacuidade

**`E(afd) = { <A> | A é um afd que L(A) = vazia }`**

O teste da vacuidade tem como objetivo verificar se um dado autômato não aceita nenhuma palavra. Isso também pode ser interpretado como: dado um estado inicial, não existe um caminho para um estado final de aceitação. Se imaginarmos o problema dessa segunda maneira, conseguimos usar uma abordagem similar ao do grafo conexo.

Ao invés de nós, temos estados. Iniciamos marcando o estado inicial, continuamos para os estados que são alcançados pelo primeiro, se ao final da execução o estado final de aceitação não foi marcado, não conseguimos chegar até ele, logo aceitamos, senão, rejeitamos.

### Reconhecimento da mesma linguagem

**`EQ(afd) = { <A, B> | A e B são AFDS e L(A) = L(B) }`**

Esse problema é um dos mais interessantes, pela criatividade necessária para resolver ele. O problema se propõe a testar se duas linguagens aceitam as mesmas palavras, você pode achar que precisaríamos testar todas as palavras desses autômatos para só então confirmar se essas linguagens são iguais, o que seria um problema caso a linguagem fosse infinita, mas isso não é necessário.

O que fazemos é utilizar propriedades de conjuntos, pense no seguinte, se os dois autômatos são iguais, se estivéssemos interessados em saber palavras que pertencem ao primeiro autômato, mas não ao segundo e vice-versa, esse conjunto de palavras deve ser vazio, certo?
Então, usamos isso ao nosso favor. Isso pode ser transcrito como:  
`L(C) = [L(A) inter ~L(B)] U [~L(A) inter L(B)] = vazio`

Do primeiro capítulo, vimos que os autômatos são fechados para todas as operações, então tendo em mão o autômato da linguagem C, basta executarmos o autômato do teste da vacuidade, se o mesmo aceita, aceitaremos e se o mesmo rejeita, rejeitaremos. A linguagem consegue ser decídivel, porque apenas manipulamos os estados do autômato, não simulamos uma execução com infinitas palavras, devido a isso conseguimos garantir a resposta.

## Linguagens Reconhecíveis

De forma similar às linguagens decidíveis, uma linguagem é dita reconhecível se existe uma máquina de turing que a reconhece. A diferença sutil entre a definição anterior, é que linguagens reconhecíveis nem sempre retornam uma resposta. Tais linguagens conseguem sempre afirmar quais palavras pertencem a elas, mas não asseguram que retornarão uma resposta no caso contrário.

### Problema da parada

O problema da parada pode te assustar um pouco, mas é um teorema bem importante e que vai ser bastante necessário desse ponto em diante, porque você verá que para concluir que um problema não é decidível, o que fazemos é tentar equiparar o problema da parada que não é decidível a ele.

Um vídeo muito legal para entender esse assunto é [este](https://www.youtube.com/watch?v=wGLQiHXHWNk), além disso, ele foi usado como base para essa explicação. O problema da parada consiste em ter um programa que tenha a capacidade de afirmar se um programa qualquer (inclusive ele mesmo) irá parar ou não, podemos estar interessados nisso, já que a máquina de turing que representa um computador pode executar indefinidamente.

Para provar que isso não é possível usamos um tipo de **prova por contradição**, iniciamos assumindo que é possível indicar se um programa para ou não e chegaremos a uma contradição, nos levando a concluir que nossa afirmação era falsa. Suponha que existe um programa **H**, que atua como um oráculo, que prevê o futuro, no caso desse programa ele recebe outro e consegue prever se o programa da entrada para ou não. Agora suponha que existe outro programa **D**, que é como um disseminador de **fake news**, ao receber um programa ele passa pra **H** e diz exatamente o contrário que **H** disse. Então se **H** disse que o programa para, ele dirá que não para, e vice-versa.

Agora imagine o cenário em que **D** passa ele mesmo como entrada, como ele recebe um programa como entrada, isso é possível. Essa ideia pode parecer estranha, mas é isso que um compilador faz, ele é um programa que recebe outro como entrada. Ao passar **D** como entrada, **H** poderia afirmar que **D** para, mas como **D** sempre afirma o contrário, ele diria que não para. É aqui que chegamos na contradição, se existe um programa **H** que consegue afirmar que o problema para, ele deveria ser coerente com o resultado apontado por **D**, como **D** afirma que para e não para ao mesmo tempo, pelo **príncipio do terceiro excluído**, isso é uma contradição, logo, podemos concluir que H não existe.



### Máquina de Turing e a pertinência a linguagem

**`A(mt) = { <M, w> | M é uma mt e m aceita w }`**

Para esse problema, agimos de modo similar, ao que foi feito com os autômatos, atuamos simulado a execução dessa máquina, se nossa maquina M aceita, aceitamos e se ela rejeita, rejeitamos. O problema é que como temos a saida indefinida, isto é, um loop, o programa ficará executando indefinidamente e como vimos que não conseguimos prever se o programa para ou não do tópico anterior, esse problema também é apenas reconhecível.


### Máquina de Turing e a Vacuidade

**`Vazio(mt) = { <M> | M é uma mt e L(m) = vazio }`**

A ideia por trás da prova é reduzir esse problema a uma variação da **A(mt)** que sabemos que é indecídivel. Se a linguagem é vazia, ele não aceita nenhuma palavra. Então se ele aceita pelo menos uma, deixa de ser vazia e não pertence a nossa linguagem.

Testamos para esse caso base, em que a linguagem só tem uma única palavra, e vemos que não conseguimos responder nem mesmo nele. Criamos uma variação da máquina anterior, adicionando alguns estados iniciais que verificam se a palavra passada é diferente da que nossa linguagem possui, se ela for, rejeitamos, caso contrário, colocamos ela pra executar na máquina anterior. No entanto, mais uma vez, recaímos no problema de se determinar se a máquina para ou não. E como não conseguimos assegurar o nosso estado de negação, concluímos que ela é reconhecível.

## Irreconhecibilidade

Além das linguagens citadas anteriormente, existe um outro tipo de linguagem, que é a linguagem irreconhecível. Esse tipo não consegue garantir nem o estado de aceitação, nem o de rejeição. A partir dos exemplos, isso ficará mais claro.

## Co-reconhecibilidade

Um teorema importante, antes de entender melhor o que é a irreconhecibilidade, é entender o teorema da co-reconhecibilidade, que afirma que se uma linguagem e seu complemento são reconhecíveis, então a primeira será reconhecível. Isto porque, se o complemento de uma linguagem é decidível. Se isso occore, indica que a linguagem já consegue garantir o não, porque quando fazemos o complemento, o que era o antigo não, passará a ser o estado de aceitação, e dessa forma ela só garantirá isso, se antes garantia o de rejeição. E assim, concluímos que ela só pode ser decidível.

Devido a esse fato, se tivermos uma linguagem apenas reconhecível, ao fazermos seu complemento, o resultado é que obtemos uma **linguagem irreconhecível**, já que ela não garante a rejeição e quando fizermos o complemento, esse passará a ser o novo estado de aceitação.

## Operações entre Linguagens

### Linguagem reconhecível ∩ Linguagem reconhecível

Ao fazermos a interseção de uma linguagem reconhecível com outra reconhecível, obtemos outra reconhecível, já que como as duas garantem o sim, a interseção não alterará essa propriedade e a resultante ainda terá esse comportamento.

### Linguagem decídivel U Linguagem decidível

Ao fazermos a união de duas decidíveis, estamos obtendo todo o conjunto de linguagens que garantem o sim e o não e unindo a ele mesmo, logo o resultado é uma linguagem decídivel também.

### Linguagem reconhecível U Linguagem decidível

Ao fazermos a união de uma reconhecível com uma decidível, acabamos por obter uma reconhecível, isto se dá, porque se nos depararmos com o caso em que ambas as linguagens rejeitam a palavra, poderíamos continuar executando indefinidamente no caso da primeira, logo a linguaguem garante apenas a aceitação.

### Linguagem reconhecível ∩ Linguagem decidível

Apesar de uma delas ser decídivel, se nos depararmos com o caso da primeira receber uma palavra que não pertence a lingugagem também executaríamos indefinidamente, como no caso anterior, e portanto, a linguagem resultante é reconhecível.






