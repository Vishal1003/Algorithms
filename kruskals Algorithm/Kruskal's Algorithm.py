"""
----------------------------- Kruskal's Algorithm ----------------------------

Given an undirected, connected and weighted graph G(V, E) with V number of 
vertices (which are numbered from 0 to V-1) and E number of edges.

Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.

Input Format :
    Line 1: Two Integers V and E (separated by space)
    Next E lines : Three integers ei, ej and wi, denoting that there exists 
    an edge between vertex ei and vertex ej with weight wi (separated by space)
	
Output Format :
    MST
	
Sample Input :
    4 4
    0 1 3
    0 3 5
    1 2 1
    2 3 8
Sample Output :
    1 2 1
    0 1 3
    0 3 5
"""

class Edge:
    def __init__(self,src,dest,wt):
        self.src=src
        self.dest=dest
        self.wt=wt
        
def getParent(v,parent):
    if v==parent[v]:
        return v
    return getParent(parent[v],parent)
def kruskal(edges,nVertices):
    parent = [i for i in range(nVertices)]
    edges=sorted(edges,key=lambda edge:edge.wt)
    count=0
    output=[]
    i=0
    while count<(nVertices-1):
        currentEdge=edges[i]
        srcParent=getParent(currentEdge.src,parent)
        destParent=getParent(currentEdge.dest,parent)
        if srcParent!=destParent:
            output.append(currentEdge)
            count+=1
            parent[srcParent]=destParent
        i+=1
    return output
            
li=[int(ele) for ele in input().split()]
n=li[0]
E=li[1]
edges=[]

for i in range(E):
    curr_input=[int(ele) for ele in input().split()]
    src=curr_input[0]
    dest=curr_input[1]
    wt=curr_input[2]
    edge=Edge(src,dest,wt)
    edges.append(edge)
output=kruskal(edges,n)

for edge in output:
    if edge.src < edge.dest:
        print(str(edge.src) + " " + str(edge.dest) + " " + str(edge.wt) )
    else:
        print(str(edge.dest) + " " + str(edge.src) + " " + str(edge.wt) )
