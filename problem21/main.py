def d(n):
    result = 1 # because we dont wanna check 1 since 1 is always there for all number
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            if (n // i == i):
                result += i
            else:
                result += i + (n // i)
    return result

summation = 0
for i in range(1, 10000):
    b = d(i)
    if (d(b) == i) and b != i:
        summation += i

print(summation)

