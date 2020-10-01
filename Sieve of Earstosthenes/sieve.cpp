// Check prime number upto MAX
#include <bits/stdc++.h>
#define MAX 100
using namespace std;
#define vi vector<int>

void printVec(vi &arr);

void sieve(vi &primes)
{
    primes[0] = 0;
    primes[1] = 0;
    int i;
    while (i <= MAX)
    {
        if (primes[i] == 1)
        {
            int j = 2;
            while (j * i <= MAX)
            {
                primes[i * j] = 0;
                j++;
            }
        }
        i++;
    }
    printVec(primes);
}

int main()
{
    vi primes(MAX, 1);

    sieve(primes);
    int n;
    cin >> n;
    string ans = "Yes";
    if (primes[n] == 0)
        ans = "No";
    cout << ans;
    return 0;
}

void printVec(vi &arr)
{
    int index = 0;
    for (auto ele : arr)
    {
        if (ele == 1)
            cout << index << " ";
        index++;
    }
    cout << endl;
}