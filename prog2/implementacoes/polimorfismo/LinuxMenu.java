import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Classe responsável pela representação de um menu Linux.
 * 
 * @author Lucas de Medeiros
 */
public class LinuxMenu implements Menu {

    private List<String> opcoes;

    public LinuxMenu() {
        this.opcoes = new ArrayList<>();
        this.opcoes.add("Sou um menu Linux");
    }

    /**
     * Sobrescrita do método 'exibir' sem parâmetros no contexto de LinuxMenu.
     */
    @Override
    public void exibir() {
        // Implementação do menu Linux...
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