# Given an integer n, return the number of prime numbers that are strictly less than n.
# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


from math import isqrt


def sieve(n):
    if n < 2:
        return 0
    prime = [True] * n
    prime[0] = False
    prime[1] = False

    for i in range(isqrt(n)+1):
        if prime[i]:
            for x in range(i*i, n, i):
                prime[x] = False

    # return [i for i in range(n) if prime[i]]
    return sum(prime)


print(sieve(int(input())))
