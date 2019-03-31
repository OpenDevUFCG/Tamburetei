/**
 * Classe que representa a operação de soma.
 * 
 * @author Lucas de Medeiros
 */
public class Soma implements Operacao {

    /**
     * Retorna a soma de dois números.
     * 
     * @param valor1 primeiro valor.
     * @param valor2 segundo valor.
     * @return a soma de valor1 com valor2.
     */
    @Override
    public double calcular(double valor1, double valor2) {
        return valor1 + valor2;
    }
}
