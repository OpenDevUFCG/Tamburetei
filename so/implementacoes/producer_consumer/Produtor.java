import java.util.List;
import java.util.Random;

/**
 * Classe que representa o produtor, que sempre está adicionando novos objetos
 * no buffer. Nesse exemplo, o buffer será representado por uma lista
 * compartilhada entre um produtor e um consumidor.
 * 
 * @author Lucas de Medeiros
 */
public class Produtor implements Runnable {

    private List<Integer> listaCompartilhada;
    final private int TAMANHO_MAXIMO = 5;

    /**
     * Construtor do produtor.
     * 
     * @param listaCompartilhada lista que será compartilhada com um consumidor.
     */
    public Produtor(List<Integer> listaCompartilhada) {
        this.listaCompartilhada = listaCompartilhada;
    }

    @Override
    public void run() {
        Random random = new Random();

        while (true) {
            try {
                Integer value = random.nextInt(10);
                this.produce(value);
                System.out.println("Produtor produziu: " + value);
            } catch (InterruptedException ie) {
            }
        }
    }

    /**
     * Método principal do produtor, o 'produce'. Quando o buffer estiver cheio, o
     * produtor deve esperar até que um consumidor consuma algo do mesmo, para que
     * possa voltar a adicionar itens.
     * 
     * @param elemento elemento a ser adicionado na lista
     * @throws InterruptedException lança a exeção se a thread atual não for a
     *                              propietária do monitor deste objeto.
     */
    public void produce(int elemento) throws InterruptedException {

        synchronized (listaCompartilhada) {
            while (listaCompartilhada.size() == TAMANHO_MAXIMO) {
                System.out.println("A lista compartilhada está cheia... " + "Esperando um consumidor consumir algo.");
                listaCompartilhada.wait();
            }
        }

        synchronized (listaCompartilhada) {
            listaCompartilhada.add(elemento);
            Thread.sleep(1000);
            listaCompartilhada.notify();
        }
    }
}