#include<bits/stdc++.h>
using namespace std;

int gcd(int a,int b){ //function for finding Greatest Common Divisor
    if(b==0)
        return a;
    gcd(b,a%b);
}

void find_divisor(int arr[],int n){ //function for finding divisor
    for(int i=1;i<=n;i++){
        if(n%i==0){
            arr[i-1] = i;
        }
    }
    sort(arr,arr+n);
    reverse(arr,arr+n);
}

int find_max_divisor(int arr[],int n,int i,int low,int high){
    //loop for finding maximum divisor
    //the array arr[] was reversed in the find_divisor(int,int) function
    for(int i=0;i<n;i++){
        if(arr[i]!=0){
            if(arr[i]>=low && arr[i]<=high)
                return arr[i];
        }
        else
            break;
    }
    return -1;

}

int main(){
    int a,b,q,low,high;
    cin>>a>>b;
    cin>>q;
    //finding gcd
    int n = gcd(a,b);

    //taking array to store the divisors
    int arr[n] = {0};

    //function for finding divisors of the gcd
    find_divisor(arr,n);

    while(q--){
        cin>>low>>high;
        //finding the maximum divisor
        int res = find_max_divisor(arr,n,0,low,high);
        cout<<res<<endl;
    }
    return 0;
}
