"""
-------------------------------- Merge Sort ---------------------------- 

Sort an array A using Merge Sort.
"""

def mergeSort(arr, start, end): 

    size=end-start 
    if size<=1: 
        return 

    mid = (start+end)//2 
    mergeSort(arr, start, mid) 
    mergeSort(arr, mid, end) 

    #Merge Two Sorted lists 
    result = [0] * size 
    i=start 
    j=mid 
    k=0 

    while(i<mid and j<end): 
        if(arr[i]<arr[j]): 
            result[k] = arr[i]
            k += 1 
            i += 1 
        else: 
            result[k] = arr[j] 
            k += 1 
            j += 1 

    while(i<mid): 
        result[k] = arr[i] 
        k += 1 
        i += 1 

    while(j<end): 
        result[k] = arr[j] 
        k += 1 
        j += 1 

    for i in range(0,size): 
        arr[start+i] = result[i] 
        
# Main 
n=int(input()) 
arr=list(int(i) for i in input().strip().split(' ')) 
mergeSort(arr, 0, n) 
for num in arr: 
    print(num, end=' ') 
    print()