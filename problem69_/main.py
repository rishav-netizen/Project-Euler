def gcd(n: int, m: int) -> int: # assuming no negative input
    if 0 in {m, n}:
        return max(m, n)

    maximum = max(m, n)
    minimum = min(m, n)

    if maximum % minimum == 0:
        return minimum
    
    return gcd(minimum, maximum % minimum)

def relativePrime(a: int, b: int) -> bool:
    return gcd(a, b) == 1

def primesTill(limit: int) -> set:
    if limit <= 1:
        return set()
    
    isPrime = (limit + 1) * [True]
    isPrime[0] = isPrime[1] = False

    primes = set()

    for a in range(2, int(limit**0.5) + 1):
        if isPrime[a]:
            for multiple in range(a**2, limit + 1, a):
                isPrime[multiple] = False

    for i in range(2, limit + 1):
        if isPrime[i]:
            primes.add(i)
    
    return primes


def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if (n % 2 == 0):
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def phi(n: int) -> int:
    count = 1 # because 1 is already relative prime to all 
    for i in range(2, n):
        if relativePrime(i, n):
            count += 1
    
    return count

MILLION = 1000000
LIMIT = 100
def test():
    primes = {3, 5, 7, 11}
    composites = {4, 6, 8, 9}
    nums = [30, 210]
    for j in nums:
        phi_n = phi(j)
        n = j
        ratio = phi_n/n
        print(f"ϕ({n}) = {phi_n} ; Ratio = {ratio}")
    print()

def bruteForce():
    max_ratio = 0
    max_ratio_i = 0
    for i in range(11, MILLION + 1):
        ratio = i/phi(i)
        if ratio > max_ratio:
            max_ratio = ratio
            max_ratio_i = i

    print(max_ratio_i)

def main():

    # using hella observations and stuff like that we understand that
    # adding distinct prime factors increases n/ϕ(n) ratio
    # ϕ(p) = p - 1 where p is a prime

    primeSet = sorted(primesTill(LIMIT)) # just product of primes from 2 to 17 
    number = 1

    for prime in primeSet:
        if number*prime <= MILLION:
            number *= prime
        else:
            break
    
    print(number)


if __name__ == "__main__":
    main()