#include <iostream>

using namespace std;

int main()
{
    int t, n;
    cin >> t;
    for(int i=0; i<t; i++){
        cin >> n;
        int arr[n];
        int flag = 1;
        for(int j=0; j<n; j++){
            cin >> arr[j];
        }
        // initialise coins of each type to 0 since Chef has no money initially
        int fives = 0, tens = 0, fifteens = 0;
        // if first person doesn't pay Rs. 5 coin, Chef cannot sell any icecream as he has no change initially
        if(arr[0]!=5){
            flag = 0;
        }else{
            // first person pays Rs.5 coin
            fives++;
            // iterate for other people
            for(int j=1; j<n; j++){
                // if person pays Rs. 5, just add it to the balance
                if(arr[j]==5){
                    flag = 1;
                    fives++;
                // if person pays Rs. 10 and Chef has Rs. 5 coin, he can sell icecream, else break the loop
                }else if(arr[j]==10){
                    if(fives>=1){
                        flag = 1;
                        fives--;
                        tens++;
                    }else{
                        flag = 0;
                        break;
                    }
                // if person pays Rs. 15 and Chef has Rs. 10 balance, he can sell icecream, else break the loop
                // if Rs. 10 coin is available, that will be exchanged (higher priority)
                // else if two Rs. 5 coins are available, those will be exchanged
                }else if(arr[j]==15){
                    if(tens>=1){
                        flag=1;
                        tens--;
                        fifteens++;
                    }else if(fives>=2){
                        flag=1;
                        fifteens++;
                        fives = fives-2;
                    }else{
                        flag=0;
                        break;
                    }
                }
            }
        }
        if(flag == 0){
            cout << "NO" <<endl;
        }else{
            cout << "YES" <<endl;
        }
    }
}