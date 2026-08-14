def primesTill(n: int):
    if (n <= 1):
        return []
    
    isPrime = (n + 1) * [True]
    isPrime[0] = isPrime[1] = False

    for a in range(2, int(n**0.5) + 1):
        for multiple in range(a**2, n + 1, a):
            isPrime[multiple] = False

    primes = []

    for i in range(2, n + 1):
        if isPrime[i]:
            primes.append(i)

    return primes

LIMIT = 50000000
def main():
    # N = a^2 + b^3 + c^4 
    # a_max = 7069
    # b_max = 367
    # c_max = 83
    # print(f"{LIMIT**0.5}, {LIMIT**(1/3)}, {LIMIT**0.25}")

    primeSet = primesTill(7069)
    sums = set()
    for a in primeSet:
        for b in primeSet:
            if b <= 367:
                for c in primeSet:
                    if c <= 83: 
                        N = a**2 + b**3 + c**4
                        if N < LIMIT:
                            sums.add(N)

    print(len(sums))


if __name__ == "__main__":
    main()

    