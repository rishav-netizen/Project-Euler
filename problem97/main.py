value = 2
last = 1
for i in range(1, 7830457):
    value *= 2
    value %= 10**10 # for last 10 digits

value *= 28433
value %= 10**10
last += value

print(last)