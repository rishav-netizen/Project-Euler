# brute force

MILLION = 1000000

fractional_part = ""

for i in range(MILLION + 1):
    fractional_part += str(i)

product = 1

for i in range(7):
    product *= int(fractional_part[10**i])

print(product)