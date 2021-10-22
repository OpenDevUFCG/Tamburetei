# CNF, Tableux e SAT Solvers

CNF, Tableux e SAT Solvers são algoritmos que resolvem os problemas da validade ou satisfatilibilidade de fórmulas na Lógica Proposicional. 

## Validade e Satisfatibilidade

- Uma fórmula é **válida** se, para **todas** as interpretações ou modelos, ela será **verdadeira**. Outra forma de dizer isso é que o valor de todas as linhas da tabela verdade é verdadeiro.
- Uma fórmula é **satisfazível** se existe pelo **menos uma** interpretação ou modelo **verdadeira**. Ou seja, ela tem pelo menos uma linha da tabela verdadeira.

Essas definições estão conectadas e pode-se achar a validade de uma fórmula a partir da satisfatibilidade, e vice-versa.
- Uma fórmula é **válida** se a sua negação **não** é **satisfazível**.
- Uma fórmula é **satisfazível** se sua negação **não** é **válida**.
