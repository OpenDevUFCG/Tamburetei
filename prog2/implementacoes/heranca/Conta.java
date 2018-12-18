/**
 * Classe abstrata responsável pela representação de uma conta no sistema.
 * 
 * @author Rick Elton
 */
public abstract class Conta {

    protected int valor;
    private String cpf;

    /**
     * Constrói uma nova instancia de Conta no sistema a partir do CPF.
     *  
     * @param cpf String que representa o cpf do dono da conta.
     */
    public Conta(String cpf) {
        this.cpf = cpf;
        this.valor = 0;
    }

    /**
     * Método que irá realizar depositos na conta.
     * 
     * @param valor Inteiro que representa o valor a ser depositado na conta.
     * @return Inteiro saldo da conta depois do deposito.
     */
    public int depositar(int valor) {
        this.valor += valor;
        return this.valor;
    }

    /**
	 * Sobrescrita do método toString, que vai retornar uma representação em
	 * String de uma instância de Conta, a partir de seus dois campos: cpf, 
	 * e valor(saldo).
	 */
    @Override
    public String toString() {
        return this.cpf + " - saldo: " + this.valor;
    }

    /**
     * Método abstrato para sacar um determinado valor da conta. Já que cada tipo de 
     * conta saca de maneiras diferentes.
     * 
     * @param valor Inteiro que representa o valor a ser sacado da minha conta.
     * @return Inteiro valor que foi sacado da minha conta.
     */
    public abstract int sacar(int valor);
}