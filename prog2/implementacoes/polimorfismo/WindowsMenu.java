import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Classe responsável pela representação de um menu Windows.
 * 
 * @author Lucas de Medeiros
 */
public class WindowsMenu implements Menu {

    List<String> opcoes;

    public WindowsMenu() {
        this.opcoes = new ArrayList<>();
        this.opcoes.add("Sou um menu Windows");
    }
    
    /**
     * Sobrescrita do método 'exibir' sem parâmetros no contexto de WindowsMenu.
     */
    @Override
    public void exibir() {
        // Implementação do menu Windows.
        System.out.println(Arrays.toString(this.opcoes.toArray()));
    }

    /**
     * Método de LinuxMenu para exibir o menu com as opções dadas.
     * 
     * @param opcoes Opções que serão passadas ao menu.
     */
    @Override
    public void exibir(List<String> opcoes) {
        this.opcoes.addAll(opcoes);
        exibir();
    }
}