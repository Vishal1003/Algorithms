#include <bits/stdc++.h> 
using namespace std;
#define     mod             1e9+7
#define     ll              long long
#define     mp              make_pair
#define     t()             int test;cin>>test;while(test--)
#define     setbits(x)      __builtin_popcountll(x)
#define     si              set<int>
#define     ii              pair<int,int>
#define     que_max         priority_queue <int>
#define     que_min         priority_queue <int, vi, greater<int>>
#define     IOS             ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define     endl            '\n'

const int N = 2e5 + 5;
int a[N];

//calculate subset sum using dynamic programming
void subsetSum(){

	int n,sum;
	cin>>n>>sum; //input the length of array and sum
	vector<int> v(n);

	for(int i=0;i<n;i++) cin>>v[i];   //input the array elements

	bool t[n+1][sum+1];  

	for(int i=0;i<=n;i++){             //initialisation of the 2D array
		for(int j=0;j<=sum;j++){
			if(i == 0) t[i][j] = false;
			if(j == 0) t[i][j] = true;
		}
	}

	for(int i=1;i<=n;i++){
		for(int j=1;j<=sum;j++){
			if(v[i-1] <= j)
				t[i][j] = t[i-1][j-v[i-1]] || t[i-1][j];
			else
				t[i][j] = t[i-1][j];
		}
	}
	cout<<t[n][sum];  
}
 
int32_t main()
 
{  
    #ifndef ONLINE_JUDGE
    	freopen("input1.txt", "r", stdin);
    	freopen("output1.txt", "w", stdout);
    #endif

    IOS;

    solve();


}
