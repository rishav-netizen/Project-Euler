'''
34 - 333

'''
def isPandigital(n: int) -> bool:
    str_n = str(n)
    if len(str_n) == 9:
        return all(digits in str(n) for digits in "123456789")
    return False
    
# print(isPandigital(123456789))

def concatenator(n: int) -> int:
    result = 0
    str_result = str(result)[2:]
    i = 0
    while len(str_result) <= 9:
        result = n*i
        str_result += str(result)
        i += 1
    return int(str_result)

# number = 978
# print(concatenator(number))
# print(isPandigital(concatenator(number)))
        

def largestPandigital():
    max = 0
    for i in range(2, 10000):
       concatenated = concatenator(i)
       if isPandigital(concatenated):
            # print(i)
            if concatenated > max:
                max = concatenated
                print(i)
    return max

print(largestPandigital())

