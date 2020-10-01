#include<bits/stdc++.h>

using namespace std;

bool isPrime(int n)
{
    if(n==1)
        return false;
    for(int i=2;i*i<=n;i++)
        if(n%i==0)
        return false;
    return true;
}

int main()
{
    cout<<"Enter the number to be checked\n";
    int n;
    cin>>n;
    if(isPrime(n))
        cout<<"Prime\n";
    else
        cout<<"Not Prime\n";
    return 0;

}
