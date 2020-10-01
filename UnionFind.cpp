#include<iostream>
using namespace std;

class UnionFind
{
private:
	int n, *parent, *rank;
public:
	UnionFind(int n)
	{
		this->n = n;
		rank = new int[n+1];
		parent = new int[n+1];
		for(int i=1; i<=n; i++)
		{
			parent[i] = i;
			rank[i] = 1;
		}
	}
	int Find(int i)
	{
		if(parent[i] == i)
			return i;
		else
			return parent[i] = Find(parent[i]);
	}
	void Union(int a, int b)
	{
		if(Find(a) == Find(b))
			return;
		int i = Find(a);
		int j = Find(b);
		if(rank[i] < rank[j])
			swap(i,j);
		if(rank[i] == rank[j])
			rank[i]++;
		parent[j] = i;
	}
};

int main()
{
	int n = 6;
	UnionFind a(n);
	a.Union(1,2);
	a.Union(3,4);
	a.Union(2,3);
	cout<<"parent of"<<4<<" "<<a.Find(4)<<"\n";// 1
	cout<<"parent of"<<5<<" "<<a.Find(5)<<"\n";// 5
	return 0;
}