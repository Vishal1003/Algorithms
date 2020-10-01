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
// Returns the Inverse Modulo of the Number
long long int inv_mod(long long int a){
    return fastexp(a,mod-2);
}
void preprocess(vector<long long int>&arr,long long int n){
    arr.push_back(1);
    for(int i=1;i<=n;i++){
        arr.push_back((arr[i-1]*i)%mod);
    }
}
long long int nCr(long long int n,long long int r,vector<long long int>&arr){
    // if the preprocessing array is empty then we need to fill it factorial(i) for i in [0,10]
    if(arr.empty())preprocess(arr,n);
    if(r==0||r==n)return 1;
    //Calulate the modular inverse of r!(n-r)!
    long long int temp=(arr[r]*arr[n-r])%mod;
    temp=inv_mod(temp);
    //return the answer as product of n! and modular inverse of denominator.
    return (arr[n]*temp)%mod;
}
int main(){
    vector<long long int>arr;
    long long int n=10;
    for(int i=0;i<=n;i++){
        cout<<nCr(n,i,arr)<<" ";
    }
    cout<<endl;
}