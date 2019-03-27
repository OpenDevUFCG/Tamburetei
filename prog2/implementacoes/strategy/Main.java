/**
 * Classe principal para exemplificar padrão Strategy em Java.
 * 
 * @author Lucas de Medeiros
 */
public class Main {
    public static void main(String[] args) {
        // Imprimindo o resultado do cálculo de imposto seguindo a estratégia ICMS.
        Imposto icms = new ICMS(50.0);
        System.out.println(icms.calcular());

        // Imprimindo o resultado do cálculo de imposto seguindo a estratégia IPI.
        Imposto ipi = new IPI(50.0);
        System.out.println(ipi.calcular());
    }
}
