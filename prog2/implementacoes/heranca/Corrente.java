/**
 * Classe que representa o tipo de conta Corrente no sistema.
 * 
 * @author Rick Elton
 */
public class Corrente extends Conta {

    private int ch;

    /**
     * Constrói uma instancia de conta Corrente.
     * 
     * @param cpf String que representa o cpf do dono da conta.
     * @param ch Inteiro que representa o valor a mais que posso sacar.
     */
    public Corrente(String cpf, int ch) {
        super(cpf);
        this.ch = ch;
    }

    /**
     * Método sobrescrito da classe pai(Conta), pois a conta Corrente saca de maneira diferente.
     * Pois o saldo pode ficar negativo.
     * 
     * @return Inteiro valor que foi sacado da minha conta.
     */
    @Override
    public int sacar(int valor) {
        if (this.valor + this.ch >= valor) {
            this.valor -= valor;
        }
        return valor;
    }
}