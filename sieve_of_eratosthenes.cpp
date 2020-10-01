#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int s;
vector<bool> sieve(1000000,0);

void Sieve(int S){
    sieve[0] = 1;
    sieve[1] = 1;
	for(int i = 2;i < sqrt(S);i++){
		for(int j = i+i;j < S;j += i){
			sieve[j] = 1;
		}
	}
}

int main(){
	cout<<"Choose sieve size\n";
	cin>>s;
	Sieve(s);
	cout<<"Primes in that range are\n";
	for(int i = 0;i < s;i++){
		if(sieve[i] == 0){
			cout<<i<<" ";
		}
	}
}
