// Author: rishab_1128
//Cycle Detection in a Directed Graph using DFS

#include<bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"
#define SIZE 100001
const int MOD  = 1000000007;

vector<int>adj[SIZE];
bool vis[SIZE];
bool rec[SIZE];

bool dfs_detect_cycle(int node)
{
	if(!vis[node])
	{
        //Mark the current node as visited and part of recursion stack 
		vis[node]=1;
		rec[node]=1;
        //Recur for all the vertices adjacent to this vertex 
		for(int child: adj[node])
		{
			if(!vis[child]&&dfs_detect_cycle(child))
				return true;
			else if(rec[child])
				return true;
		}
	}
	rec[node]=0; // remove the vertex from recursion stack 
	return false;
}

void solve()
{
	//Creating the adjacency list
	adj[1].push_back(2);
    adj[1].push_back(3);
    adj[2].push_back(3);
    adj[3].push_back(1);
    adj[4].push_back(4);

    // Mark all the vertices as not visited and not part of recursion stack 
	memset(vis,0,sizeof(vis));
	memset(rec,0,sizeof(rec));

	for(int i=1; i<=4; i++)
	{
		if(!vis[i])
		{
            //Call the recursive function to detect cycle in different DFS trees
			int flag=dfs_detect_cycle(i);
			if(flag)
			{
				cout<<"CYCLE DETECTED"<<endl;
				return;
			}
			else
			{
				cout<<"NO CYCLE DETECTED"<<endl;
				return;
			}
		}
	}
}

int32_t main()
{
    /*std::ios::sync_with_stdio(false);
     #ifndef ONLINE_JUDGE
       freopen("input.txt","r",stdin);
       freopen("output.txt","w",stdout);
    #endif*/

	int t=1;
	//cin>>t;
	while(t--)
	{
		solve();
	}

	return 0;
}