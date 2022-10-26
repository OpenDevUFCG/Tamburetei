## Inteligência Artificial - Resolvendo problemas por busca

**Agentes resolvedores de problema**: conseguem planejar uma sequẽncia de ações que devem ser executadas para atingir um estado objetivo.

### 1. Problem-Solving Agents
Podemos dividir um problema em 4 fases:
- Formulação do Objetivo
	- Qual deve ser o objetivo a ser cumprido pelo agente? Qual o estado do ambiente em que esse objetivo está concluído?
- Formulação do Problema
	- O agente deriva descrições dos estados e ações necessárias para alcançar o objetivo.
- Busca
	- Antes de tomar qualquer ação, o agente simula sequẽncias de ações no modelo , procurando uma sequência que satisfaça o objetivo. Essa sequência que satisfaz o objetivo é chamada de **solução**.
- Execução
	- O agente executa as ações que estão na solução, uma por vez.

#### 1.1 Search problems and solutions
Um problema de busca é definidido por:
- Um conjunto de possíveis estados que o ambiente pode estar.
- O estado iniical no qual o agente inicia.
- Um conjunto de um ou mais estados objetivos (*goal status*)
- As ações disponíveis ao agente. Dado um estado *s*, *ACTIONS(s)* retorna um conjunto finito de ações que podem ser tomadas em *s*
- UIm modelo de transição que descreve o que cada ação faz. *RESULT(s,a)* retorna o estado obtido ao aplicar a ação *a* no estado *s*.
- Função custo da ação, denotado por *ACTION-COST(s,a,s')*, que dá o custo numérico de aplicar a ação *a* no estado *s* para alcançar o estado *s'*. Esse custo depende da Medida de Perfomance ([[Medidas de Perfomance devem dizer o que deseja ser alcançado no ambiente]])
---
Uma sequẽncia de ações forma um caminho; 
A solução é um caminho do estado inicial até o estado objetivo;
Uma **solução ótima** é uma solução com o menor custo entre todas as soluções.
#### 1.2 Formulating Problems
A formulação de um problema é sempre um **modelo** - uma abstração matemática - e não a vida real (mapa vs território). Por causa disso, temos que remover detalhes que não influenciam no problema. Essa remoção é chamada de **abstração**.

### 3. Search Algoritms
Algoritmos de busca recebem um problema de busca e retornam a solução do problema ou uma falha, caso a solução não exista.
Geralmente esses algoritmos navegam por uma árvore sobre o espaço de estados do problema, onde cada nó representa um estado e as arestas representam as ações.
A árvore de busca descreve caminhos entre os estados. O espaço de estados é um conjunto potencialmente infinito.

-> Para cada nó alcançado, podemos gerar os nós descedentes a partir das ações disponíveis no nó atual. Ao nó que foi gerado, dizemos que ele foi alcançado (mesmo que não tenha sido expandido).
-> A fronteira de uma árvore de busca é a divisão entre o nó alcançado e seus nós descendentes gerados.
-> O problema essencial é: qual nó gerado devo expandir que me dará a solução com o menor custo?

#### 3.1 Best-first search
Para escolher o nó na fronteira que deve ser expandido, uma estratégia comum (best-first search) é escolher um nó, **n**, com um valor mínimo de uma **evaluation function, f(n)**. Para cada iteração escolhemos um nó na fronteira com um valor *f(n)* mínimo, retorna o estado se é um estado objetivo ou então expande para gerar nós filhos.
Ao escolher diferentes funções *f(n)*, obtemos algoritmos específicos diferentes.

### 3.3 Redundant Path
É importante lembrar de tratar casos que possam conter ciclos ou caminhos redundantes. Isso pode ser feito mantendo os estados visitados em memória (quando couberem) ou de outras maneiras.
- Algoritmos que checam ciclos = **graph search**
- Algoritmos que não checam ciclos = **tree search**

#### 3.4 Measuring problem-solving perfomance
Critérios de avaliação de um algoritmo
- **Completude**
	- O algoritmo garante que uma solução será encontrada, caso exista?
- Otimização de custo
	- O algoritmo encontra a solução ótima?
- Complexidade de tempo
	- Quanto tempo leva para encontrar a solução? Qual a nálise assintótica?
- Complexidade de espaço
	- Quanto de memória é necessário?

Fatores que influenciam a complexidade de tempo:
- d -> depth. Altura do nó.
- b -> branching factor. Média de quantos nós filhos cada nó terá.