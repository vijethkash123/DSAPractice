'''
Checking till sqrt(n) is enough to check if a number is prime or not
Explanation:

If a number n is not a prime, it can be factored into two factors a and b:
n = a * b
Now a and b can't be both greater than the square root of n, 
since then the product a * b would be greater than sqrt(n) * sqrt(n) = n.
So in any factorization of n, at least one of the factors must be less than or equal 
to the square root of n, and if we can't find any factors less than or equal to the square root, 
n must be a prime.
'''

import math
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(isPrime(13))
print(isPrime(12))
print(isPrime(9))
print(isPrime(23))


"""
To generate prime numbers from 1 to n. Note: else in for else is only executed when the break is `not` encountered.
"""
def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            primes.append(num)
    return primes

# Get user input
n = int(input("Enter the upper limit for prime numbers: "))

# Generate and print prime numbers
prime_numbers = generate_primes(n)
print(f"Prime numbers between 2 and {n} are:")
print(prime_numbers)
