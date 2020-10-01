#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
// Returns (a^b)%mod
long long int fastexp(long long int a,long long int b){
    //base case
    if(b==0)return 1;
    //Recursive Case
    a=a%mod;
    long long int t=fastexp(a,b/2);
    // If the power is odd return t^2*a;
    if(b&1){
        t=(t*t)%mod;
        return (t*a)%mod;
    }
    // power is odd return t^2
    else{
        return (t*t)%mod;
    }
}
int main(){
    long long int a=13;
    long long int b=14;
    cout<<fastexp(a,b)<<endl;
    return 0;
}