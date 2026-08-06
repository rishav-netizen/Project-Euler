# for a specific denominator we want just the numerators that are co prime to the denominator
# for d = 8, possible n = 1,3,5,7 
# eulers totient function phi(n) returns the number of such numerators
# hence we can use it for this question

# but since the limit is till a million we use a sieve like we did for sieve of Erastosthenes

# we know for primes phi(p) = p - 1 but here since we also include 1 cuz its co prime with all we make it phi(p) = p


def TotientSieveSum(limit: int):
    phi = (limit + 1) * [0]
    for i in range(1, limit + 1):
        phi[i] = i # assuming all are primes initially

    for i in range(2, limit + 1):
        if phi[i] == i: # meaning i is a prime
            for multiples in range(i, limit + 1, i):
                phi[multiples] = (phi[multiples] // i) * (i - 1)

    total = 0
    for i in range(2, limit + 1):
        total += phi[i]

    return total

MILLION = 1000000

def main():
    print(TotientSieveSum(limit=MILLION))

main()