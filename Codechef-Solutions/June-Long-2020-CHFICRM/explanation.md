## PROBLEM LINK
[https://www.codechef.com/JUNE20B/problems/CHFICRM](https://www.codechef.com/JUNE20B/problems/CHFICRM)

## EXPLANATION
### CONDITIONS
* Only Rs 5,10 and 15 coins are available.
* Initially Chef has no money.
* Chef won't skip any person without selling icecream to him.
### EXPLANATION:
* Initialise 3 variables fives, tens, fifteens to zero (Since Chef has no money initially)
* These variables will keep a count of the number of coins of each type available with Chef after each sale.
* If the first person doesn't give a Rs. 5 coin, Chef can't sell icecream to anyone. In that case, print NO directly and return.
* In other cases, iterate for all persons
* If a person gives a Rs.5 coin, increment "fives" by 1 and continue.
* If a person gives a Rs. 10 coin, there are two cases:
    * If Chef has Rs. 5 coin, transaction is possible. Increment "tens" by 1 and decrement "fives" by 1.
    * Else transaction is not possible. Break the loop.
* If a person gives a Rs. 15 coin, there are three cases:
    * If Chef has Rs. 10 coin, transaction is possible. Increment "fifteens" by 1 and decrement "tens" by 1.
    * Else if Chef has 2 Rs. 5 coins, transaction is possible. Increment "fifteens" by 1 and decrement "fives" by 2.
    * Else transaction is not possible. Break the loop.
> During a transaction of Rs. 15, if Rs. 10 coin is available, it will be used for the transaction before using Rs. 5 coin. This is because Rs. 5 coin can also be used for exchanging with Rs. 10 coin. This is a greedy approach and it always works!