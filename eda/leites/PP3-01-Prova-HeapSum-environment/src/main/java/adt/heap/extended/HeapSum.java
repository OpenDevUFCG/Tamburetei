package adt.heap.extended;

/**
 * Representa uma min-heap que possui metodos de soma de seus elementos segundo criterios
 * Restricao geral: sua implementacao pode usar APENAS os metodos poll(), peek(), isEmpty()
 * OBSERVEM AS RESTRICOES ESPECIFICAS DE CADA METODO NOS COMENTARIOS.  ELAS CONTEM MAIS RESTRICOES
 * E/OU POSSIBILIDADES.
 * 
 * @author adalbertocajueiro
 *
 */
public interface HeapSum {
	/**
	 * Retorna a soma dos elementos compreendidos entre a k1-esima estatistica de 
	 * ordem (inclusive) e k2-esima estatistica de ordem (inclusive) na heap.
	 * Exemplo: suponha uma min heap onde foram previamente inseridos os 
	 * elementos [1,3,5,7,9,11,13,15,17]
	 * Seja k1 = 3 (o terceiro menor elemento eh 5)
	 * Seja k2 = 8 (o oitavo menor elemento eh 15)
	 * A soma seria entao: 5+7+9+11+13+15 = 60
	 * 
	 * Restricoes:
	 * - Voce pode considerar que as estatisticas de ordem variam de 1 até N (quantidade 
	 *   de elementos inseridos da heap)
	 * - Voce NAO pode usar memoria extra (estruturas), exceto variaveis simples.
	 * 
	 * @param k1  o k1-esimo menor elemento
	 * @param k2  o k2-esimo menor elemento
	 * @return
	 */
	public Integer sumRangeOrderStatistics(Integer k1, Integer k2);
	
	/**
	 * Retorna a soma dos elementos da heap compreendidos entre o valor v1 (caso v1 esteja na heap ele sera
	 * incluido) e o valor v2 (caso v2 esteja na heap ele sera incluido).
	 * Exemplo: suponha uma min heap onde foram previamente inseridos os 
	 * elementos [1,3,5,7,9,11,13,15,17]
	 * Seja v1 = 6 (nao esta na heap)
	 * Seja v2 = 15 (esta na heap)
	 * A soma seria entao: 7+9+11+13+15 = 55
	 * 
	 * Restricoes:
	 * - Voce NAO pode usar memoria extra (estruturas), exceto variaveis simples.
	 * - Voce pode assumir que v1 <= v2
	 * 
	 * @param v1  um valor que pode estar na heap
	 * @param v2  um valor que pode estar na heap
	 * @return
	 */
	public Integer sumRangeBetween(Integer v1, Integer v2);
	
	/**
	 * Retorna a soma dos elementos da heap que estao em determinado nivel 
	 * da heap (a raiz esta sempre no nivel 0).
	 * Exemplo: suponha uma min heap onde foram previamente inseridos os 
	 * elementos [1,3,5,7,9,11,13,15,17]
	 *            1             (level 0)
	 *        3       5         (level 1)
	 *      7   9  11   13      (level 2)
	 *   15  17                 (level 3)
	 * 
	 * Seja level = 0 (a soma retornada eh 1)
	 * Seja level = 1 (a soma retornda eh 8)
	 * Seja level = 3 (a soma retornda eh 32)
	 * 
	 * Restricoes:
	 * - Voce PODE usar o metodo toArray() da heap
	 * - Caso a heap nao possua o nivel informado o resultado deve ser 0 (zero)
	 * 
	 * @param level  o nivel da heap a ser somado
	 * @return
	 */
	public Integer sumRangeAtLevel(int level);
}
