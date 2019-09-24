import java.util.ArrayList;
import java.util.List;

/**
 * Classe principal para rodar o Exemplo de producer-consumer em Java. Aqui, são
 * criadas duas Threads, uma para o produtor e o consumidor, e as duas são
 * rodadas de maneira "paralela". A lógica de implementação de cada um estão
 * nas classes Produtor e Consumidor, respectivamente.
 * 
 * Nesse exemplo, o buffer será representado por uma lista
 * compartilhada entre um produtor e um consumidor.
 * 
 * @author Lucas de Medeiros
 */
public class ExemploProdutorConsumidor {
  public static void main(String[] args) {
    List<Integer> listaCompartilhada = new ArrayList<>();

    Thread threadProdutor = new Thread(new Produtor(listaCompartilhada));
    Thread threadConsumidor = new Thread(new Consumidor(listaCompartilhada));

    threadProdutor.start();
    threadConsumidor.start();
  }
}