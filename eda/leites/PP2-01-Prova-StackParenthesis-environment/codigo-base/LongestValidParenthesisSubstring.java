package adt.stack.parenthesis;

/**
 * @author Cláudio Campelo
 * 
 * Esta classe contém apenas um método que recebe como parâmetro uma string contendo apenas
 * parênteses e identifica a maior sequência válida de parênteses. Dizemos que uma sequência de parênteses
 * é válida quando todos os parênteses abertos são fechados. A ideia de sequência válida é equivalente
 * a ideia aplicada em expressões matemáticas e em expressões lógicas em linguagens de programação. 
 * Percebe-se, portanto, que a sequência identificada corresponde a alguma substring da string informada. 
 * Esta substring identificada deve ser o retorno do método.
 * 
 * A sua solução DEVE ser baseada em PILHA.
 * Para isto, crie uma instância da classe Stack de Java (java.util.Stack.Stack).
 * Uma única instância é suficiente para resolver o problema.
 * 
 * Exemplos de sequência válida:
 * ()
 * ()()
 * (())
 * ()()()
 * (())(())
 * ()()(())
 * 
 * Exemplos de sequências não válidas:
 * ((
 * )
 * (
 * ))((
 * )((
 * 
 * Exemplos de entrada e saída para o método

 * Entrada: ()
 * Saída: ()
 * Neste caso, há apenas uma sequência válida, portanto, ela é a mais longa.
 * 
 * Entrada: ((()))((
 * Saída: ((()))
 * Neste caso, os dois últimos parênteses denotam uma sequência inválida.
 * Portanto, a sequência anterior é considerada a mais longa válida.
 *  
 * Entrada: ((()))()((()()
 * Saída: ((()))()
 * Neste caso, há duas sequências válidas: ((()))() e ()(). No meio delas
 * há uma sequência inválida: ((. Portanto, a primeira sequência encontrada
 * é considerada o retorno do método, por ser a mais longa. 
 * 
 * OBSERVAÇÕES:
 * 
 * 1. A entrada esperada deve ser sempre strings contendo APENAS parênteses. Caso
 * a entrada não seja dessa forma, o retorno do método deve ser null.
 * 
 * 2. Note que podem haver várias substrings representando sequências válidas, 
 * separadas por outras inválidas.
 * 
 * 3. Caso haja duas sequências válidas de mesmo comprimento (sendo este o 
 * comprimento mais longo) a última sequência deve ser retornada. 
 *
 *
 * RESTRIÇÕES:
 * 
 * 1. A sua solução DEVE ser baseada em PILHA.
 * Para isto, crie uma instância da classe Stack de Java (java.util.Stack.Stack).
 * 
 * 2. Só é permitido usar os seguintes métodos de Stack: push(elem); pop(); isEmpty(); size(); e peek().
 * 
 * 3. Voce deve acessar os caracteres da string sequencialmente. Ou seja, você deve iterar/navegar pelos
 * caracteres (em qualquer direção). Isso significa que você não pode, por exemplo, usar métodos como substring
 * para manipular blocos de caracteres.
 *  
 * ATENÇÃO: se estas restrições não forem respeitadas, a nota atribuída será ZERO. 
 *
 *
 */
public interface LongestValidParenthesisSubstring {

    public String findLongest(String parenthesis);

}
