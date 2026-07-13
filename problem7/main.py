def isPrime(n):
    if n<=1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def NthPrime(n):
    count = 0;
    for i in range(2, 100000000000):
        if isPrime(i):
            count+=1
        if count == n:
            return i

print(NthPrime(10001))