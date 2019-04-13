/**
 * Classe Principal do sistema.
 * 
 * @author Rick Elton
 */
public class Main {

    public static void main(String[] args) {

        // Poupanca
        Conta c1 = new Poupanca("123");
        c1.depositar(500);
        System.out.println(c1.toString()); // 123 - saldo: 500
        c1.sacar(200);
        c1.sacar(400); // Saque não vai ser realizado.
        System.out.println(c1.toString()); // 123 - saldo: 300

        // Corrente
        Conta c2 = new Corrente("456", 100);
        c2.depositar(500);
        System.out.println(c2.toString()); // 456 - saldo: 500

        c2.sacar(200);
        c2.sacar(400); // Vou ficar com saldo negativo :(
        System.out.println(c2.toString()); // 456 - saldo: -100

    }

}
