## PROBLEM LINK
[https://www.codechef.com/JUNE20B/problems/EVENM](https://www.codechef.com/JUNE20B/problems/EVENM)

## EXPLANATION
* It is given that the matrix M will be a NxN matrix with numbers from 1 to N^2. So, it is clear that all the numbers from 1 to N^2 will be present in the matrix.
* According to the conditions, adjacent diagonal elements (left diagonal as well as right diagonal) should add up to an even number. Therefore, adjacent diagonal elements should be either both even or both odd.
* It can be observed that if the numbers are placed serially from 1 to N^2 row-wise but from opposite directions for adjacent rows, then the above condition can be met.
### WHY?
* Let the length of a row be N.
* Numbers from 1 to N will be placed in first row from left to right.
* The (N+1)th number will be placed just below Nth number which will be diagonally adjacent to (N-1)th number in previous row.
* We know that the parity of (N+1)th number and (N-1)th number will be same.
* And this pattern will continue for the rest of the numbers for each row.
## Hence, this method of placing numbers will work for any N.