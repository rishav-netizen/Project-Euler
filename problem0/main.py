result = 0

for i in range(1,225000):
    if (i % 10) in {1, 3, 5, 7, 9}:
        result += i**2

print(result)

