'''
n^2 + n + 41
produces 40 primes for consecutive int values 0 <= n <= 39

n^@ - 79n + 1601
produces 80 primes for the consecutive int values 0 <= n <= 79

considering n^2 + an + b
|a| < 1000
|b| <= 1000
find ab for which the quadratic produces the max number of primes 
by consecutive n value starting from 0

---
b = prime (odd? only even prime is 2)
1 + a = non prime ? (odd prime + odd prime = even)
1 + a + b = prime
odd prime - odd prime = even
hence a = odd, since 1 + a = even for b != 2
** when n = b, then b is common so this means n can never exceed b
'''

def isPrime(m: int) -> int:
    if m <= 1:
        return False
    
    for i in range(2, int(m**0.5) + 1):
        if m % i == 0:
            return False
    return True

max = 0 # the maximum chain length 
prod = 0 # the product ab
for b in range(41, 1001):
    if isPrime(b): 
        for a in range(-999, 1000):
            if (a % 2 != 0):
                n = 0
                while isPrime(n**2 + n*a + b):
                    n += 1
                if n > max:
                    prod = a*b
                    max = n

print(prod, max)