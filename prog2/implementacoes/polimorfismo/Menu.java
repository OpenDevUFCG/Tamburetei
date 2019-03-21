import java.util.List;

/**
 * Interface responsável pela representação de um menu genérico.
 * 
 * @author Lucas de Medeiros
 */
public interface Menu {

    /**
     * Método que exibe o menu.
     */
    void exibir();

    /**
     * Método genérico para exibir o menu com as opções dadas.
     * 
     * @param opcoes Opções que serão passadas ao menu.
     */
    void exibir(List<String> opcoes);
}