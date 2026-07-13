def fib(n):
    t0 = 0
    t1 = 1
    s = 0

    if n <= 1:
        return n;

    for i in range(2, n+1):
        s = t0 + t1
        t0 = t1
        t1 = s
    
    return s

def print_fib(n):
    for i in range(0, n):
        print(fib(i), end="")
        if (i < n-1):
            print(", ", end='')
    print()

def evenFibSum(limit):
    result = 0
    i = 0
    while fib(i) < limit:
        if (fib(i) % 2 == 0):
            result += fib(i)
        i+=1
    return result

print(evenFibSum(4000000))