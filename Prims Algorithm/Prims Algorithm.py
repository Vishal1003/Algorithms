#prims algorithm
import sys

class Graph:
    def __init__(self,vertices):
        self.vert=vertices
        self.AM=[[0 for i in range(self.vert)]for j in range(self.vert)]
    def addEdge(self,v1,v2,wt):
        self.AM[v1][v2]=wt
        self.AM[v2][v1]=wt
        
    def getMinVertex(self,visited,weight):
        minVertex=-1
        for i in range(self.vert):
            if visited[i]==False and (minVertex==-1 or weight[minVertex]>weight[i]):
                minVertex=i
        return minVertex
    
    def prims(self):
        visited=[False for i in range(self.vert)]
        parent=[-1 for i in range(self.vert)]
        weight=[sys.maxsize for i in range(self.vert)]
        weight[0]=0
        for i in range(self.vert-1):
            minVertex=self.getMinVertex(visited,weight)
            visited[minVertex]=True
            for j in range(self.vert):
                if visited[j]==False and self.AM[minVertex][j]>0:
                    if weight[j]>self.AM[minVertex][j]:
                        weight[j]=self.AM[minVertex][j]
                        parent[j]=minVertex
        for i in range(1,self.vert):
            if i<parent[i]:
                print(str(i)+' '+str(parent[i])+' '+str(weight[i]))
            else:
                print(str(parent[i])+' '+str(i)+' '+str(weight[i]))
    
li=[int(i) for i in input().split()]
n=li[0]
e=li[1]
g=Graph(n)
for i in range(e):
    cur=[int(i) for i in input().split()]
    g.addEdge(cur[0],cur[1],cur[2])
g.prims()