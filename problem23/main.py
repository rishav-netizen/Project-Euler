def sumOfProperDivisors(n: int) -> int:
    result = 1
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            if (n // i == i):
                result += i
            else:
                result += (i+(n // i))
    return result

def isAbundant(n):
    return sumOfProperDivisors(n) > n

abundant: list[int] = [] # length = 6965
for i in range(1, 28124):
    if isAbundant(i):
        abundant.append(i)

can_be_written_as_sum: list[bool] = [False] * 28124

for i in abundant:
    for j in abundant:
        if (i + j) <= 28123:
            can_be_written_as_sum[i+j] = True

result = 0
length = len(can_be_written_as_sum)
for i in range(length):
    if not can_be_written_as_sum[i]:
        result += i

print(result)