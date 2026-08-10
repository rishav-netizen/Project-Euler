from math import isqrt
import decimal

def isPerfectSquare(n: int) -> bool:
    root = isqrt(n) # returns integer sqrt
    return root*root == n

def digitalSumOf(n: int) -> int:
    root = decimal.Decimal(n).sqrt()
    integer_part = int(str(root).split(".")[0])
    decimal_part = str(root).split(".")[1]
    
    # since the integer takes 1 space we just need the other 99 digits, couldve written 99 or limit - 1 
    first_hundred = decimal_part[0:limit - len(str(integer_part))] 
    
    total = integer_part

    for i in first_hundred:
        total += int(i)
    return total

limit = 100 # first 100 digits including the integral part, 99 decimal digits

def main() -> int:
    # for decimal calculation we set precision
    decimal.getcontext().prec = limit + 5 # limit + 5 so that i am safe from round offs of the last digits

    finalSum = 0

    for i in range(1, limit + 1):
        if not isPerfectSquare(i):
            finalSum += digitalSumOf(i) 

    print(finalSum)
    return 0
    # print(digitalSumOf(2))

main()