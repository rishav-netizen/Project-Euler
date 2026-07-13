MILLION = 1000000

def fact(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


summation = 0
for i in range(9, 0, -1):
    summation += fact(i)

print(i, summation)
# print(fact(9))