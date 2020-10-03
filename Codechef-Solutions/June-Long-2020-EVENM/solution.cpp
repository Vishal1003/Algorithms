#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int s=0; s<t; s++){
        int m;
        cin >> m;
        int arr[m][m];
        int val=1;
        for(int i=0; i<m; i++){
            // If row number is even, fill numbers from left to right
            if(i%2 == 0){
                for (int j = 0; j < m; j++){
                    arr[i][j] = val;
                    val++;
                }
            } else {
            // If row number is odd, fill numbers from right to left
                for (int j = m-1; j >= 0; j--){
                    arr[i][j] = val;
                    val++;
                }
            }
        }
        for(int i=0; i<m; i++){
            for(int j=0; j<m; j++){
                cout << arr[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}