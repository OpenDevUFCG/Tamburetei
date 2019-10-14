package problems;

/**
 * Dado um array arbitrario nao necessariamente ordenado de inteiros (Integer) e um parametro x, 
 * closest(x) eh o elemento do array que mais se aproxima de x. 
 * 
 * Exemplo: closest([4,6,8,10],7) = 6 (poderia ser tambem 8)
 * closest([4,6,8,10],8) = 8 
 * 
 * @author Adalberto e Campelo
 *
 */
public interface Closest {
	/**
	 * Retorna o elemento do array que mais se aproxima de x.
	 * 
	 * @param array
	 * @return o elemento do array que mais se aproxima de x.
	 * 
	 * Restricoes:
	 * - voce nao pode usar nenhum metodo pronto de qualquer biblioteca.
	 * - voce pode assumir que o array nao tem elementos repetidos
	 * - todo e qualquer codigo que voce implementar deve estar na sua classe 
	 *   de implementacao.
	 * - caso o array seja vazio, o metodo deve retornar null;
	 * - OBSERVE AS RESTRICOES ESPECIFICAS NA CLASSE DE IMPLEMENTACAO QUE VOCE RECEBEU
	 * 
	 */
	public Integer closest(Integer[] array, Integer x);

}
