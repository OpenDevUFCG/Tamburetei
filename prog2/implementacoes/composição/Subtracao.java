/**
 * Classe que representa a operação de subtração.
 * 
 * @author Lucas de Medeiros
 */
public class Subtracao implements Operacao {

    /**
     * Retorna a multiplicação de dois números.
     * 
     * @param valor1 primeiro valor.
     * @param valor2 segundo valor.
     * @return a subtração de valor1 por valor2.
     */
    @Override
    public double calcular(double valor1, double valor2) {
        return valor1 - valor2;
    }
}