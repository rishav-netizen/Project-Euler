MILLION = 1000000

def primes_less_than(n: int) -> set[int]: # Sieve of Eratosthenes
    if n < 2:
        return set()

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for a in range(2, int(n**0.5) + 1):
        if is_prime[a]:
            for multiples in range(a**2, n + 1, a):
                is_prime[multiples] = False

    primes = set()
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.add(i)

    return primes

def isCircularPrime(n: int) -> bool:
    number = str(n)
    length = len(number)

    if length >= 2:
        if any(digits in number for digits in "024685"):
            return False
    
    for i in range(length):
        number = number[1:] + number[0] #trying every combination of a number by string slicing
        if int(number) not in primes:
            return False
        
    return True

primes = primes_less_than(MILLION)
count = 0
for i in range(2, MILLION):
    if isCircularPrime(i):
        count += 1
        print(i)

print("Count: ", count)
# print(any({0, 0, 0}))


