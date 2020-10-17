"""
---------------------- Insertion Sort --------------------
"""

n=int(input())
li=[int(x) for x in input().split()]
def insertionSort(li):
    for i in range(1,len(li)):
        j=i-1
        temp=li[i]
        while j>=0 and li[j]>temp:
            li[j+1]=li[j]
            j-=1
        li[j+1]=temp
insertionSort(li)
for i in li:
    print(i,end=" ")