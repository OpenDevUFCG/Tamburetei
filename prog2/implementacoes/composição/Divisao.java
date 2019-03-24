/**
 * Classe que representa a operação de divisão.
 * 
 * @author Lucas de Medeiros
 */
public class Divisao implements Operacao {

    /**
     * Retorna a divisão de dois números.
     * 
     * @param valor1 primeiro valor.
     * @param valor2 segundo valor.
     * @return a divisão de valor1 por valor2.
     * @throws IllegalArgumentException caso valor2 seja igual a 0
     */
    @Override
    public double calcular(double valor1, double valor2) {
        if (valor2 == 0) {
            throw new IllegalArgumentException("O segundo valor não pode ser igual a 0!");
        }

        return valor1 / valor2;
    }
}