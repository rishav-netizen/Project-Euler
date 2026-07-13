def cornerSum(n): # for n * n matrix, min n = 3
    return 4*n**2 -6*(n - 1)

sum = 1
n=3
while (n<=1001):
    sum+=cornerSum(n)
    n+=2

print(sum)