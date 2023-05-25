## Inteligência Artificial - Estratégias de Busca Desinformada (heurística)

### 5. Estratégias de Busca Heurística (informadas)
Utiliza "dicas" específicas do dominío sobre a localização dos objetivos.
Função Heurística:
	h(n) = custo estimado do menor caminho do nó n ao nó objetivo.

#### 5.1 Greedy best-first search (busca gulosa)
- Sempre expande o nó com a menor heurística (que parece estar mais próximo da solução)
	- $${f(n) = h(n)}$$
- Completo para espaço de estados finito
- Não é custo ótimo
- Complexidade de tempo e espaço: $${O(|V|)}$$

#### 5.2 A* Search
- $${f(n) = g(n) + h(n)}$$, onde $${g(n)}$$ é o custo do caminho do estado inicial até o estado do nó n.
- Completo
- Se a heurística for **admissível** (otimista; não exagera no resultado além da vida real), a busca possui custo ótimo.

Uma heurística $${h(n)}$$ é **consistente** se, para cada nó $${n}$$ e cada sucessor $${n'}$$ de $${n}$$ gerado por uma ação $${a}$$, temos:
	$${h(n) \le c(n, a, n') + h(n')}$$

Toda heurística consistente é admissível, mas não vice versa.

#### 5.3 Weighted A*
- $${f(n) = g(n) + W*h(n), W > 1}$$
- Não garante a solução ótima, mas pode ser encarada como uma solução sub-ótima (levando menos tempo e espaço para ser concluída).
- 