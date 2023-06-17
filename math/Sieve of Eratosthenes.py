# Given an integer n, return the number of prime numbers that are strictly less than n.
# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

from math import isqrt


### find all prime numbers in a range

def sieve(n):
    ### 0 and 1 are prime so we can return 0
    if n < 2:
        return 0
    ### create an n sized array, initially all set to 1
    prime = [True] * n
    ### 0 and 1 are prime
    prime[0] = False
    prime[1] = False

    # Iterate from 2 to the square root of n
    for i in range(2,isqrt(n)):
        if prime[i]:
            ## go through the multiples of each iteration of i from i*i to n
            for x in range(i*i, n, i):
                prime[x] = False
    # True numbers will be prime
    return [i for i in range(n) if prime[i]]


print(sieve(int(input())))
