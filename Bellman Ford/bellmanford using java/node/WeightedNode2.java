package node;

import java.util.*;

import mst.DisjointSet;

public class WeightedNode2 implements Comparable<WeightedNode2> {
	public String name;

	private ArrayList<WeightedNode2> neighbors = new ArrayList<WeightedNode2>();
	private HashMap<WeightedNode2, Integer> weightMap = new HashMap<>();
	private boolean isVisited = false;
	private WeightedNode2 parent;
	private int distance;
	private DisjointSet set;

	public WeightedNode2(String name) {
		this.name = name;
		distance = Integer.MAX_VALUE;
	}

	public DisjointSet getSet() {
		return set;
	}

	public void setSet(DisjointSet set) {
		this.set = set;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public ArrayList<WeightedNode2> getNeighbors() {
		return neighbors;
	}

	public void setNeighbors(ArrayList<WeightedNode2> neighbors) {
		this.neighbors = neighbors;
	}

	public HashMap<WeightedNode2, Integer> getWeightMap() {
		return weightMap;
	}

	public void setWeightMap(HashMap<WeightedNode2, Integer> weightMap) {
		this.weightMap = weightMap;
	}

	public boolean isVisited() {
		return isVisited;
	}

	public void setVisited(boolean isVisited) {
		this.isVisited = isVisited;
	}

	public WeightedNode2 getParent() {
		return parent;
	}

	public void setParent(WeightedNode2 parent) {
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
	public int compareTo(WeightedNode2 o) {
		return this.distance - o.distance;
	}

}
