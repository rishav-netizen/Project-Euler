def isPrime(n: int) -> int:
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    
    return True

limit = 2000000
result = 0
for i in range(1, limit):
    if isPrime(i):
        result += i

print(result)

# ! make sure to see the pdf it has crazy implementation