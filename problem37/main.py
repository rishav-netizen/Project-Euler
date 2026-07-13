def primes_till(n: int) -> set[int]:
    if n <= 1:
        return set()
    
    # assume all are primes initially 
    is_prime = (n + 1) * [True]

    # since 0 and 1 are not primes we set them to false
    is_prime[0] = is_prime[1] = False

    # our set where all the primes would go
    primes = set()

    for a in range(2, int(n**0.5) + 1):
        if is_prime[a]:
    # we check from a^2 because like the numbers' earlier multiples are already marked during the previous iterations of the loop when the value of a was smaller
            for multiples in range(a**2, n + 1, a):
                is_prime[multiples] = False
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.add(i)

    return primes
    
    
def isTruncable(n: int) -> bool:
    strNum = str(n)
    length = len(strNum)
    if length < 2:
        return False
    for i in range(length):
        # print(strNum[:i+1])
        # print(strNum[i:])
        if int(strNum[:i+1]) not in primeSet:
            return False
        elif int(strNum[i:]) not in primeSet:
            return False
    return True


def main():
    result = count = 0
    for i in primeSet:
        if i < 10:
            continue

        str_i = str(i)
        #? because the first digit can be 2 or 5
        if not (any(digits in str_i[1:] for digits in "024685") or any(digits in str_i for digits in "0468")):
            if isTruncable(i):
                result += i
                count += 1
                print(i)
                
    print("Sum of truncable primes:", result, "\nCount:", count)

MILLION = 1000000
primeSet = primes_till(100*MILLION)

if __name__ == "__main__":
    main()