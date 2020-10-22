package node;

import java.util.ArrayList;

public class NumberOfPathsNode {

	int costToReachLastCell = 0;
	int costOfCurrentCell = 0;
	NumberOfPathsNode rightCell = null;
	NumberOfPathsNode downCell = null;
	int numberOfWaysToComeHereFromRightOrDown = 0;
	ArrayList<Integer> NumberOfWaysSatifyingDownCell = new ArrayList<Integer>();
	ArrayList<Integer> NumberOfWaysSatifyingRightCell = new ArrayList<Integer>();
	
	
	
	//Constructor
	public NumberOfPathsNode(int costOfCurrentCell, NumberOfPathsNode rightCell, NumberOfPathsNode DownCell, int costToReachLastCell) {
		this.costOfCurrentCell = costOfCurrentCell;
		this.rightCell = rightCell;
		this.downCell = DownCell;
		this.costToReachLastCell = costToReachLastCell;
	}
	
	
	
	
	//Getting numbers of ways to reach last cell from current cell
	public int getnumberOfWaysToReachLastCellFromHere() {
		int numberOfWaysToReachLastCellFromHere = 0;
		for(int i=0; i<NumberOfWaysSatifyingRightCell.size(); i++) {
			if(NumberOfWaysSatifyingRightCell.get(i) == costOfCurrentCell) {
				numberOfWaysToReachLastCellFromHere++;
			}
		}
		for(int i=0; i<NumberOfWaysSatifyingDownCell.size(); i++) {
			if(NumberOfWaysSatifyingDownCell.get(i) == costOfCurrentCell) {
				numberOfWaysToReachLastCellFromHere++;
			}
		}
		return numberOfWaysToReachLastCellFromHere;
	}
	
	
	//Calculate number ways
	public void setNumberOfWaysToComeHereFromRightOrDown() {
		
		numberOfWaysToComeHereFromRightOrDown = NumberOfWaysSatifyingDownCell.size() + NumberOfWaysSatifyingRightCell.size();
		System.out.println("numberOfWaysToComeHereFromRightOrDown: " + numberOfWaysToComeHereFromRightOrDown);
		for(int i=0; i<NumberOfWaysSatifyingDownCell.size();i++) {
			System.out.println("DownArray: " + NumberOfWaysSatifyingDownCell.get(i) + "  ");
		}
		
		for(int i=0; i<NumberOfWaysSatifyingRightCell.size();i++) {
			System.out.println("RightArray: " + NumberOfWaysSatifyingRightCell.get(i) + "  ");
			
		}
		
	}
	
	
	//Calculate number of ways to come here from Right cell
	public void calculateNumberOfWaysSatifyingRightCell(){
		if(rightCell == null) { 
			return;
		}
		
		int sizeOfRightCellsRight = rightCell.NumberOfWaysSatifyingRightCell.size();
		int sizeOfRightCellsDown  = rightCell.NumberOfWaysSatifyingDownCell.size();
		
		for(int i=0; i<sizeOfRightCellsRight; i++) {
			if(rightCell.NumberOfWaysSatifyingRightCell.get(i) >= rightCell.costOfCurrentCell) {
				NumberOfWaysSatifyingRightCell.add(rightCell.NumberOfWaysSatifyingRightCell.get(i)-rightCell.costOfCurrentCell);
			}
		}//end of loop
		
		for(int i=0; i<sizeOfRightCellsDown; i++) {
			if(rightCell.NumberOfWaysSatifyingDownCell.get(i) >= rightCell.costOfCurrentCell) {
				NumberOfWaysSatifyingRightCell.add(rightCell.NumberOfWaysSatifyingDownCell.get(i)-rightCell.costOfCurrentCell);
			}
		}//end of loop
	}//end of method
	
	
	//Calculate number of ways to come here from Down cell
		public void calculateNumberOfWaysSatifyingDownCell(){
			if((downCell == null) && (rightCell == null)) { //Base case for last row and col
				NumberOfWaysSatifyingDownCell.add(costToReachLastCell);
			}
			
			if(downCell == null) {
				return;
			}
			
			int sizeOfDownCellsRight = downCell.NumberOfWaysSatifyingRightCell.size();
			int sizeOfDownCellsDown = downCell.NumberOfWaysSatifyingDownCell.size();
			
			for(int i=0; i<sizeOfDownCellsRight; i++) {
				if(downCell.NumberOfWaysSatifyingRightCell.get(i) >= downCell.costOfCurrentCell) {
					NumberOfWaysSatifyingDownCell.add(downCell.NumberOfWaysSatifyingRightCell.get(i)-downCell.costOfCurrentCell);
				}
			}//end of loop
			
			for(int i=0; i<sizeOfDownCellsDown; i++) {
				if(downCell.NumberOfWaysSatifyingDownCell.get(i) >= downCell.costOfCurrentCell) {
					NumberOfWaysSatifyingDownCell.add(downCell.NumberOfWaysSatifyingDownCell.get(i)-downCell.costOfCurrentCell);
				}
			}//end of loop
		}//end of method
	
}//end of class

