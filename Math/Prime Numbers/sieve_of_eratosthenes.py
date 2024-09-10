def sieve_of_eratosthenes(n):
    """Generate all prime numbers less than n using the Sieve of Eratosthenes."""
    is_prime = [True] * n
    p = 2
    while (p * p < n):
        if is_prime[p] == True:
            for i in range(p * 2, n, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n) if is_prime[p]]

print(sieve_of_eratosthenes(10))

