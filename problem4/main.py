maximum = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        p = i * j
        if str(p)[::-1] == str(p):
            maximum = max(maximum, p)

print(maximum)

