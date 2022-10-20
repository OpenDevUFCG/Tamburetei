# Gramáticas Livres do Contexto

# Introdução

## Exemplo informal

### A linguagem dos palíndromos

- A linguagem dos palíndromos (*𝐿𝑝* )
    - Um palíndromo é uma palavra que se lê da mesma forma da frente pra trás e de trás pra frente
    - Exemplos: 𝑎𝑎𝑎𝑎𝑎𝑎, 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏, 0110, 𝜖, 𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟, etc.
- *𝐿𝑝* não é regular
- Considere Σ = 0,1 , existe uma definição recursiva básica para as palavras em *𝐿𝑝*
    - Base: 𝜖, 0 e 1 são palíndromos
    - Indução: se 𝑤 ∈ 𝐿𝐿 𝑝𝑝 , então 0𝑤0 e 1𝑤1 ∈ *𝐿𝑝*
    - **Nenhuma** palavra será palíndromo se não seguir essa regra de indução básica
- Uma **Gramática livre do contexto** (GLC) é uma notação formal para expressar essa definição recursiva das linguagens

## O que é uma gramática?

- Uma gramática consiste de uma ou mais **variáveis** que representam classes de palavras (i.e. linguagens)
- Existem **regras** que ditam como as palavras de cada linguagem são construídas
- O processo de construção se baseia em
    - **Símbolos** de um alfabeto (nenhuma surpresa)
    - Palavras que já sabemos que pertencem à linguagem
    - Ou ambos

## Gramática para *Lp*

- Para 𝐿𝑝 vamos precisar de uma variável 𝑆 que representa o conjunto dos palíndromos
- As regras da gramática:
    1. 𝑆 → 𝜖
    2. 𝑆 → 0
    3. 𝑆 → 1
    4. 𝑆 → 0𝑆0
    5. 𝑆 → 1𝑆1
- As três primeiras regras são a base da indução:
    - Nos dizem que a a classe dos palíndromos incluem 𝜖𝜖, 0 e 1
    - O lado direito não contém variáveis, por isso são a base da definição
- As duas últimas são a parte indutiva da definição
    - Por exemplo, a quarta regra diz que para qualquer 𝑤𝑤 ∈ 𝐿𝐿 𝑝𝑝 , 0𝑤𝑤𝑤 ∈ 𝐿𝐿 𝑝𝑝

## Formalmente:

- Uma GLC é uma tupla 𝐺 = <𝑉, Σ, 𝑅, 𝑆> em que
    - 𝑉 é um conjunto finito de **variáveis** (também chamadas de **não terminais**)
        - Cada variável representa um conjunto de palavras da linguagem
    - Σ é um conjunto finito de **terminais**, i.e. os símbolos das palavras que serão construídas (𝑉 ∩ Σ = ∅)
        - Nenhuma variável é um terminal e nenhum terminal é uma variável
    - 𝑅 é o conjunto das **regras de produção** que representam a **definição recursiva** da linguagem
    - 𝑆 é o símbolo inicial que representa toda a **linguagem** sendo definida
        - Outra variáveis podem ser usadas e elas definem subconjuntos da lingua
    

## Regras de Produção:

- Cada regra de produção consiste de
    1. Uma variável (também chamada de cabeça da produção)
    2. Do símbolo de produção →
    3. Uma cadeia de zero ou mais terminais e variáveis (corpo da produção)
        1. Essa cadeia representa uma forma de gerar palavras a partir da cabeça
        2. Ao fazer isso, terminais não são modificados e cada variável do corpo vai ser substituída de acordo com as regras definidas
    4. Formalmente, 𝑅 é do tipo **𝛼 → 𝛽** em que 𝛼 ∈ 𝑉 e 𝛽 ∈ (𝑉 ∪ Σ)*

## GLC para palíndromos

- 𝐺𝐺 𝑝𝑝 = ⟨ 𝑆𝑆 , 0,1 , 𝑅𝑅, 𝑆𝑆⟩ em que 𝑅𝑅 é definida por
    - 𝑆 → 𝜖𝜖
    - 𝑆 → 0
    - 𝑆 → 1
    - 𝑆 → 0𝑆0
    - 𝑆 → 1𝑆1
- Podemos ainda definir da seguinte forma
    - 𝑆 → 𝜖 | 0 | 1 | 0𝑆0 | 1𝑆1

# Derivações usando a gramática

- Aplicamos as regras de produção para saber que determinadas palavras fazem parte da linguagem da gramática
- Duas possíveis abordagens
1. Inferência Recursiva
    - Usamos as produções do corpo até a cabeça
2. Derivações
    - Usamos as produções da cabeça até o corpo

### Derivações

- Novo símbolo relacional: ⇒
- Seja G = <V, Σ, R, S> uma GLC em que:
    - A ∈ V
    - 𝛼, 𝛽 ⊂ (𝑉 ∪ Σ)*
    - 𝐴 → 𝛾 ∈ 𝑅
    
    Então, escrevemos:
    
    - 𝛼A𝛽  ⇒  𝛼𝛾𝛽
    
    E dizemos que 𝛼A𝛽  deriva (gera)  𝛼𝛾𝛽
    

### Zero ou mais passos de Derivação

- Definimos ⇒* para denotar zero ou mais passos
    - Base: Seja 𝛼 ∈ (𝑉 ∪ Σ)*, então 𝛼 ⇒* 𝛼
    - Indução: se  𝛼 ⇒* 𝛽 e 𝛽 ⇒* 𝛾, então 𝛼 ⇒* 𝛾

# A linguagem de uma gramática

- Seja 𝐺𝐺 = ⟨𝑉𝑉, Σ, 𝑅𝑅, 𝑆𝑆⟩ uma GLC, então a linguagem de 𝐺𝐺 é
    - 𝐿(𝐺) = {𝑤 ∈ Σ* | 𝑆 ⇒* 𝑤}
    - o conjunto de palavras sobre Σ derivadas a partir do símbolo inicial
- Se 𝐺 é uma GLC, dizemos que 𝐿(𝐺) é uma Linguagem Livre do Contexto