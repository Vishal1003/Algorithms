#include <iostream>
#include <algorithm>

using namespace std;
 
//function to display array list
void dispArray(int arr[], int size)
{
    for(int i = 0; i < size; i++)
        cout <<" "<< arr[i];
    cout<<endl;
}
 

//main code for binary search 
int main()
{
    int a[]= {10, 1, 20, 2, 30, 4};
    
    //get array length
    int arr_length = sizeof(a) / sizeof(int);
    
    //print array
    cout<<"Array elements are: ";
    dispArray(a, arr_length);
 
    //sort the array
    sort(a, a + arr_length);
    cout<<"Sorted array elements: ";
    dispArray(a, arr_length);
    
    //searching 30 in the array
    if(binary_search(a, a+ arr_length, 30))
        cout<<"Element found"<<endl;
    else
        cout<<"Element is not found"<<endl;
        
    return 0;
}
