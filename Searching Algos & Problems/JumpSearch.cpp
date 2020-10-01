/* C++ program to implement Jump Search 

Let’s consider the following array: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). Length of the array is 16. Jump search will find the value of 55 with the following steps assuming that the block size to be jumped is 4.
STEP 1: Jump from index 0 to index 4;
STEP 2: Jump from index 4 to index 8;
STEP 3: Jump from index 8 to index 12;
STEP 4: Since the element at index 12 is greater than 55 we will jump back a step to come to index 8.
STEP 5: Perform linear search from index 8 to get the element 55.


*/

#include <bits/stdc++.h> 
using namespace std; 

int jumpSearch(int arr[], int x, int n) 
{ 
	// Finding block size to be jumped 
	int step = sqrt(n); 

	// Finding the block where element is 
	// present (if it is present) 
	int prev = 0; 
	while (arr[min(step, n)-1] < x) 
	{ 
		prev = step; 
		step += sqrt(n); 
		if (prev >= n) 
			return -1; 
	} 

	// Doing a linear search for x in block 
	// beginning with prev. 
	while (arr[prev] < x) 
	{ 
		prev++; 

		// If we reached next block or end of 
		// array, element is not present. 
		if (prev == min(step, n)) 
			return -1; 
	} 
	// If element is found 
	if (arr[prev] == x) 
		return prev; 

	return -1; 
} 

// Driver program to test function 
int main() 
{ 
	int arr[] = { 0, 1, 1, 2, 3, 5, 8, 13, 21, 
				34, 55, 89, 144, 233, 377, 610 }; 
	int x = 55; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	
	// Find the index of 'x' using Jump Search 
	int index = jumpSearch(arr, x, n); 

	// Print the index where 'x' is located 
	cout << "\nNumber " << x << " is at index " << index; 
	return 0; 
} 

// Contributed by nuclode 
