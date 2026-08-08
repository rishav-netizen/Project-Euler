def primesTill(n: int) -> list[int]:
    if (n <= 1):
        return []

    isPrime = (n + 1) * [True]
    isPrime[0] = isPrime[1] = False

    for a in range(2, int(n**0.5) + 1):
        if isPrime[a]:
            for multiples in range(a**2, n + 1, a):
                isPrime[multiples] = False

    primeSet = []
    for i in range(2, n + 1):
        if isPrime[i]:
            primeSet.append(i)

    return primeSet

LIMIT = 10000

# Dynamic programming approach (its almost like magic to me)
def main():
    primes = primesTill(LIMIT)
    ways = [0] * (LIMIT + 1)
    ways[0] = 1
    for prime in primes:
        for current_sum in range(prime, LIMIT):
            ways[current_sum] = ways[current_sum] + ways[current_sum - prime]

    for i in range(LIMIT + 1):
        if ways[i] > 5000:
            print(i)
            break


if __name__ == "__main__":
    main()
    
