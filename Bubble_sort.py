def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr
              
if __name__ == "__main__":
    arr = [2,3,1,5,4]
    print(bubbleSort(arr))
  
