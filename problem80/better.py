from math import isqrt

def isPerfectSquare(n: int) -> bool:
    root = isqrt(n) # returns integer sqrt
    return root*root == n

def digitalSumOf(n: int) -> int:
    first_hundred = str(isqrt(n * (10**(limit*2))))
    total = 0
    for i in first_hundred:
        total += int(i)

    return total

limit = 99 # after the integer we want 99 digits

def main():
    # like if i want 3 digits of root(2) i would just do root(2 x 10^6) = root(2) x 10^3
    total = 0

    for i in range(1, 100 + 1):
        if not isPerfectSquare(i):
            total += digitalSumOf(i)

    print(total)

if __name__ == "__main__":
    main()
