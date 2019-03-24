/**
 * Classe que representa um imposto que deve seguir o padrão de cálculo
 * do IPI (Imposto sobre Produtos Industrializados).
 * 
 * @author Lucas de Medeiros
 */
public class IPI implements Imposto {

    private static final double PERCENT = 0.2;
    private double valor;

    /**
     * Construtor de IPI a partir do valor.
     * 
     * @param valor valor, em reais, de uma receita a ser aplicada o imposto.
     */
    public IPI(double valor) {
        this.valor = valor;
    }

    /**
     * Implementção da lógica para o cálculo do imposto seguindo a estratégia IPI.
     * 
     * @return cálculo do imposto IPI
     */
    @Override
    public double calcular() {
        // Lógica para o cálculo do imposto seguindo a estratégia IPI.
        return this.valor * PERCENT;
    }
}