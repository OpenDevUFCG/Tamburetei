/**
 * Classe principal para exemplificar composição em Java.
 * 
 * @author Lucas de Medeiros
 */

public class Main {

    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora(5.0, 2.0);

        // Como a operação padrão é soma, imprime o valor da soma entre os números.
        System.out.println(calculadora.calcular());

        Operacao multiplicacao = new Multiplicacao();
        calculadora.setOperacao(multiplicacao);

        // Imprime o valor da multiplicação entre os números.
        System.out.println(calculadora.calcular());

        Operacao subtracao = new Subtracao();
        calculadora.setOperacao(subtracao);

        // Imprime o valor da subtração entre os números.
        System.out.println(calculadora.calcular());

        Operacao divisao = new Divisao();
        calculadora.setOperacao(divisao);

        // Imprime o valor da divisão entre os números.
        System.out.println(calculadora.calcular());
    }
}