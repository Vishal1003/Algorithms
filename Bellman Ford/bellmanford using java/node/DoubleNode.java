package node;


public class DoubleNode {
	private int value;
	private DoubleNode next;
	private DoubleNode prev;
	
	public int getValue() {
		return value;
	}

	public void setValue(int value) {
		this.value = value;
	}

	public DoubleNode getNext() {
		return next;
	}

	public void setNext(DoubleNode next) {
		this.next = next;
	}

	public DoubleNode getPrev() {
		return prev;
	}

	public void setPrev(DoubleNode prev) {
		this.prev = prev;
	}

	@Override
	public String toString() {
		return  value + "";
	}

}
