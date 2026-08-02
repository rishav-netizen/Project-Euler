from math import factorial

MILLION = 1000000

def factSum(n: int) -> int:
    str_num = str(n)
    total = 0
    for i in str_num:
        total += factorial(int(i))

    return total


def chainLength(n: int) -> int:
    chainNums = {n}
    num = factSum(n)
    count = 1
    while num not in chainNums:
        chainNums.add(num)
        num = factSum(num)
        count += 1

    return count

def main():
    sixtyCount = 0
    for i in range(1, MILLION + 1):
        if chainLength(i) == 60:
            sixtyCount += 1
    print(sixtyCount)


main()