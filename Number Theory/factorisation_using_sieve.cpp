#include<bits/stdc++.h>

using namespace std;
int is_prime[1000001];

void sieve()
{
    int maxn=1000000;
    for(int i=2; i<=maxn; i++)
        is_prime[i]=-1;
    is_prime[1]=1;


    for(int i=2; i<=maxn; i++)
    {
        if(is_prime[i]==-1)
        {
            for(int j=i; j<=maxn; j+=i)
                if(is_prime[j]==-1)
                    is_prime[j]=i;
        }
    }
}
void factors(int n)
{
    while(n>1)
    {
        cout<<is_prime[n]<<" ";
        n=n/is_prime[n];
    }
}
int main()
{
    sieve();
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        factors(n);
    }
    return 0;

}
