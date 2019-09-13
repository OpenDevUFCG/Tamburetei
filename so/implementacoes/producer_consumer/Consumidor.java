import java.util.List;

/**
 * Classe que representa o consumidor, que sempre estará consumindo objetos do
 * buffer. Nesse exemplo, o buffer será representado por uma lista compartilhada
 * entre um produtor e um consumidor.
 * 
 * @author Lucas de Medeiros
 */
public class Consumidor implements Runnable {

    private List<Integer> listaCompartilhada;

    /**
     * Construtor do consumidor.
     * 
     * @param listaCompartilhada lista que será compartilhada com um produtor.
     */
    public Consumidor(List<Integer> listaCompartilhada) {
        this.listaCompartilhada = listaCompartilhada;
    }

    @Override
    public void run() {
        while (true) {
            try {
                Integer value = this.consume();
                System.out.println("Consumidor consumiu: " + value);
            } catch (InterruptedException ie) {
            }
        }

    }

    /**
     * Método principal do consumidor, o 'consume'. Quando o buffer estiver vazio, o
     * consumidor deve esperar até que um produtor produza algo para o mesmo, para
     * que possa voltar a consumir itens.
     * 
     * @param elemento elemento a ser adicionado na lista
     * @throws InterruptedException lança a exeção se a thread atual não for a
     *                              propietária do monitor deste objeto.
     */
    public Integer consume() throws InterruptedException {
        Integer value = 0;

        synchronized (listaCompartilhada) {
            while (listaCompartilhada.isEmpty()) {
                System.out.println("A lista compartilhada está vazia... " + "Esperando um produtor adicionar algo.");
                listaCompartilhada.wait();
            }
        }

        synchronized (listaCompartilhada) {
            Thread.sleep(1000);
            value = listaCompartilhada.remove(0);
            return value;
        }
    }

}