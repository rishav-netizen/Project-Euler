def prime_seive(n: int) -> list:
    if n <= 1:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for a in range(2, int(n ** 0.5) + 1):
        if is_prime[a]:
            for multiples in range(a**2, n + 1, a):
                is_prime[multiples] = False

    primes = []
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return (primes)

def isPrime(n):
    return n in prime_set


def main():
    max_len = 0
    running_sum = 0

    for p in primes:
        running_sum += p
        if running_sum > MILLION:
            break
        max_len += 1

    l = len(primes)
    k = 0
    total = 0
    for k in range(max_len, 1, -1):
        current_sum = sum(primes[:k])

        for i in range(l - k + 1):

            if current_sum < MILLION and isPrime(current_sum):
                return current_sum

            if i < l - k:
                current_sum += primes[i+k] - primes[i]

            if current_sum > MILLION: 
                break




from time import perf_counter

start = perf_counter()

MILLION = 1000000
primes = prime_seive(MILLION)
prime_set = set(primes)

answer = main()
end = perf_counter()
print(answer)
print(f"{(end - start) * 1000:.6f} ms")