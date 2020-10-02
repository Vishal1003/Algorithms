/*
QUESTION:
Maximum divisors in a Range
-----------------------------
You are given two integers a and b. After that, you will be given q queries each of which contains
two integers low and high. Let’s define S as the set of common divisors of a and b which lie in the range
low to high i.e. low=d=high. Find the maximum element in this set S or report -1 if no such element is possible.



INPUT:
First line contains two integers a and b.
q lines follow: Each line contains 2 space separated integers denoting low and high


OUTPUT:
Output q lines. Each line denotes maximum divisor which lies in range 
[low,high]. Report -1 if no such divisor exists.	


Constraints:
1<=q<=10^5
0<=low,high,a,b<=10^9


EXAMPLE:
input
8 12
4
2 10
3 7
2 2 
5 6
output
4
4
2
-1

Sample Test Case Explanation
For a=8 and b=12, common divisors are [1,2,4].
1. Between [2,10] and [3,7] maximum common divisor is 4.
2. Between [2,2] maximum common divisor is 2.
3. Between [5,6] there is no common divisor, so -1.
*/


//SOLUTION:

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
