#include<bits/stdc++.h>
using namespace std;

struct segtree {
	int size; // this stores the length of the array to the next power of 2 if it isn't a power of 2

	vector<long long> sums; // this stores the precomputed values of each segment of the array

	// in the init function we are calculating the size of the segment tree array we need to calculate.
	// for detailed explanation please see documentation
	void init(int n) {
		size = 1;
		while(size < n) {
			size *= 2;
		}
		sums.assign(2 * size, 0);
	}

	// a utility function to store the initial elements of the array in the segment tree
	long long single(long long a) {
		return a;
	}


	// utility function to merge the two nodes of a segment tree. We can change the operation
	// to perform different tasks like minimum, maximum in the segment
	long long merge(long long a, long long b) {
		return (a + b);
	}

	// building the segment tree. This takes O(N) time
	void build(vector<long long> &a, int x, int lx, int rx) {
		if(rx - lx == 1) {
			if(lx < (int)a.size()) {
				sums[x] = single(a[lx]);
			}
			return;
		}
		int m = (rx + lx) / 2;
		build(a, 2 * x + 1, lx, m);
		build(a, 2 * x + 2, m, rx);
		sums[x] = sums[2 * x + 1] + sums[2 * x + 2];
	}

	void build(vector<long long> &a) {
		build(a,0,0,size);
	}

	// setting the value at index i to v
	void set(int i, int v, int x, int lx, int rx) {
		if(rx - lx == 1) {
			sums[x] = v;
			return;
		}

		int m = (rx + lx) / 2;

		// if the index is less than the mid index of the segment, we look in the left child
		if(i < m) {
			set(i, v, 2 * x + 1, lx, m);
		}
		// else we look in the right child
		else {
			set(i, v, 2 * x + 2, m, rx);
		}
		// we merge the two childs to get the value of the parent node
		sums[x] = merge(sums[2 * x + 1] , sums[2 * x + 2]);
	}

	void set(int i, int v) {
		set(i, v, 0, 0, size);
	}

	// calculating the sum of the elements from range [l..r)
	long long sum(int l, int r, int x, int lx, int rx) {

		// if the segment tree segment is completely inside the query segment we return a neutral value so that the answer doesn't change
		if(lx >= r or l >= rx) {
			return 0;
		}

		// if the segment tree segment is completely inside the query segment we return the value at the segment node
		else if(lx >= l and rx <= r) return sums[x];

		int m = (rx + lx) / 2;

		// calculate left child
		long long s1 = sum(l, r, 2 * x + 1, lx, m);
		// calculate right child
		long long s2 = sum(l, r, 2 * x + 2, m, rx);

		// we merge the two childs to get the value of the parent node
		return merge(s1,s2);
	}

	long long sum(int l, int r) {
		return sum(l, r, 0, 0, size);
	}
};
 
int main() {

	// Let the sample input be
	/*
	Let the sample input be
	5 5
	5 4 2 3 5
	2 0 3
	1 1 1
	2 0 3
	1 3 1
	2 0 5
	
	Here n = 5, m = 5

	initial array elements = {5, 4, 2, 3, 5}

	we have two types of queries: 
	1 i v: set the element with index i to v 
	2 l r: calculate the sum of elements with indices from l to r−1 

	So here the queries are: 
	2 0 3
	1 1 1
	2 0 3
	1 3 1
	2 0 5

	After performing the queries we get the following answers: 
	11
	8
	14

	
	*/


	int n,m;
	cin >> n >> m;

	segtree st;
	// we are initialising the segment tree
	st.init(n);

	vector<long long> a(n);
	for(int i=0;i<n;i++) {
		cin >> a[i];
	}

	// building the segment tree
	st.build(a);

	// performing queries
	while(m--) {
		int op;
		cin >> op;
		// operation of type 1
		if(op == 1) {
			int i,v;
			cin >> i >> v;
			st.set(i,v);
		}

		// operation of type 2
		else {
			int l, r;
			cin >> l >> r;
			cout << st.sum(l,r) << '\n';
		}
	}
}