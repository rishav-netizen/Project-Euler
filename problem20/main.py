from math import factorial

def factDigitSum(n):
    result = 0
    num = factorial(n)
    for i in str(num):
        result += int(i)
    
    return result


print(factDigitSum(100))

