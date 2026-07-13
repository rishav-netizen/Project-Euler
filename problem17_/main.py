# ? solved this in third wave coffee in BLR lmfao

# make dictionaries
ones = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4
}

teens = {
    10: 3,
    11: 6,
    12: 6,
    13: 8, 
    14: 8, 
    15: 7, 
    16: 7, 
    17: 9, 
    18: 8, 
    19: 8
}

tens = {
    20: 6, 
    30: 6, 
    40: 5, 
    50: 5, 
    60: 5, 
    70: 7, 
    80: 6, 
    90: 6
}

HUNDRED_LEN = 7 # len("hundred")
AND_LEN = 3 # len("and")

def get_letter_count(n):
    if n == 1000: #onethousand
        return len("onethousand")

    count = 0

    if n >= 100:
        hundreds_digit = n//100
        count += ones[hundreds_digit] + HUNDRED_LEN

        if (n % 100 != 0):
            count += AND_LEN

    remainder = n % 100

    if remainder < 10:
        count += ones[remainder]
    elif (remainder >= 10) and (remainder <= 19):
        count += teens[remainder]
    elif remainder > 19:
        ones_digit = remainder % 10
        tens_value = remainder - ones_digit
        count += tens[tens_value]
        count += ones[ones_digit]
    elif remainder == 0:
        pass

    return count


# print(get_letter_count(456))
# print(len("fourhundredandfiftysix"))

result = 0
for i in range(1, 1001):
    result += get_letter_count(i)

print(result)
