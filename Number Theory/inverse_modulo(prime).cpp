// calculate inverse modulo with respect to a prime number
// using fermat's theorem for a prime number m:  x inversemod m is xpower(m-1)

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

ll inverse_mod(ll x, ll y){
  return power(x,y-1);
}


int main(void)
{
  ll x;cin>>x;
  ll y;cin>>y;
  
  if(x%y==0) cout<<"does not exist"<<endl;
  else  cout<<inverse_mod(x,y)<<endl;

  return 0;
 }

