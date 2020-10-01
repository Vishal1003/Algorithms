// power function to calculate n power m in O(log(N))
/* base case when y==0 x^0=1 
   if y!=0 then we will divide y into 3 parts i.e. y/2 , y/2 , y%2
   power function will return x^(y/2) * x^(y/2) * x^(y%2)   
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll power(ll x,ll y){
     if(y==0)return 1;             //base case

     ll temp=power(x,y/2);
     if(y%2) return temp*temp*x;   // if y is odd

     else return temp*temp;        // if y is even
}


int main(void)
{
  ll x;cin>>x;
  ll y;cin>>y;

  cout<<power(x,y)<<endl;

  return 0;
 }

