def square_digit(n: int) -> int:
    str_num = str(n)
    length = len(str_num)
    result = 0
    for i in range(length):
        digit = int(str_num[i])
        result += digit**2

    return result


def arrives_at(n: int) -> int:
    value = square_digit(n)
    while value not in [89, 1]:
        value = square_digit(value)

    return value

TEN_MILLION = 10000000

def main():
    count_89 = 0
    for i in range(1, TEN_MILLION + 1):
        if arrives_at(i) == 89:
            count_89 += 1
        
    print(count_89)
        

if __name__ == "__main__":
    main()