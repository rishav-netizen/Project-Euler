from math import comb
MILLION = 1000000
count = 0
for n in range(1, 101):
    for r in range(n//2 + 1):
        if comb(n, r) > MILLION:
            if r != n - r:
                count += 2
            else:
                count += 1 
print(count)