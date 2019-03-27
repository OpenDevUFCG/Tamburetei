import java.util.Comparator;

/**
 * Classe que vai ser a responsável pela implementação do comparador de dois filmes
 * pelos seus respectivos anos de lançamento.
 * 
 * @author Lucas de Medeiros
 */
public class FilmeComparadorPorAno implements Comparator<Filme> {

    /**
     * Reescreve função compare, comparando dois filmes pelo ano.
     * 
     * @param f1 primeiro filme a ser comparado
     * @param f2 segundo filme a ser comparado
     * @return inteiro que representa se um dos filmes é maior, ou se são iguais.
     */
    @Override
    public int compare(Filme f1, Filme f2) {
        return f1.getAno() - f2.getAno();
    }
}
