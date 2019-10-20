/**
 * Dado dois arrays ordenados em ordem crescente, encontrar a k-esima
 * estatistica de ordem da uniao ordenada deles.
 * 
 * Restricoes: - Os arrays nao ira possuir elementos em comum ou duplicados. - K
 * eh um valor entre 1 e array1.length + array2.length (Soma do tamanho dos dois
 * arrays). - Caso nao houver a k-esima estatistica de ordem, o metodo deve
 * retorna null. - Nao eh permitido o uso de memoria extra. - Seu algoritmo deve
 * ter complexidade O(n), sendo n a soma do tamanho dos dois arrays. - Nao eh
 * permitido o uso de metodos prontos de manipulacao de array, exceto length.
 *
 */
public class OrderStatisticsSortedUnion<T extends Comparable<T>> {

    public T statisticsOrder(T[] array1, T[] array2, int k) {
        T order = null;
        if ((array1.length + array2.length) > k) {
            int i = 0;
            int j = 0;

            while (i < array1.length && j < array2.length && (i + j) < k) {
                if (array1[i].compareTo(array2[j]) < 0) {
                    order = array1[i];
                    i++;
                } else if (array1[i].compareTo(array2[j]) > 0) {
                    order = array2[j];
                    j++;
                }
            }

            while (i < array1.length && (i + j) < k) {
                if (array1[i].compareTo(array2[j - 1]) > 0) {
                    order = array1[i];
                }
                i++;
            }

            while (j < array2.length && (i + j) < k) {
                if (array2[j].compareTo(array1[i - 1]) > 0) {
                    order = array2[j];
                }
                j++;
            }
        }
        return order;
    }
}
