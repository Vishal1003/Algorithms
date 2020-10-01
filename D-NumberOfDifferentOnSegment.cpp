#include <bits/stdc++.h>
#define pc putchar
#define gc getchar
#define gcu getchar_unlocked
#define fi first
#define se second
#define pb push_back
#define mod ((ll)1e9 + 7)
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
//===============================================================================================
 
int n, m, base = 1;
int a[300009][49], ans[49];
void obliczans(int v, int l, int r, int x, int y);
 
//===============================================================================================
int main()
{
    scanf("%d %d", &n, &m);
    while (base < n)
        base <<= 1;
    for (int i = 0, temp; i < n; i++)
    {
        scanf("%d", &temp);
        a[base + i][temp]++;
    }
    for (int i = base - 1; i; i--)
        for (int j = 1; j <= 40; j++)
            a[i][j] = a[i * 2][j] + a[i * 2 + 1][j];
    for (int i = 0, tempa, tempb, tempc; i < m; i++)
    {
        scanf("%d %d %d", &tempa, &tempb, &tempc);
        if (tempa == 1)
        {
            memset(ans, 0, sizeof ans);
            obliczans(1, 0, base - 1, tempb - 1, tempc - 1);
            tempa = 0;
            for (int j = 1; j <= 40; j++)
                if (ans[j])
                    tempa++;
            printf("%d\n", tempa);
        }
        else
        {
            tempb += base - 1;
            memset(a[tempb], 0, sizeof a[tempb]);
            a[tempb][tempc]++;
            tempb >>= 1;
            while (tempb)
            {
                for (int j = 1; j <= 40; j++)
                    a[tempb][j] = a[tempb * 2][j] + a[tempb * 2 + 1][j];
                tempb >>= 1;
            }
        }
    }
}
//===============================================================================================
void obliczans(int v, int l, int r, int x, int y)
{
    if (l > y || r < x)
        return;
    if (l >= x && r <= y)
    {
        for (int i = 1; i <= 40; i++)
            if (a[v][i])
                ans[i] = 1;
        return;
    }
    obliczans(v * 2, l, (l + r) / 2, x, y);
    obliczans(v * 2 + 1, (l + r) / 2 + 1, r, x, y);
}