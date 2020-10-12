#include <bits/stdc++.h>
using namespace std;

int fun(vector<int>& height){
    int n=height.size();
        if(n==0) return 0;
        stack<int> s;
        int top,distance,length;
        int curr=0;
        int ans=0;
        while(curr<n){
            while(!s.empty() && height[curr]>height[s.top()]){
                top=s.top();
                s.pop();
                if(s.empty())
                    break;
                distance=curr-s.top()-1;
                length=((height[curr]<height[s.top()])?height[curr]:height[s.top()])-height[top];
                ans+=distance*length;
            }
            s.push(curr);
            curr++;
        }
        return ans;
}

int main() {
	vector<int> v({0,1,0,2,1,0,1,3,2,1,2,1});
	cout<<"The amount of trapped rainwater is "<<fun(v);
	return 0;
}