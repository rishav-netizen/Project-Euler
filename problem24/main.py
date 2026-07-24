MILLION = 1000000

def fact(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# print(999999 // fact(9)) # millionth permutation starts with 2
# print(999999 % fact(9))

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = MILLION - 1
number = ''
for i in range(9, -1, -1):
    digit_index = target // fact(i)
    number += str(digits[digit_index])
    digits.remove(digits[digit_index])
    target = target % fact(i)

print(number)
# print(digits)