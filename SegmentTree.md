### What is a Segment Tree

A Segment Tree is a data structure that allows answering range queries over an array effectively, while still being flexible enough to allow modifying the array. 
This includes finding the sum of consecutive array elements a[l…r], or finding the minimum element in a such a range in O(logn) time. Between answering such queries 
the Segment Tree allows modifying the array by replacing one element, or even change the elements of a whole subsegment (e.g. assigning all elements a[l…r] to any value, 
or adding a value to all element in the subsegment).

### Simplest form of a Segment Tree

To start easy, we consider the simplest form of a Segment Tree. We want to answer sum queries efficiently. The formal definition of our task is: 
We have an array a[0…n−1], and the Segment Tree must be able to find the sum of elements between the indices l and r (i.e. computing the sum ∑ri=la[i]), 
and also handle changing values of the elements in the array (i.e. perform assignments of the form a[i]=x). The Segment Tree should be able to process both queries in O(logn) time.

### Construction

Before constructing the segment tree, we need to decide:

the value that gets stored at each node of the segment tree. For example, in a sum segment tree, a node would store the sum of the elements in its range [l,r].
the merge operation that merges two siblings in a segment tree. For example, in a sum segment tree, the two nodes corresponding to the ranges a[l1…r1] and a[l2…r2] would be merged into a node corresponding to the range a[l1…r2] by adding the values of the two nodes.
Note that a vertex is a "leaf vertex", if its corresponding segment covers only one value in the original array. It is present at the lowermost level of a segment tree. Its value would be equal to the (corresponding) element a[i].

Now, for construction of the segment tree, we start at the bottom level (the leaf vertices) and assign them their respective values. On the basis of these values, we can compute the values of the previous level, using the merge function. And on the basis of those, we can compute the values of the previous, and repeat the procedure until we reach the root vertex.

It is convenient to describe this operation recursively in the other direction, i.e., from the root vertex to the leaf vertices. The construction procedure, if called on a non-leaf vertex, does the following:

recursively construct the values of the two child vertices
merge the computed values of these children.
We start the construction at the root vertex, and hence, we are able to compute the entire segment tree.

The time complexity of this construction is O(n), assuming that the merge operation is constant time (the merge operation gets called n times, which is equal to the number of internal nodes in the segment tree).
