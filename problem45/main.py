def T(n): 
    return n*(n + 1)/2

def P(n):
    return n*(3*n - 1)/2

def H(n):
    return n*(2*n - 1)

# n-th hexagonal number is (2n - 1)-th triangular number

i = 144
found = False
while not found:
    h = H(i)
    n = ((1 + 24*h)**0.5 + 1) / 6
    if n.is_integer():
        # j = ((1 + 8*h)**0.5 - 1) / 2
        # print(T(j))
        print(h)
        found = True
        break
    i += 1
 