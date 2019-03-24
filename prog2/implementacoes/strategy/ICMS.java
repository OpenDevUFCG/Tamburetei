/**
 * Classe que representa um imposto que deve seguir o padrão de cálculo
 * do ICMS (Imposto sobre Circulação de Mercadorias e Serviços).
 * 
 * @author Lucas de Medeiros
 */
public class ICMS implements Imposto {

    private static final double PERCENT = 0.10;
    private double valor;

    /**
     * Construtor de ICMS a partir do valor.
     * 
     * @param valor valor, em reais, de uma receita a ser aplicada o imposto.
     */
    public ICMS(double valor) {
        this.valor = valor;
    }

    /**
     * Implementção da lógica para o cálculo do imposto seguindo a estratégia ICMS.
     * 
     * @return cálculo do imposto ICMS
     */
    @Override
    public double calcular() {
        return this.valor * PERCENT;
    }
}