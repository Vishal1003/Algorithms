#include<iostream>
#include<cstdio>

#define MAXINT 65356

using namespace std;

int main()
{
    // input a graph where n indicate no. od vertices edges- no. of edges;
    int n,edges;

    cout<<"Enter no. of vertices ";
    cin>>n;

    cout<<"Enter no. of edges ";
    cin>>edges;

    int x,y,w; // x,y vertex of edge , w- weight of edge.

    int** graph=new int*[n]; // stores graph.

    for(int i=0;i<n;i++)
    graph[i]=new int[n];

    for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)
    graph[i][j]=0;

    for(int i=1;i<=edges;i++)
    {
            cin>>x>>y>>w;

            graph[x-1][y-1]=w;
    }

    int v; //starting vertex;

    cout<<"Enter starting vertex ";
    cin>>v;

    int* dist=new int[n];      // distance keeps account the distance to reach non tree vertex from tree vertex.
    int* parent=new int[n];   // keeps track of parent of each vertex.
    bool* intree=new bool[n]; // keeps track which vertex is a tree vertex or non tree vertex.

    for(int i=1;i<=n;i++)
    {
            dist[i-1]=MAXINT;
            parent[i-1]=-1;
            intree[i-1]=false;
    }

    dist[v-1]=0; // starting vertex distance will always be zero.

    // algorithm to construct tree each time will add one edge to while loop.

    while(!intree[v-1])
    {
                       int i=v-1;
                     intree[i]=true;

                     for(int j=0;j<n;j++)
                     {
                             if(graph[i][j]!=0)
                             {
                                               if(!intree[j] && dist[j]>graph[i][j])
                                               {
                                                             dist[j]=graph[i][j];
                                                             parent[j]=i;
                                               }
                             }
                     }

                     // to find which is the non tree vertex with minimum distance from the tree

                     v=1;
                     int d=MAXINT;

                     for(int i=0;i<n;i++)
                     {
                             if(dist[i]<d && !intree[i])
                             {
                                          d=dist[i];
                                          v=i+1;
                             }
                     }

    }

    system ("pause");

    return 0; 
}
