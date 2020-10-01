//Implementation of Strassens Matrix Multiplication in C++
//Written by PeeyushKumar

#include <iostream>
using namespace std;


int ** get_matrix(int row, int col)
{
    int ** matrix = new int * [row];

    for (int i=0; i<row; i++)
        matrix[i] = new int [col];
    
    cout<<"Enter the matrix (" << row << 'x' << col << "):" <<endl;
    for (int i=0; i<row; i++)
        for (int j=0; j<col; j++)
            cin>>matrix[i][j];
    cout<<endl;

    return matrix;
}


void print_matrix(int **matrix, int row, int col)
{
    for (int i=0; i<row; i++)
    {
        for (int j=0; j<col; j++)
            cout << matrix[i][j] << ' ';
        cout << endl;
    }
    cout << endl;
}

int main()
{
    int ** A = get_matrix(2, 2);
    int ** B = get_matrix(2, 2);
 
    int C[4];
    int P[7];

    P[0] = (A[0][0]+A[1][1]) * (B[0][0] + B[1][1]);
    P[1] = (A[1][0]+A[1][1]) * B[0][0];
    P[2] = A[0][0] * (B[0][1] - B[1][1]);
    P[3] = A[1][1] * (B[1][0] - B[0][0]);
    P[4] = (A[0][0]+A[0][1]) * B[1][1];
    P[5] = (A[1][0]-A[0][0]) * (B[0][0] + B[0][1]);
    P[6] = (A[0][1]-A[1][1]) * (B[1][0] + B[1][1]);

    C[0] = P[0] + P[3] - P[4] + P[6];
    C[1] = P[2] + P[4];
    C[2] = P[1] + P[3];
    C[3] = P[0] + P[2] - P[1] + P[5];

    cout<<"\n"<<C[0]<<' '<<C[1]<<'\n'<<C[2]<<' '<<C[3]<<"\n";

    return 0;
}
