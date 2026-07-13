def P(n):
    return n*(3*n - 1)/2


k = 1
found = False
while not found:
    for j in range(k - 1, 0, -1):
        P_k = P(k)
        P_j = P(j)
        D =  P_k - P_j
        n = ((1 + 24*D)**0.5 + 1) / 6
        if n.is_integer():
            S = P_k + P_j
            m = ((1 + 24*S)**0.5 + 1) / 6
            if m.is_integer():
                print(D)
                found = True
                break
    k += 1



