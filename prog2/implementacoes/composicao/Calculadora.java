/**
 * Classe que representa uma calculadora simples, que deve ser capaz
 * de realizar as quatro operações básicas.
 * 
 * @author Lucas de Medeiros
 */
public class Calculadora {

    private double valor1;
    private double valor2;
    private Operacao operacao;

    /**
     * Construtor de calculadora a partir dos valores.
     * 
     * @param valor1 primeiro valor
     * @param valor2 segundo valor
     */
    public Calculadora(double valor1, double valor2) {
        this.valor1 = valor1;
        this.valor2 = valor2;

        // Garantindo que o valor padrão para a operação seja de soma.
        this.operacao = new Soma();
    }

    /**
     * Método set para a operação.
     * 
     * 
     * @param operacao operação que deve ser feita no método calcular,
     * caracterizando uma composição.
     */
    public void setOperacao(Operacao operacao) {
        this.operacao = operacao;
    }

    /**
     * Calcula o valor a partir da operação.
     * 
     * @return resultado da operação.
     */
    public double calcular() {
        return this.operacao.calcular(this.valor1, this.valor2);
    }
}
