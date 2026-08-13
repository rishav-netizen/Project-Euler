from math import log
# instead of comparing powers we take log of power to get b log(a) from a^b
with open("0099_base_exp.txt", "r") as file:
    maximum = 0
    max_a = 0
    max_b = 0
    max_line = 0
    line_number = 0
    for line in file:
        line_number += 1
        line = line.strip()
        numbers = line.split(",")
        a = int(numbers[0])
        b = int(numbers[1])
        value = b * log(a)
        if (value > maximum):
            maximum = value
            max_a = a
            max_b = b
            max_line = line_number
    # print(maximum, max_a, max_b, max_line)
    print(max_line)


    