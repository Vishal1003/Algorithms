"""
------------------- Bubble Sort --------------------
Sort an array using 'Bubble Sort'.
"""
n=int(input())
li=[int(x) for x in input().split()]
def bubbleSort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
bubbleSort(li)
for i in li:
    print(i,end=" ")