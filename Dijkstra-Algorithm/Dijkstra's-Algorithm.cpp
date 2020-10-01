// C++ implementation of Dijkstra's Algorithm

#include<bits/stdc++.h>
using namespace std;


// Get min weight vertex in  every step

int getminIndex(int *weight,bool *vis,int n)
{
    int mn = -1;
    for(int i = 0;i<n;i++)
    {
        if(!vis[i] && ((mn==-1)||(weight[mn]>weight[i])))
        {
            mn = i;
        }
    }
    return mn;
}
int main()
{

  // taking input number of vetex and edges
  int e, v;
  // eg. 4 4
  cin >> v >> e;

  // Initialize 2D adjency matrix
  int **a = new int*[v+1];

      for(int i = 0;i<=v;i++)
      {
          a[i] = new int[v+1];
          for(int j = 0;j<=v;j++)
          {
              a[i][j] = 0;
          }
      }

    for(int i = 0;i<e;i++)
    {
        // start vertex ,end vertex and corresponding weight eg.
        // 0 1 3
        // 0 3 5
        // 1 2 1
        // 2 3 8
        int f,s,w;
        cin>>f>>s>>w;
		a[f][s] = w;
        a[s][f] = w;
    }
    // store shortest distance from starting vector in dist array
    int *dist = new int[v+1];
    dist[0] = 0;
    for(int i = 1;i<v;i++)
    {
        dist[i] = INT_MAX;
    }
    bool *vis = new bool[v+1];
    for(int i  = 1;i<v;i++)
    {
       // Pick the minimum distance vertex from the set of vertices not
       // yet processed. u is always equal to src in the first iteration.
        int mnInd = getminIndex(dist,vis,v);

        vis[mnInd] = true;

        for(int j = 0;j<v;j++)
        {

            if(vis[j]==false && a[mnInd][j])
            {
               // Update dist[v] only if is not in sptSet, there is an edge from
               // mnInd to j, and total weight of path from src to  j through mnInd is
               // smaller than current value of dist[j]
                int cur = dist[mnInd] + a[mnInd][j];
               	if(dist[j]>cur)
                {
                    dist[j] = cur;
                }
            }
        }
    }
    // first output is vertex and their distance from starting vertex 0

    for(int i = 0;i<v;i++)
    {
        cout<<i<<" "<<dist[i]<<endl;
    }

    // 0 0
    // 1 3
    // 2 4
    // 3 5

  return 0;
}
