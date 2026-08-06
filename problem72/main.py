# for a specific denominator we want just the numerators that are co prime to the denominator
# for d = 8, possible n = 1,3,5,7 
# eulers totient function phi(n) returns the number of such numerators
# hence we can use it for this question

# but since the limit is till a million we use a sieve like we did for sieve of Erastosthenes

# we know for primes phi(p) = p - 1 but here since we also include 1 cuz its co prime with all we make it phi(p) = p


def TotientSieveSum(limit: int):
    phi = (limit + 1) * [0]
    for i in range(1, limit + 1): # limit + 1 to be inclusive of the million
        phi[i] = i # assuming all are primes initially

    for i in range(2, limit + 1):
        # when i is a composite (non-prime) number, the inner for loop doesn't run at all, cuz its phi value has been overwritten in previous iterations
        if phi[i] == i: # meaning i is a prime
            for multiples in range(i, limit + 1, i): # calculates phi of all multiples of the prime
                phi[multiples] = (phi[multiples] // i) * (i - 1)

    total = 0
    for i in range(2, limit + 1): # since in (n/d) n < d, we exclude 1 and start from 2
        total += phi[i]

    return total

MILLION = 1000000

def main():
    print(TotientSieveSum(limit=MILLION))

main()