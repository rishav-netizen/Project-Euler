def sumOfSquares(n):
    return (int)(n*(n + 1)*(2*n + 1))/6

def sumOf(n):
    return (int)(n*(n + 1))/2


print(sumOfSquares(100))
print(sumOf(100)**2)
print(sumOf(100)**2 - sumOfSquares(100))

