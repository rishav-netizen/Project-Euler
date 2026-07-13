def factors_of(n):
    if n<=3:
        return {n}
    
    factors = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            factors.add(d)
            while n % d == 0:
                n //= d
        d += 1

    if n > 1:
        factors.add(n)

    return factors

n = 2
limit = 1000000000000000000000
count = 0
consecutive_count = 5
while n < limit:
    if len(factors_of(n)) == consecutive_count:
        count += 1
    else:
        count = 0
    
    if count == consecutive_count:
        consecutives = []
        for i in range(n-(consecutive_count-1), n+1):
            consecutives.append(i)
        print(consecutives)
        break
    n+=1