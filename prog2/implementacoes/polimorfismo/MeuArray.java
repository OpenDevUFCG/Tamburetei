import java.util.Arrays;

/**
 * Classe responsável pela representação de um array genérico.
 * 
 * @author Lucas de Medeiros
 */
public class MeuArray<T> {
    private T[] array;

    /**
     * Construtor apenas com o tamanho do novo array genérico que será criado.
     * 
     * @param tamanho tamanho do array.
     */
    @SuppressWarnings("unchecked")
    public MeuArray(int tamanho) {
        this.array = (T[]) new Object[tamanho];
    }

    /**
     * Construtor com um array já existente que será passado para o array interno.
     * 
     * @param array array passado.
     */
    public MeuArray(T[] array) {
        this.array = array;
    }

    /**
     * Imprime o array.
     */
    public void print() {
        System.out.println(Arrays.toString(this.array));
    }

    /**
     * Adiciona um novo elemento em determinada posição do array.
     * 
     * @param elemento elemento a ser adicionado.
     * @param pos posição em que deve ser inserido
     * @throws IllegalArgumentException caso a posição a ser inserida seja inválida.
     */
    public void add(T elemento, int pos) {
        if (pos >= this.array.length || pos < 0)
            throw new IllegalArgumentException("Posição inválida!");
        this.array[pos] = elemento;
    }

    /**
     * Remove o elemento de determinada posição do array.
     * 
     * @param pos posição do elemento a ser removido.
     */
    public void remove(int pos) {
        this.array[pos] = null;
    }

    /**
     * Remove a primeira ocorrência de um elemento do array.
     * 
     * @param elemento elemento a ser removido.
     */
    public void remove(T elemento) {
        int contador = 0;
        for (T el : this.array) {
            if (el.equals(elemento)) {
                this.array[contador] = null;
                break;
            } else {
                contador++;
            }
        }
    }
}
