## Decidibilidade

Esse tópico concentra-se em demonstrar que problemas são soluvéis ou não, isto é, quais problemas um computador consegue resolver e quais não.  

Você pode pensar que não é útil saber quais problemas o computador não consegue resolver, mas você verá que isso o ajudará a concentrar seus esforços na simplificação e alteração de problemas que você sabe que não são resolvíveis para todos os casos. Além disso, isso o ajuda a compreender melhor a computação, uma vez que você entende seus limites.

## Linguagens Decidiveis

Uma linguagem é dita **decidível**, se existe uma máquina de turing que a decide. Isto significa que existe um programa que consegue resolver o problema, e para cada entrada do mesmo, consegue retornar um resultado, seja ele de aceitação ou de rejeição(você pode pensar em uma exceção, por exemplo). Lembre-se que em uma máquina de turing, um dos possíveis estados é não responder nada e assim ficar em loop, quando uma linguagem é decidível, esse cenário **nunca** ocorre.

O livro busca representar os problemas decidiveis, por meio de linguagens, isso porque, como desde o ínicio da disciplina estamos fazendo autômatos para o reconhecimento das mesmas, então será fácil pra você se a mesma linha de raciocínio for seguida, mas cada linguagem citada abaixo equivale a um problema e o autômato(a.k.a. programa), a solução.

### Polinômio com uma raiz inteira

O problema do polinômio com uma raiz inteira num primeiro momento, pode parecer que não é decidivel, já que se tivermos um polinômio com múltiplas raízes, precisamos testar usando a abordagem de **força bruta**, e assim o computador pode ficar executando indefinidamente, como consequência o problema não consegue ser decidível. No entanto, no caso de um polinômio com uma única raiz inteira conseguimos fazer ele ser decível, porque conseguimos limitar a quantidade de casos que precisamos testar.

O [teorema das raizes racionais](https://pt.wikipedia.org/wiki/Teorema_das_ra%C3%ADzes_racionais) afirma que se o polinômio possui uma raiz ela está entre dois valores, e assim a procura tem fim. Dessa forma, conseguimos afirmar que o problema é decidível, uma vez que também conseguiremos responder quando o polinômio não tem uma raiz, diferentemente do problema inicial.

### Grafo convexo

### Pertinência a uma linguagem

### Vacuidade

### Reconhecimento da mesma linguagem


## Linguagens Reconheciveis

- pequena discussao
- exemplos
- Problema da parada

## Operações e Decidibilidade
- linguagens reconheciveis


## Redutibilidade