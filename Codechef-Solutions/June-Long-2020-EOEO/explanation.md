## PROBLEM LINK
[https://www.codechef.com/JUNE20B/problems/EOEO](https://www.codechef.com/JUNE20B/problems/EOEO)

## EXPLANATION
* We have to find the number of ways how Jerry can win the game.
* Jerry will win only if JS has greater number of 2's in the prime factorisation of JS than that of TS. (ie. JS can be divided by 2 greater number of times)
* For finding the number of 2's in the prime factorisation of TS, we can count the number of trailing zeros in the binary form of TS.
* For Jerry to win, JS should have a minimum of these many trailing zeros + 1.
* So we can remove all such trailing zeros and the first 1, and the resultant number will give the number of ways Jerry can win.
### EXAMPLE 1:
TS = 11 => TS = 1011 in binary
Number of trailing zero = 0
Removing all trailing zero and first '1', resultant number = 101 which is 5 in decimal.
### Hence, answer = 5

### EXAMPLE 2:
TS = 10 => TS = 1010 in binary
Number of trailing zero = 1
Removing all trailing zero and first '1', resultant number = 10 which is 2 in decimal.
### Hence, answer = 2

### EXAMPLE 3:
TS = 100 => TS = 1100100 in binary
Number of trailing zero = 2
Removing all trailing zero and first '1', resultant number = 1100 which is 12 in decimal.
### Hence, answer = 12