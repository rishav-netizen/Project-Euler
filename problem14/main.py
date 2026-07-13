max_len = n = best_n = 0
for i in range(13, 1000000):
    n = i
    length = 0
    while n != 1:
        length += 1
        if (n % 2 == 0):
            n = n//2
        else: 
            n = 3*n + 1
    if length > max_len:
        max_len = length
        best_n = i

print(best_n)
print(max_len)