"""
    k = m + (p - s)
    m = no. of factors taken
    p = product of those m factors
    s = sum of those m factors
    p - s is basically the no. of 1's we would need to reach the number using sum, if its already reached by product of factors
"""

def fill_minimals(p, s, m, prev_factor):
    k = m + p - s
    if(k <= MAX_K and m > 1):
        minimal[k] = min(p, minimal[k])

    for i in range(prev_factor, MAX_N // p):
        fill_minimals(p * i, s + i, m + 1, i)

MAX_K = 12000 
MAX_N = 2 * MAX_K
minimal = [float('inf')] * (MAX_K + 1)
fill_minimals(1, 0, 0, 2)

result = sorted(set(minimal)) # get rid of duplicates and sort also
result.remove(float('inf'))
# print(result)
print(sum(result))