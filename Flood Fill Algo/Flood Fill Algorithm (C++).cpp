// Flood fill algorithm in C++ using Queue

#include <bits/stdc++.h>
using namespace std;

void checkAndPush(int x,int y, int r,  int c, int prevC, int newC, queue<pair<int,int>>&q, vector<vector<int>> &screen)
{
    if(x<0 || y<0 || x>=r || y>=c || screen[x][y]!=prevC)
        return;
    
    screen[x][y]=newC;
    q.push(make_pair(x,y));
    return;
}

//Driver code
int main() {
    int r,c,i,j,x,y,prevC,newC;
    queue<pair<int,int>>q;
    pair<int, int> cur;
    
    cin>>r>>c;
    vector<vector<int>> screen(r) ;
    
  //input the screen array
	for(i=0;i<r;i++)
	{
	    vector<int>row(c);
	    for(j=0;j<c;j++)
	        cin>>row[j];
	    screen[i]=row;
	}
	
	cin>>x>>y;
	prevC=screen[x][y];
	
	cin>>newC;
    
  //push first position pair to queue
  checkAndPush(x,y,r,c,prevC,newC,q,screen);

  while(!q.empty())
  {
      cur=q.front();
      q.pop();
      x=cur.first;
      y=cur.second;

      //fill adjacent cells
      checkAndPush(x-1,y,r,c,prevC,newC,q,screen);
      checkAndPush(x+1,y,r,c,prevC,newC,q,screen);
      checkAndPush(x,y-1,r,c,prevC,newC,q,screen);
      checkAndPush(x,y+1,r,c,prevC,newC,q,screen);
  }
  cout<<"Updated screen after call to floodFill: \n"; 
  for (i = 0; i < r; i++) 
  { 
      for (j = 0; j < c; j++) 
          cout<<screen[i][j]<<" "; 
      cout<<endl; 
  } 
	return 0;
}
