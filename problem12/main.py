def primeFactorsOf(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return factors

def triangularNumber(n):
    return (n*(n+1))/2

# n = int(input("n: "))
for i in range(999999):
    trn = triangularNumber(i)
    if len(primeFactorsOf(trn)) >= 500:
        print(trn, i)
        break
