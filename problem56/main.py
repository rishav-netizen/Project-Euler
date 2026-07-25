def digitSum(number: int) -> int:
    total = 0
    for i in str(number):
        total += int(i)
    return total

max_sum = 0

for a in range(2, 100):
    for b in range(2, 100):
        number = a ** b
        digit_sum = digitSum(number)
        max_sum = max(max_sum, digit_sum)
        
print(max_sum)


