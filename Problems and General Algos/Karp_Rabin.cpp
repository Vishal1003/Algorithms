#include<iostream>
#include<string>
using namespace std;

#define a 256 // Base for hash value = size of alphabet -> |ASCII| = 256

void search(string pat, string txt, int m)
{
    /*
    pat -> pattern
    txt -> text
    m -> size of table
    */
    int M = pat.size();
    int N = txt.size();
    int h=1;
    
    int p = 0; // Hash value for pattern
    int t = 0; // Hash value for text

    // The value of h = pow(a, M - 1)%m
    for(int i = 0; i < M - 1; i++)
        h = (h * a) % m;
    // Calculate hash value of pattern and first window of text
    for (int i = 0; i < M; i++)
    {
        p = (a * p + pat[i]) % m;
        t = (a * t + txt[i]) % m;
    }
    // Slide the pattern over text one by one 
    for(int i = 0; i < N-M; i++)
    {
        // If the hash value of current window and pattern matches
        // then check for the characters one by one
        if (p == t)
        {
            int j;
            // Check the characters
            for(j = 0; j < M; j++)
                if (txt[i+j] != pat[j])
                    break;
            // if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] 
            if (j == M)
                cout << "Pattern found at index " << i << endl;
        }
        // Calculate hash value for next window of text
        // Remove leading characcter and add trailing character
        if (i < N-M)
        {
            t = (a * (t - txt[i]*h) + txt[i+M]) % m;
            //t may be -ve, in that case add base value to it
            if (t < 0) t += m; 
        }
    }
}

int main()
{
    string txt = "GEEKS FOR GEEKS", pat = "GEEK"; 
    int m = 101; // A prime number - size of the table
    search(pat, txt, m);
    return 0;
}