# n digit number would range from 10**(n-1) to 10**(n) - 1
from math import log10

count = 0
for x in range(1, 10):
    n = 1    
    while  (n <= (1/(1 - log10(x)))):
        value = x**n
        if len(str(value)) == n:
            print(f"{x}^{n} == {value}")
            count += 1
        n += 1


print(f"\ncount: {count}")
