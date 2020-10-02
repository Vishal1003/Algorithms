"""
-----------------------------------  Inplace Heap Sort  --------------------------------

Given an integer array of size n. Sort this array (in decreasing order) using heap sort.
"""

def down_heapify(arr,i,n):
    parentIndex=i
    leftChildIndex=2*parentIndex+1
    rightChildIndex=2*parentIndex+2
    
    while leftChildIndex<n:

        minIndex=parentIndex

        if arr[minIndex]>arr[leftChildIndex]:
            minIndex=leftChildIndex

        if rightChildIndex<n and arr[minIndex]>arr[rightChildIndex]:
            minIndex=rightChildIndex
        
        if minIndex==parentIndex:
            return

        arr[minIndex],arr[parentIndex]=arr[parentIndex],arr[minIndex]

        parentIndex=minIndex

        leftChildIndex=2*parentIndex+1
        rightChildIndex=2*parentIndex+2
    return

def heapSort(arr):

    n=len(arr)
    for i in range(n//2 -1,-1,-1):
        down_heapify(arr,i,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        down_heapify(arr,0,i)

    return
	
#main
n=int(input())
arr=[int(ele) for ele in input().split()]
heapSort(arr)
print(*arr)