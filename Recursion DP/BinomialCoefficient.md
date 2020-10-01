Binomial Coeeficients
=============================
We call nCr (read as n choose ) as the Binomial Coeffiecient. In the terms of Combinatorics this the number of ways we can select r items for a group of n distint items if the ordering of the selection does not matter. This is quite common in combinatorics problems in Competitive Programming.

I suggest an algorithm which has O(n) preprocessing anf O(n) space. It can then resolve each query for nCr%prime in O(log(prime)) time.

Algorithm
-----------------------------

1. Calculate the value of factorials from 0 to n and store them in an array.
2. Calculate the product of r! and (n-r)! using the arr array.
3. Find the inervse modulo of the product in Step 2. This can be done using Fast Exponentiation in O(log(prime)) time.
4. return the final answer as product of n! (from the arr array) and the Inverse Modulo found in Step 3.

