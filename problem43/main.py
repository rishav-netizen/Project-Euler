import itertools

def isPandigitalZeroToNine(number: int) -> bool:
    length = len(str(number))

    if length != 10:
        return False
    
    digits = ""
    for i in range(length):
        digits += str(i)

    if all(i in str(number) for i in digits):
        return True

    return False

def property(number: int) -> bool:
    primes = [2, 3, 5, 7, 11, 13, 17]
    i = 1
    str_number = str(number)

    for prime in primes:
        if not int((str_number[i:i+3])) % prime == 0:
            break
        i += 1
    else:
        return True
    
    return False

def main():
    total = 0
    # lower limit is the 0 to 9 pandigital which is mentioned in question
    for p in itertools.permutations("0123456789"):
        str_num = "".join(p)
        i = int(str_num)
        if property(i) and isPandigitalZeroToNine(i):
            total += i
            print(i)

    print("Sum:", total)


if __name__ == "__main__":
    main()


