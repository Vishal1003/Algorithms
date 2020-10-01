Fast Modular Exponentiation
=============================
Modular exponentiation is used in public key cryptography.

It involves computing b to the power e (mod m):

c ← be (mod m)

You could brute-force this problem by multiplying b by itself e - 1 times, but it is important to have fast (efficient) algorithms for this process.

In cryptography, the numbers involved are usually very large. Without an efficient algorithm, the process would take too long.

It can clearly be seen that running time of naiive algorithm is O(n).

In this code I will provide an O(log2(n)).

Fast Exponentiation is very important and many competitve programming questions usually involve this as a sub problem.

Algorithm
-------------------------------

Fast modular exponentiation can be carried out recursively based on the fact that:
* a<sup>e</sup> = a<sup>e/2</sup> x a<sup>e/2</sup> (when e is even) and
* a<sup>e</sup> = a<sup>e - 1</sup> * a (when e is not even)

The recursive method breaks the exponentiation down into simpler and simpler computations:

1. Define function modExp(base, exponent, modulus)
2. Set base case - if exponent = 1, return 1
3. If the exponent is even, return square(func(base, exponent / 2, mod)) % mod
4. If the exponent is not even, return (base % mod) * func(base, exponent - 1, mod)

