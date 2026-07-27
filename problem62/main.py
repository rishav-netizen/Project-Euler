from itertools import permutations
import math

# print("".join(sorted("543")))

n = 405
found = False
table = {}
while not found:
    cube = n**3
    key = "".join(sorted(str(cube)))

    if key not in table:
        table[key] = []
    table[key].append(n)

    if len(table[key]) == 5:
        print(f"List of 5 permutable cubes: {table[key]}")
        print(f"The smallest cube is: {table[key][0]} ^ 3 = {table[key][0]**3}")
        found = True

    n += 1