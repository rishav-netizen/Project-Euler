def isPandigitalPrime(n: int) -> bool:
    digits = ""
    str_n = str(n)
    length = len(str_n)
    for i in range(1, length + 1):
        digits += str(i)
    # sort the digits too cuz it returns a list, so we compare list to list
    is_pandigital = sorted(str_n) == sorted(digits)
    return is_pandigital and isPrime(n)

def isPrime(n: int) -> bool:
    if n<=1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumTill(n):
    return (n*(n+1))/2

for i in range(1, 10):
    if sumTill(i)%3==0: #cuz digits sum is divisible by 3 hence number is divisible by 3
        print(f"Non prime digit lengths: {i}")

# this tells us that the largest pandigital prime number is 7digit
# but the unit place cant be 5246
# for largest must start with 7
# options 137 2456

# 7 6 5 4 3 2 1

for i in range(7650001, 7654321 + 1):
    if isPandigitalPrime(i):
        print("Largest pandigital prime: ", end="")
        print(i)



 