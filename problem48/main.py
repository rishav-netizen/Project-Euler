current_sum = 0
for i in range(1, 1001):
    # current_sum += pow(i, i, 10**10)
    current_sum += (i**i) % (10**10)
    current_sum %= 10**10

print(current_sum)