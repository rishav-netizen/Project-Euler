import math

def solve() -> int:
    a, b = 0, 1
    k = 1 # kth fibonacci number

    golden_ratio = (1 + 5**0.5) / 2
    log_phi = math.log10(golden_ratio)
    log_rt5 = math.log10(5 ** 0.5)

    while True:
        a, b = b % 10**9, (a + b) % (10 ** 9)
        k += 1
        if isPandigital(b):
            # this means last 9 are pandigital now check for first 9
            t = k * log_phi - log_rt5 # t is log10(F_k)
            frac = t - int(t) # F_k its fractional part gives the starting digits and integral part gives number of digits
            first_ten = int((10 ** frac) * (10**8))

            if isPandigital(first_ten):
                return k

def isPandigital(n):
    str_n = str(n)
    return len(str_n) == 9 and set(str_n) == set("123456789") 

def main():
    print(solve())

if __name__ == "__main__":
    main()
