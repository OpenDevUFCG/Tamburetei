# Autômatos de Pilha

Os **autômatos de pilha** são semelhantes aos autômatos finitos, porém, contam com um componente extra que provê memória: a **pilha**. Essa pilha é infinita e seu uso é motivado pela forma simples de armazenamento, não envolvendo endereçamento do conteúdo. Assim, o grande diferencial dos autômatos de pilha é a capacidade de armazenar símbolos nessa pilha à medida que realizam transições.

De maneira análoga aos autômatos finitos, existem autômatos de pilha determinísticos e não-determinísticos, porém, esses dois tipos não possuem as mesmas capacidades e tem objetivos distintos.

A definição formal de um **autômato de pilha (AP)** é uma 6-tupla **<Q, Σ, Γ, δ, q0, F>**, tal que:

- **Q** é o conjunto de estados.
- **Σ** é o alfabeto da entrada.
- **Γ** é o alfabeto da pilha.
- **δ: Q × Σ × Γε → P(Q × Γε)** é a função de transição do autômato.
- **q0** ∈ Q é o estado inicial do autômato.
- **F** ∈ Q é o conjunto de estados finais do autômato.

No **diagrama de estados**, utiliza-se a notação **a, b → c** para as transições, indicando que o autômato lê um símbolo *a* da entrada e substitui o símbolo *b* do topo da pilha por um símbolo *c*. A seguir, algumas notações importantes:

- Se **a = λ** (ou ε), tem-se que a transição é realizada sem consumir símbolos da entrada.
- Se **b = λ** (ou ε), tem-se que o símbolo *c* é empilhado sem remover o topo da pilha.
- Se **c = λ** (ou ε), tem-se que o símbolo do topo da pilha é desempilhado sem ser substituído.
- O símbolo **$** é um marcador do início da pilha, de modo que se **b = $** na última transição, a pilha estará vazia.

## Linguagens Livres de Contexto

Os autômatos de pilha são capazes de reconhecer algumas linguagens não-regulares e equivalem às **gramáticas livres de contexto (GLC)**. Além disso, dada uma **linguagem livre de contexto (LLC)**, obrigatoriamente há um autômato de pilha que a reconheça. Assim, uma forma prática de provar que uma linguagem é livre de contexto é construir o autômato de pilha que à reconheça.

Para criar um autômato de pilha que reconheça uma gramática livre de contexto, se começa adicionando o símbolo **$** e a variável inicial à pilha. A seguir, inicia-se o seguinte *loop*: 

- Se o topo da pilha for uma variável, uma de suas regras é selecionada não-deterministicamente para substituí-la.
- Se o topo da pilha é um terminal e coincide com o símbolo atual da entrada, ele é desempilhado.
- Se o topo da pilha é o **$**, o estado de aceitação foi alcançado.

Nesse contexto, caso mais de um ramo não-determinístico alcance a aceitação, diz-se que há **ambiguidade**. Porém, é importante compreender que existem linguagens que só podem ser geradas por gramáticas ambíguas.

Assim como os autômatos de pilha reconhecem as linguagens livres de contexto, os **autômatos de pilha determinísticos (APD)** reconhecem as **linguagens livres de contexto determinísticas (LLCD)**. Eles podem ser identificados pela existência de uma única transição válida a cada instante do processamento. Ainda, o determinismo garante a não-ambiguidade.

A nível de comparação, as **linguagens sensíveis ao contexto (LSC)** são aquelas em que pode haver mais de um símbolo à esquerda de cada regra, de modo que certas substituição estão habilitadas apenas em certos contextos.

### Lema do Bombeamento para LLCs

Se uma linguagem A é livre de contexto, existe um número **p** e uma cadeia **s** tal que qualquer palavra dessa linguagem que seja maior que p possuirá uma árvore sintática com repetição, ou seja, é possível gerar variações dessa palavra que pertencem à linguagem. Assim, é possível dividir a cadeia em cinco pedaços **s = uvxyz**, tal que:

- Para *i ≥ 0*, **u (v^i) x (y^i) z** ∈ A
- **|vy| > 0**
- **|vxy| ≤ p**

O lema do bombeamento é geralmente utilizado para provar que uma linguagem não é livre de contexto através de suas implicações sobre a ordem e o balanceamento dos símbolos.