def F(n):
    t1 = 1
    t2 = 1
    s = 0
    if (n<=1):
        return n
    if n==2:
        return t2
    for i in range(3, n + 1):
        s = t1 + t2
        t1 = t2
        t2 = s
    return s

for i in range(4500, 5000):
    if len(str(F(i))) == 1000:
        print(i)

