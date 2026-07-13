def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def maxPrimeFactorOf(n):
    maximum = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if isPrime(i):
                maximum = max(maximum, i)
            if isPrime(n // i):
                maximum = max(maximum, n // i)
    return maximum

# EULER SOLUTION BEST
def largestPrimeFactor(n):
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1

    return n


n = 600851475143
# print(maxPrimeFactorOf(n))
print(largestPrimeFactor(n))

