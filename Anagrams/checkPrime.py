primes = [3,5,7,11,13,17,19]

# 1 is excluded since 1 is identity element for multiplication and division
# 2 is the smallest prime number since it is only divisible by 1 and 2
numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def checkPrime(n):
    is_prime = False # we have not found i that divides n
    factor_found = 1 # 1 is a factor of all numbers since 1 * n = n
    for i in range(2, n):
        # if n divided by i has no remainder, then i is a factor of n
        # prime numbers have no factors other than 1 and itself
        remainder = n % i
        if remainder == 0:
            is_prime = True
            factor_found = i # store the factor that divides n for printing
            break # exit loop since we found a factor
    if is_prime:
        print(f'Since {n} is divisible by {factor_found}, {n} is not a prime number.')
    else:
        print(f'Since {n} is not divisible by any integer between 2:{n-1}, {n} is a prime number.')

for number in numbers:
    checkPrime(number)

for prime in primes:
    checkPrime(prime)

# Improved version of checkPrime using square root of n
# Since all factors of n are less than or equal to sqrt(n), we can reduce the number of iterations
# https://sites.pitt.edu/~bonidie/cs441/primes.pdf (page 4)
from math import sqrt
def improved_checkPrime(n):
    is_prime = False # we have not found i that divides n
    factor_found = 1 # 1 is a factor of all numbers since 1 * n = n
    for i in range(2, int(sqrt(n)) + 1):
        # if n divided by i has no remainder, then i is a factor of n
        # prime numbers have no factors other than 1 and itself
        remainder = n % i
        if remainder == 0:
            is_prime = True
            factor_found = i # store the factor that divides n for printing
            break # exit loop since we found a factor
    if is_prime:
        print(f'Since {n} is divisible by {factor_found}, {n} is not a prime number.')
    else:
        print(f'Since {n} is not divisible by any integer between 2:{n-1}, {n} is a prime number.')

for number in numbers:
    improved_checkPrime(number)

for prime in primes:
    improved_checkPrime(prime)