## Check if number is prime (Sieve of Erastosthenes)

1. Create a bool primes(vector/array) of size MAX and initially assign true
2. Make a prime[0]=0 and primes[1]=0
3. for every index where primes[i]==1
4. initialize j=2
5. and count till i\*j<=MAX and make primes[i\*j]=0
6. REPEAT Step(1..5) till i<MAX
