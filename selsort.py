#python3
#This is a python file to show how to selection sort without using the actual <list>.sort() function.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minimum_index = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum_index]:
                minimum_index = j
        arr[minimum_index], arr[i] = arr[i], arr[minimum_index]
    return arr

if __name__ == "__main__":
    a = [1,4,3,2,5]
    a = selection_sort(arr)
    print(a)
    
        
        

