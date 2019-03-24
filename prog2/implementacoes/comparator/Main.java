import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * Classe principal para exemplificar comparator em Java.
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

        // Criação de um comparator com funções lambda
        Comparator<Filme> comparadorPorAnoLambda = 
            (f1, f2) -> f1.getAno() - f2.getAno();
        
        // Criação de um comparator (método convencional)
        Comparator<Filme> comparatorPorAnoConvencional = new FilmeComparadorPorAno();

        // Você pode usar o comparator por lambda também, mas para o exemplo, vamos usar o convencional.
        filmes.sort(comparatorPorAnoConvencional);

        // Imprimindo o array ordenado pelos respectivos anos de publicação.
        System.out.println(Arrays.toString(filmes.toArray()));
    }
}