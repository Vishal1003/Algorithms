#include <bits/stdc++.h>
using namespace std;

//Majority element is the element which appears more than n/2 times in an array,
//where n is the size of the array.

//Function to calculate the majority element
int fun(vector<int> v){
    //Variable 'ele' to store the majority element 
    int ele=v[0];
    int k=1;
    for(int i=1;i<v.size();i++){
        if(v[i]==ele)
            k++;
        else 
            k--;
        if(k==0){
            ele=v[i];
            k=1;
        }
    }
    return ele;
}

int main() {
	vector<int> v({3,2,4,3,3,3});
	int ans=fun(v);
	int k=0;
	for(int i=0;i<v.size();i++){
	    if(v[i]==ans)
	        k++;
	}
	if(k>v.size()/2)
	    cout<<"Majority element is "<<ans;
	else
	    cout<<"No majority element";
	return 0;
}