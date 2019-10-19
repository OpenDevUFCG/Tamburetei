/**
 * Classe que representa uma pilha implementada usando-se um noh de uma lista
 * simplesmente ligada, como estrutura sobrejacente. 
 * 
 * Restricoes:
 * - Complexidade dos metodos deve ser em O(1).
 * - Voce nao deve usar estrutura auxiliar que faça uso de memoria extra.
 * - Metodos auxiliares que voce desenvolver deve ser implementados nessa classe.
 *
 * @param <T>
 */
public class StackSingleLinkedListNodeImpl<T> implements Stack<T> {
	
	private SingleLinkedListNode<T> top;
	private Integer tamanhoMax;
	private Integer size;

	/**
	 * A pilha para ser criada precisa ter um tamanho maximo
	 * @param tamanhoMaximo
	 */
	public StackSingleLinkedListNodeImpl(int tamanhoMaximo) {
		this.top = new SingleLinkedListNode<T>();
		this.tamanhoMax = tamanhoMaximo;
		this.size = 0;
	}

	@Override
	public void push(T element) throws StackOverflowException {
		if (element != null && size < tamanhoMax){
			SingleLinkedListNode newNode = new SingleLinkedListNode(element, this.top);
			this.top = newNode;
			this.size++;
		} else if (this.size >= this.tamanhoMax) {
		    throw new StackOverflowException();
        }
	}

	@Override
	public T pop() throws StackUnderflowException {
	    T result;

	    if (this.size > 0){
	        result = this.top.getData();
	        this.top = this.top.getNext();
	        size--;
        } else {
	        throw new StackUnderflowException();
        }
        return result;
	}

	@Override
	public T top() {
	    T result = null;

		if (!this.isEmpty()){
		    result = this.top.getData();
        }

        return result;
	}

	@Override
	public boolean isEmpty() {
		return size == 0;
	}

	@Override
	public boolean isFull() {
        return size == tamanhoMax;
	}

}
