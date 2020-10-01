// Statement- Preffix sum to find the sum over a range of elements in O(1)
#include <bits/stdc++.h>
using namespace std;
//It works on O(n)
vector<int> buildPrefSum(vector<int> &arr){
  vector<int> prefArr(arr.size());
  prefArr[0]=arr[0];
  for(int i=1; i<(int)arr.size(); i++){
    prefArr[i]=prefArr[i-1]+arr[i];
  }
  return prefArr;
}
//It works on O(1)
int findSum(int l, int r, vector<int> &pref){
  if(l>0){
    return pref[r]-pref[l-1];
  }else{
    return pref[r];
  }
}
int main(){
   int n;
   cin>>n;
   vector<int> arr(n);
   for(int i=0; i<n; i++) cin>>arr[i];
   vector<int> prefixSumArr = buildPrefSum(arr);
   
   int q;
   cin>>q;
   while(q--){
    int l, r;
    cin>>l>>r;
    cout<<findSum(l, r, prefixSumArr)<<"\n";
   }
   return 0;
}
/*Sample
-----------------
Input 
7 -> Length of the array
2 3 8 -5 8 1 36 -> Array
4 -> No of quarries
For each of the quaries enter the l and r for each segment
1 3
4 6
0 4 
2 2
----------------
Output
6
45
16
8
*/
