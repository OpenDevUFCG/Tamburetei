## Inteligência Artificial - Estratégias de Busca Desinformada

### 4. Estratégias de busca desinformadas
Nesse tipo de busca, o algoritmo não tem ideia do quâo distante está do objetivo.

#### 4.1 Busca por largura
- Apropriado para pequenos problemas onde todas as funções de custo são as mesmas
- Complexidade de tempo e espaço: $${{O(b^d)}}$$
- Completo (sempre acha uma solução)
- Quando todos os custos são iguais, o algoritmo é otimizado no custo. Ele encontra a solução ótima.

#### 4.2 Algoritmo de Dijkstra ou Uniform-Cost Search
- **Best-first search** onde a função de evaluação é o custo do caminho do nó raiz até o nó atual. Sendo assim, sempre expande para o nó associado com o tamanho de menor custo.
- Completo
- Custo ótimo

#### 4.3 Busca em profundidade
- Expande sempre o nó mais "profundo"
- Incompleto
	- Em árvores infinitas pode nunca acabar
- Não é custo ótimo
	- Retorna a primeira solução que achar

Sua principal vantagem é sua complexidade de memória $${{O(b*m)}}$$, já que não é necessário manter uma tabela dos nós alcançados.

#### 4.4 Busca em profundidade limitada e busca iterativa

##### Busca em profundidade limitada
- Versão da busca em profundidade onde é fornecido um valor, $${l}$$, tal que todos os nós na profundidade $${l}$$ são considerados folhas (sem descendentes)
- Complexidade
	- Tempo: $${O(b^l)}$$
	- Espaço: $${O(b*l)}$$
- Incompleto

##### Busca interativa
- Na busca interativa, o problema de escolher um valor limite ${l}$ é resolvido ao tentar todos os valores: 0,1... - até que uma solução seja encontrada ou o algoritmo retorne uma falha.
- Custo ótimo quando a àrvore possui todos os custos iguais
- Complexidade
	- Tempo: $${O(b^d)}$$
	- Espaço: $${O(b*d)}$$
- Método de busca aconselhado quando o espaço de estados é maior do que possa ser guardado na memória e a profundidade da solução não é conhecida.

#### 4.5 Busca bidirecional
Acontecem duas buscas simultâneas:
- Do nó raiz ao nó objetivo
- Do nó objetivo ao nó raiz
Para cada uma dessas buscas, é gerado um caminho. O algoritmo termina quando há intersecção entre os dois caminhos.
- Complexidade: $${O(b^{d/2})}$$ (Tempo e espaço)