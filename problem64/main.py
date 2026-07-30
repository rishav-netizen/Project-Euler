from math import isqrt


def get_period_length(n: int) -> int:
    a_not = isqrt(n)
    a_old = a_not
    m_old = 0
    d_old = 1
    pairs = []
    m, d = (0, 1)
    count = 0
    while True:
        m = d_old * a_old - m_old
        d = (n - (m**2)) // (d_old) 
        a = (a_not + m) // d
        if (m, d) not in pairs:
            pairs.append((m, d))
            m_old = m
            d_old = d
            a_old = a
            count += 1
        else:
            break
        # print(pairs)
    return count

def main():
    N = 10000
    odd_period = 0
    for i in range(2, N+1):
        if not (i**0.5).is_integer():
            period = get_period_length(i)
            if period % 2 != 0:
                odd_period += 1
    print(odd_period)


if __name__ == "__main__":
    main()
