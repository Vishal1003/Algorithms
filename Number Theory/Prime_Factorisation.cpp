#include<bits/stdc++.h>

using namespace std;


void primeFact(int n)
{
    for(int i=2;i*i<=n;i++)
    {
        if(n%i==0)
        {
            int cnt=0;
            while(n%i==0)
            {
                cnt++;
                n=n/i;
            }
            cout<<i<<"^"<<cnt<<"\n";
        }
    }
    if(n>1)
        cout<<n<<"^"<<"1\n";
}

int main()
{
    cout<<"Enter no. of primes to be checked : ";
    int t;
    cin>>t;
    while(t--)
    {
        cout<<"Enter the number \n";
        int n;
        cin>>n;
        primeFact(n);
    }
    return 0;
}
