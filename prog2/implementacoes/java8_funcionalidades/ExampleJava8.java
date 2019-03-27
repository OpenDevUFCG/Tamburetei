import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Classe principal para exemplificar as novas funcionalidades
 * do Java 8.
 * 
 * @author Lucas de Medeiros
 */

public class ExampleJava8 {

    public static void main(String[] args) {
        
        // Exemplo 1: Funções lambda

        List<Integer> minhaLista = new ArrayList<>();
        minhaLista.add(7);
        minhaLista.add(3);
        minhaLista.add(9);
        minhaLista.add(1);
        minhaLista.add(2);
        minhaLista.add(10);

        // Usando funções lambda para criar um Comparator para a lista criada
        Comparator<Integer> comparador = 
            (i1, i2) -> Integer.compare(i1, i2);
        
        minhaLista.sort(comparador);

        // Usando função lambda para iterar sobre a lista e imprimir valores ordenados.
        System.out.println("Imprimindo os valores ordenados:");
        minhaLista.forEach(elemento -> System.out.println(elemento));

        // Exemplo 2: stream()

        // Usando filter para fazer filtragem de elementos menores que 7 na lista
        System.out.println("Imprimindo os valores menores que 7 existentes na lista:");
        minhaLista.stream()
                    .filter(valor -> (valor < 7))
                    .forEach(System.out::println);
        
        List<String> frutas = new ArrayList<>();
        frutas.add("Banana");
        frutas.add("Maçã");
        frutas.add("Abacaxi");
        frutas.add("Berinjela");

        // Utilizando map para mapear os valores da nova lista de string pelo tamanho.
        System.out.println("Mapeando as strings pelo seu tamanho:");
        frutas.stream()
              .map(String::length)
              .forEach(System.out::println);;
        
        // Sinta-se livre para contribuir com mais exemplos...
    }
}
