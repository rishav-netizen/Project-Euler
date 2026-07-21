def primes_till(limit: int) -> set:
    if limit <= 1:
        return set()
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False   

    for a in range(2, int(limit ** 0.5) + 1):
        if is_prime[a]: 
            for multiple in range(a**2, limit + 1, a):
                is_prime[multiple] = False
    
    primes = set()
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.add(i)

    return primes

def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
 
def is_valid_pair(p1: int, p2: int) -> bool:
    # p1 and p2 are taken from prime set so no need to check their primality
    comb1 = int(str(p1) + str(p2))
    if not isPrime(comb1):
        return False
    
    comb2 = int(str(p2) + str(p1))
    if not isPrime(comb2):
        return False
    else:
        return True

 
TEN_THOUSAND = 10000
HUNDRED_THOUSAND = 100000
MILLION = 1000000
primeSet = sorted(primes_till(TEN_THOUSAND))


def main():
    length = len(primeSet)
    for p in range(length):
        a = primeSet[p]
        for q in range(p + 1, length):
            b = primeSet[q]
            if is_valid_pair(a, b): # pruning
                for r in range(q + 1, length):
                    c = primeSet[r]
                    if all(is_valid_pair(c, i) for i in (a, b)):
                        for s in range(r + 1, length):
                            d = primeSet[s]
                            if all(is_valid_pair(d, j) for j in (a, b, c)):
                                for t in range(s + 1, length):
                                    e = primeSet[t]
                                    if all(is_valid_pair(e, k) for k in (a, b, c, d)):
                                        print("The five primes are:", a, b, c, d, e)
                                        print("Sum:", sum([a, b, c, d, e]))
                                        return
                                            
if __name__ == "__main__":
    main()


'''
honestly enjoyed this one a lot haha the looping optimization was fun to think of
'''