/**
 * Classe que representa uma conta Poupança no sistema.
 * 
 * @author Rick Elton
 */
public class Poupanca extends Conta {

    /**
     * Constrói uma instancia da conta do tipo Poupança no sistema.
     * 
     * @param cpf String que representa o cpf do dono da conta.
     */
    public Poupanca(String cpf) {
        super(cpf);
    }

    /**
     * Método sobrescrito da classe pai(Conta), pois a conta Poupança saca de maneira diferente.
     * Pois o saldo não pode ficar com valor negativo.
     * 
     * @return Inteiro valor que foi sacado da minha conta.
     */
    @Override
    public int sacar(int valor) {
        if (this.valor >= valor) {
            this.valor -= valor;
        }
        return valor;
    }
}