#include<iostream>
using namespace std;

char *words[10]={"zero","one","two","three","four","five","six","seven","eight","nine"};
//char words[][6]={"zero","one","two","three","four","five","six","seven","eight","nine"};

void spelling(int n)
{
    //base case
    if(n==0)
    {
        return;
    }

    //recursive
    int digit=n%10;
    spelling(n/10);
    cout<<words[digit]<<" ";
    return;
}
int main()
{
int n;
cin>>n;
spelling(n);
}
