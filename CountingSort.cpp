#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void Print(vector<int> &arr){
    
    for(int i=0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }
    
    cout<<endl;
}

void CountingSort(vector<int> &A, vector<int> &Aux, vector<int> &sorted) {

    int N=A.size();
    // First, find the maximum value in A[]
    int K = 0;
    for(int i=0; i<N; i++) {
        K = max(K, A[i]);
    }
    
    // Initialize the elements of Aux[] with 0
    for(int i=0 ; i<=K; i++) {
        Aux[i] = 0;
    }

    // Store the frequencies of each distinct element of A[],
    // by mapping its value as the index of Aux[] array
    for(int i=0; i<N; i++) {
        Aux[A[i]]++;
    }

    int j = 0;
    for(int i=0; i<=K; i++) {
        int tmp = Aux[i];
        // Aux stores which element occurs how many times,
        // Add i in sortedA[] according to the number of times i occured in A[]
        while(tmp--) {
            //cout << Aux[i] << endl;
            sorted[j] = i;
            j++;
        }
    }
}

int main()
{
    vector<int> A{5,2,9,5,2,3,5};
    vector<int> Aux{0,0,2,1,0,3,0,0,0,2};  //Aux stores count of element 'i' in 'A'
    vector<int> sorted(A.size());
    
    CountingSort(A,Aux,sorted);
    Print(sorted);
    
    return 0;
}
