#include <bits/stdc++.h>

using namespace std;
// function to determine trailing zeros in the binary form of the number
unsigned long TrailingZero(unsigned long num)
{
  unsigned long count = 0;
  while ((num & 1) == 0)
  {
      num = num >> 1;
      count++;
  }
  return count;
}
int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
        unsigned long ts;
        cin >> ts;
        // find number of trailing zeros which will give the number of times it can be divided by 2 exactly
        unsigned long trailing = TrailingZero(ts);
        // remove all trailing zeros
        for(unsigned long j=0; j<=trailing; j++){
            ts = ts>>1;
        }
        cout << ts <<endl;
    }
    return 0;
}