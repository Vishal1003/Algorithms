# Count Sort
Counting Sort is a linear sorting algorithm with asymptotic complexity O(n+k).
Counting Sort is very time efficient and stable algorithm for sorting. 
Unlike bubble sort and merge sort, counting sort is not a comparison based algorithm. It avoids comparisons and exploits the O(1) time insertions and lookup in an array.

## pseudo code:
```
  CountingSort(A)
    //A[]-- Initial Array to Sort
    //Complexity: O(k)
    for i = 0 to k do
    c[i] = 0
    //Storing Count of each element
    //Complexity: O(n)
    for j = 0 to n do
    c[A[j]] = c[A[j]] + 1
    // Change C[i] such that it contains actual
    //position of these elements in output array
    ////Complexity: O(k)
    for i = 1 to k do
    c[i] = c[i] + c[i-1]
    //Build Output array from C[i]
    //Complexity: O(n)
    for j = n-1 downto 0 do
    B[ c[A[j]]-1 ] = A[j]
    c[A[j]] = c[A[j]] - 1
  end func
  ```
  
##  ASYMPTOTIC ANALYSIS OF COUNTING SORT
In this algorithm, the initialization of the count array and the loop which performs a prefix sum on the count array takes O(k) time. And other two loops for initialization of the output array takes O(n) time. Therefore, the total time complexity for the algorithm is : O(k)+ O(n)+ O(k)+ O(n)= O(n+k).
```
Worst Case Time complexity: O (n+k)
Average Case Time complexity: O(n+k)
Best Case Time complexity: O(n+k)
Space Complexity: O(k)
Data Structure: Array
Sorting In Place: No
Stable: Yes
```
