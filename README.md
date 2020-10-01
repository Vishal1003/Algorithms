# Important Algorithms

### Selection Sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1. The subarray which is already sorted.
2. Remaining subarray which is unsorted.

### Merge Sort

Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

### Quick Sort

QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

### HeapSort

Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.

### Counting Sort

Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence.

### Comb Sort

Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using gap of size more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion counts with one swap and performs better than Bubble Sort.

The shrink factor has been empirically found to be 1.3 (by testing Combsort on over 200,000 random lists)

Although, it works better than Bubble Sort on average, worst case remains O(n2).

### Bitonic Sort

Bitonic Sort is a classic parallel algorithm for sorting.
Bitonic sort does O(n Log 2n) comparisons.
The number of comparisons done by Bitonic sort are more than popular sorting algorithms like Merge Sort [ does O(nLogn) comparisons], but Bitonice sort is better for parallel implementation because we always compare elements in predefined sequence and the sequence of comparison doesn’t depend on data. Therefore it is suitable for implementation in hardware and parallel processor array.

### Insertion Sort
Insertion Sort is a very simple sorting algorithm which works similar to the way we arrange playing card in our hands. In this method the array is virtually split into two parts one being sorted and other being unsorted. We select an element from the unsorted part and find it's correct position in the sorted part.

Let's take an array of size n then,
Set the iterator pointing to arr[1]
Compare the current element to its predecessor
loop through this comparison with predecessor until you find the correct position of the current element
increment the iterator

Insertion sort works best for already sorted or almost sorted array with time complexity O(n), whereas worst case time complexity being o(n^2).

### Shell Sort
Shell Sort is an efficient sorting algorithm which is a variant of the Insertion Sort algorithm. We avoid large shifts as compared to Insertion Sort. The worse-case time complexity of shell sort depends on the increment sequence which is O(n<sup>3/2</sup>) and for certain increments O(n<sup>4/3</sup>). For many practical variants, determining their time complexity remains an open problem. 


### Binary Search

Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
A simple approach is to do linear search.The time complexity of above algorithm is O(n). Another approach to perform the same task is using Binary Search.

Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).

### Jump Search

Like Binary Search, Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

### Interpolation Search

Given a sorted array of n uniformly distributed values arr[], write a function to search for a particular element x in the array.

Linear Search finds the element in O(n) time, Jump Search takes O(√ n) time and Binary Search take O(Log n) time.
The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

### Exponential Search

The name of this searching algorithm may be misleading as it works in O(Log n) time. The name comes from the way it searches an element.

An exponential search is a combination of two methods:

- Find the range in which the element exists.
- Perform a binary search in that range.

To begin a search, we find the range. We do this by first checking to see if the desired element is in the first position. If not, we try an array size of 2, then 4, then 6... and so on. If the last element in the partial array is not greater than the element, we perform a binary search.

In order for exponential search to work the array must be sorted!

### Breadth First Search

BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level neighbour nodes.
As the name BFS suggests, you are required to traverse the graph breadthwise as follows:

1. First move horizontally and visit all the nodes of the current layer
2. Move to the next layer

-[ALGORITHM](https://github.com/Mu-C00L/Algorithms/blob/master/BFS%20Algorithm) -[CODE](https://github.com/Mu-C00L/Algorithms/blob/master/BFS)

### Flood Fill Algorithm

Flood fill, also called seed fill, is an algorithm that determines the area connected to a given node in a multi-dimensional array. It is used in the "bucket" fill tool of paint programs to fill connected, similarly-colored areas with a different color, and in games such as Go and Minesweeper for determining which pieces are cleared.

[ALGORITHM](https://github.com/sahanihit/Algorithms/blob/master/Flood%20Fill%20Algorithm.md)

### Kadane's Algorithm

Kadane's algorithm is a Dynamic Programming approach to solve “the largest contiguous elements in an array” with runtime of O(n). In this blog post we rewrote the algorithm to use an array instead of sum (which needs more space to hold them) that makes it a bit more easier to understand.
[ALGORITHM](https://github.com/shubhdeep123/Algorithms/blob/Kalgo/kadaneAlgo.md)

### Union Find Algorithm

A disjoint-set data structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. A union-find algorithm is an algorithm that performs two useful operations on such a data structure:

Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.

Union: Join two subsets into a single subset.

Union-Find Algorithm can be used to check whether an undirected graph contains cycle or not. Note that we have discussed an algorithm to detect cycle. This is another method based on Union-Find. This method assumes that the graph doesn’t contain any self-loops.

### Kruskal's Algorithm (Minimum Spanning Tree)

Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. If the graph is connected, it finds a minimum spanning tree. (A minimum spanning tree of a connected graph is a subset of the edges that forms a tree that includes every vertex, where the sum of the weights of all the edges in the tree is minimized. For a disconnected graph, a minimum spanning forest is composed of a minimum spanning tree for each connected component.) It is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that will not form a cycle to the minimum spanning forest.
[ALGORITHM](https://github.com/shubhdeep123/Algorithms/blob/kruskal/kruskalAlgo.md)

### Topographical Sorting in a DAG (directed acyclic graph)

Topological sort of a directed acyclic graph [DAG] is partial ordering of its nodes such that U < V implies there must not exist a path from V to U.

Kahn’s algorithm I implemented, instead produces a linear ordering such that […, U, …, V, …] means there may be a path from U to V, but not vice versa. [ALGORITHM](https://github.com/Harshit564/Algorithms/blob/master/topologicalsort.md)

### Segment Tree Implementation with Range Query and Point Update
Segment tree is a data structure that allows us to perform range queries and point updates in `O(logN)` time. Range Updates is also possible in Segment Trees, but i have implemented only Range Queries and Point Updates.
[ALGORITHM](segtree.md)

## Cycle Detection in Directed Graph
Given a directed graph, this program checks whether the graph conatins a cycle or not. The function returns true if the graph conatins at least one cycle , else returns false. Here we use DFS (Depth First Search) to detect the cycle.DFS for a connected graph produces a tree. There is a cycle in a graph only if there is a back edge present in the graph. A back edge is an edge that is from a node to itself (self-loop) or one of its ancestors in the tree produced by DFS.
[ALGORITHM](CycleDetectionDirectedGraph.cpp). for more info check out [this](https://www.geeksforgeeks.org/detect-cycle-in-a-graph/).

