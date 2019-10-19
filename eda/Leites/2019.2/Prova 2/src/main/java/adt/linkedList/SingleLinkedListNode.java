package adt.linkedList;

public class SingleLinkedListNode<T> {
	protected T data;
	protected SingleLinkedListNode<T> next;

	/**
	 * Constructor of an empty (NIL) node
	 */
	public SingleLinkedListNode() {
	}

	public SingleLinkedListNode(T data, SingleLinkedListNode<T> next) {
		this.data = data;
		this.next = next;
	}

	public T getData() {
		return data;
	}

	public SingleLinkedListNode<T> getNext() {
		return next;
	}

	public boolean isNIL() {
		return (this.data == null);
	}

	@Override
	public String toString() {
		String resp = null;
		if (!isNIL()) {
			resp = this.data.toString();
		} else {
			resp = "NIL";
		}
		return resp;
	}

	@SuppressWarnings("unchecked")
	@Override
	public boolean equals(Object obj) {
		boolean resp = false;
		if (obj instanceof SingleLinkedListNode) {
			if (!this.isNIL()) {
				resp = this.data.equals(((SingleLinkedListNode<T>) obj).data);
			} else {
				resp = ((SingleLinkedListNode<T>) obj).isNIL();
			}

		}
		return resp;
	}

	public void setData(T data) {
		this.data = data;
	}

	public void setNext(SingleLinkedListNode<T> next) {
		this.next = next;
	}

}
