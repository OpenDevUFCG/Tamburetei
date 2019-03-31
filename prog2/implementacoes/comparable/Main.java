import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Classe principal para exemplificar comparable em Java.
 * 
 * @author Lucas de Medeiros
 */

public class Main {

    public static void main(String[] args) {
        Filme filme1 = new Filme("Homem-Aranha", 2002);
        Filme filme2 = new Filme("João e Maria: caçadores de bruxas", 2013);
        Filme filme3 = new Filme("A volta dos que não foram", 2002);

        List<Filme> filmes = new ArrayList<>();
        filmes.add(filme1);
        filmes.add(filme2);
        filmes.add(filme3);

        // Como cada filme implementa comparable, vai ordenar pelo ano de lançamento.
        Collections.sort(filmes);

        // Imprimindo o array ordenado.
        System.out.println(Arrays.toString(filmes.toArray()));
    }
}
