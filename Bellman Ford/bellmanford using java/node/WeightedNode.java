package node;

import java.util.*;

import mst.DisjointSet;

public class WeightedNode implements Comparable<WeightedNode> {
	public String name;

	private ArrayList<WeightedNode> neighbors = new ArrayList<WeightedNode>();
	private HashMap<WeightedNode, Integer> weightMap = new HashMap<>();
	private boolean isVisited = false;
	private WeightedNode parent;
	private int distance;
	private DisjointSet set; //used in DisjointSet Algorithm

	public WeightedNode(String name) {
		this.name = name;
		distance = Integer.MAX_VALUE;
	}

	public DisjointSet getSet() {
		return set;
	}

	public void setSet(DisjointSet set) { //used in DisjointSet Algorithm
		this.set = set;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public ArrayList<WeightedNode> getNeighbors() {
		return neighbors;
	}

	public void setNeighbors(ArrayList<WeightedNode> neighbors) {
		this.neighbors = neighbors;
	}

	public HashMap<WeightedNode, Integer> getWeightMap() {
		return weightMap;
	}

	public void setWeightMap(HashMap<WeightedNode, Integer> weightMap) {
		this.weightMap = weightMap;
	}

	public boolean isVisited() {
		return isVisited;
	}

	public void setVisited(boolean isVisited) {
		this.isVisited = isVisited;
	}

	public WeightedNode getParent() {
		return parent;
	}

	public void setParent(WeightedNode parent) {
		this.parent = parent;
	}

	public int getDistance() {
		return distance;
	}

	public void setDistance(int distance) {
		this.distance = distance;
	}

	@Override
	public String toString() {
		return name;
	}

	@Override
	public int compareTo(WeightedNode o) {
		return this.distance - o.distance;
	}

}
