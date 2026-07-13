def get_primes_till(limit: int) -> set:
    if limit <= 1:
        return set()
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    primes = set()

    for a in range(2, int(limit**0.5) + 1):
        if is_prime[a]:
            for multiples in range(a**2, limit+1, a):
                is_prime[multiples] = False
    
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.add(i)

    return primes

limit = 10000
primes_set = get_primes_till(limit)
# print(sorted(primes_set))

n = 35
while n < limit:
    if n not in primes_set: # meaning n is odd composite
        # n = p + 2 * k^2
        for i in primes_set:
            if i < n:
                m = ((n - i)/2)**0.5
                if m.is_integer():
                    break
        else:
            print(n)

                    

    n += 2 # move to the nest odd number