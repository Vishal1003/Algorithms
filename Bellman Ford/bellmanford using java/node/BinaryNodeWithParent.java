package node;

public class BinaryNodeWithParent {
	private int value;
	private BinaryNodeWithParent parent;
	private BinaryNodeWithParent left;
	private BinaryNodeWithParent right;
	
	public int getValue() {
		return value;
	}

	public void setValue(int value) {
		this.value = value;
	}

	public BinaryNodeWithParent getParent() {
		return parent;
	}

	public void setParent(BinaryNodeWithParent parent) {
		this.parent = parent;
	}

	public BinaryNodeWithParent getLeft() {
		return left;
	}

	public void setLeft(BinaryNodeWithParent left) {
		this.left = left;
	}

	public BinaryNodeWithParent getRight() {
		return right;
	}

	public void setRight(BinaryNodeWithParent right) {
		this.right = right;
	}

	@Override
	public String toString() {
		return value+"";
	}

}
