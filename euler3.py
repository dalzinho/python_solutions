'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def primes(n):
    if n <= 2:
        return []
    sieve = [True]*(n + 1)
    for x in range(3, int(n**0.5)+1, 2):
        for y in range(3, (n//x)+1, 2):
            sieve[(x*y)]=False

    return       