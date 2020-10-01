## Motivation for segment trees.

Suppose we want to do the following operation. We want to find the **sum of all the elements** in the range **[l, r)**, **l** is inclusive and **r** is exclusive. We would also want to perform **point updates** on the array, i.e. **change the value at index I to value v**. And we want to perform Q queries of this type. We can do the following operations in the following ways:

1. We can naively calculate the sum from all elements in the **range [l,r)** in `O(N)`, i.e. linear time. This is too slow. But the advantage we have is that we can update the elements in constant time, `O(1)`.

2. Second type is that we can calculate the prefix sum of the array. This requires pre-processing of `O(N)` time. But we can answer the queries to find the sum of elements in the range from `[l,r)` in `O(1)` time. But now, updating the element at a particular index now takes `O(N)` time, as if we change the first element we need to precompute the prefix sum of the entire array.

3. We can use segment trees. Segment trees allow to query the value of some function applied in the range [l,r) in `O(logN)` time. We can update the element in a particular index in `O(logN)` time too. This is quite fast.

## Structure of Segment Trees

Let's imagine that we need to build a segment tree for the following array:
![enter image description here](https://espresso.codeforces.com/62a4ed9368574e5a3a879804287c51434b5c29a3.png)

The segment tree be constructed as follows. This is a binary tree, in the leaves of which there are elements of the original array, and each internal node contains the sum of the numbers in its children.

![enter image description here](https://espresso.codeforces.com/35bc9067266d25646e8a8a5e4ee10159df770d48.png)

**Note** : The tree turned out so beautiful, because the length of the array was a power of two. If the length of the array is not a power of two, you can extend the array with zeroes to the nearest power of two. In this case, the length of the array will increase no more than twice, so the asymptotic time complexity of the operations will not change.

Now let's look at how to do operations on such a tree.

## **Operation set**

Let's start with the operation `set`. When the element of the array changes, you need to change the corresponding number in the leaf node of the tree, and then recalculate the values that will change from this. These are the values that are higher up the tree from the modified leaf. We can simply recalculate the value in each node as the sum of the values in children.

![enter image description here](https://espresso.codeforces.com/2adeb7419495bbf9ed0dc0dcc64d8bdfd16aaac8.png)

When performing such an operation, we need to recalculate one node on each layer of the tree. We have only `logN` layers, so the operation time will be `O(logN)`.

## Operation sum

Now let's look at how to calculate the sum on a segment. To do this, let's first see what kind of numbers are written in the nodes of the segment tree. Note that these numbers are the sums on some segments of the original array.

![enter image description here](https://espresso.codeforces.com/06bbaebd49114c1f7b823a57786af0726d394655.png)

In this case, for example, the number in the root is the sum over the entire array, and the numbers in the leaves are the sum over the segment of one element.

Let's try to build the sum on the segment `[l..r)` from these already calculated sums. To do this, run a recursive traversal of the segment tree. In this case, we will interrupt recursion in two situations.

- The segment corresponding to the current node does not intersect the segment `[l..r)`. In this case, all the elements in this subtree are outside the area in which we need to calculate the sum, so we can stop the recursion.
- The segment corresponding to the current node is entirely nested in the segment `[l..r)`. In this case, all the elements in this subtree are in the area in which we need to calculate the sum, so we need to add to the answer their sum, which is recorded in the current node.

![enter image description here](https://espresso.codeforces.com/0349d47f2df242db7d9e04098f39fa6bdcacddb3.png)

Here, the crosses indicate the vertices at which the recursion broke off in the first cutoff, and the vertices in which the number was added to the answer are circled.

How long does such a tree traversal work? To answer this question, we need to understand how many nodes none of the cutoffs will happen in, and we will need to go deeper into the tree. Each such case gives us a new branch of recursion. It turns out that there will be quite a few such nodes. The fact is that in order for none of the cutoffs to work, the segment corresponding to the node of the tree must intersect the query segment, but not be contained in it entirely. This is only possible if it contains one of the boundaries of the segment `[l..r)`. But on each layer of the tree of segments there can be no more than one segment containing each of the boundaries. Thus, there can be no more than `2logN` nodes at which cutoffs did not work, and, therefore, the general asymptotic time of this procedure will be `O(logN)`.

### In what other type of operation can we use segment trees ?

In addition to the sum , using the segment tree, you can calculate any associative operation. The operation `⊗` is called associative if its result does not depend on the order in which it is calculated, that is, if `(a⊗b)⊗c=a⊗(b⊗c)`.
