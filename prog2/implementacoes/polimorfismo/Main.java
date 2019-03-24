import java.util.ArrayList;
import java.util.List;

/**
 * Classe principal para exemplificar polimorfismo em Java.
 * 
 * @author Lucas de Medeiros
 */
public class Main {

    /**
     * Chama o método exibir de um menu passado como parâmetro,
     * caracterizando um polimorfismo de subtipo.
     * 
     * @param menu menu que deve ser exibido.
     */
    public static void exibirMenu (Menu menu) {
        menu.exibir(); // Exemplo de polimorfismo de subtipo
    }

    /**
     * Chama o método exibir de um menu passado como parâmetro,
     * mas passando como parâmetros as opções que devem ser
     * exibidas, caracterizando um polimorfismo de sobrecarga.
     * 
     * @param menu menu que deve ser exibido.
     * @param opcoes opções que devem ser passadas ao 
     */
    public static void exibirMenu (Menu menu, List<String> opcoes) {
        menu.exibir(opcoes); // Exemplo de polimorfismo de sobrecarga.
    }

    /**
     * Exemplo de conversão de um número de ponto flutuante em
     * inteiro, caracterizando um exemplo de polimorfismo de
     * coersão.
     */
    public static void conversao() {
        double numero1 = 17.2;
        int numero2 = (int) numero1;

        System.out.println(numero2); // 17
    }

    /**
     * Método genérico para receber um array de qualquer tipo,
     * adicioná-lo à classe genérica MeuArray e imprimi-lo, 
     * caracterizando um exemplo de polimorfismo paramétrico.
     * 
     * @param array array que será impresso.
     */
    public static <T> void imprimeArrayGenerico(T[] array) {
        MeuArray<T> meuArray = new MeuArray<>(array);
        meuArray.print();
    }

    public static void main(String[] args) {
        // Exemplos de polimorfismo de subtipo.
        Menu windowsMenu = new WindowsMenu();
        Menu linuxMenu = new LinuxMenu();
        
        exibirMenu(windowsMenu);
        exibirMenu(linuxMenu);

        // Exemplos de polimorfismo de sobrecarga.
        List<String> opcoes = new ArrayList<>();
        opcoes.add("Iniciar");
        opcoes.add("Abrir navegador");
        opcoes.add("Sair");

        exibirMenu(windowsMenu, opcoes);
        exibirMenu(linuxMenu, opcoes);

        // Exemplo de polimorfismo de coerção.
        conversao();

        // Exemplo de polimorfismo paramétrico (generics)
        Integer[] array1 = {5, 8, 3, 4};
        Double[] array2 = {9.2, 7.1, 8.6};
        String[] array3 = {"Joaquim", "Luciano", "Dedé"};

        imprimeArrayGenerico(array1);
        imprimeArrayGenerico(array2);
        imprimeArrayGenerico(array3);
    }
}