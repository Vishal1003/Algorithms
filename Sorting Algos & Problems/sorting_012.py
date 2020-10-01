#Sort an array of 0s, 1s and 2s 
#It is a problem from geeksforgeeks and can be solved using python code
#Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

# Here t is the number of test cases,
# i is an iterative variable,
# n is the number of elements in list,
# x is the list in which elements are to be entered
# and sort() is a python in-built function which will sort the list of elements in ascending order

t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    for i in x: print(i, end=" ")
    print()
   
#This code is contributed by Akhil
