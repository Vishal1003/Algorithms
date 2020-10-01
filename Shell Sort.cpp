#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back

vector<int> shellSort(vector<int>V)
{
    for(int gap = V.size() / 2; gap > 0; gap /= 2)
    {
        for(int i = gap; i < V.size(); i += 1)
        {
            int temp = V[i];

            int j;

            for(j = i; j >= gap && V[j - gap] > temp; j -= gap)
                V[j] = V[j - gap];

            V[j] = temp;
        }
    }

    return V;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin>>N; //size of array

    vector<int>V;

    for(int i = 0; i < N; i++) //taking array inputs
    {
        int inp;
        cin>>inp;
        V.pb(inp);
    }

    vector<int>res = shellSort(V);

    //final sorted array

    for(int i = 0; i < res.size(); i++)
        cout<<res[i]<<" ";
    cout<<endl;

    return 0;
} 