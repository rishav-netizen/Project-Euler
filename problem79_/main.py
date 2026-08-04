def usedNumbers(numbers: list[str]) -> set[str]:
    usedNumbers = set()

    for number in numbers:
        valuesBefore[number[1]].add(number[0])
        valuesBefore[number[2]].add(number[0])
        valuesBefore[number[2]].add(number[1])

        usedNumbers.update(number) # adds each item of iterable separately to set
    
    return usedNumbers


def itemWithNoneBefore(used: set[str]) -> str:
    # print(valuesBefore.items()) #returns the key value tuple list
    for digit in used:
         #items with no numbers before them must be the starting digit of code (or theyre not in the code)
        if (len(valuesBefore[digit]) == 0):
            return digit
        

# using set cuz it wont allow dublicates
valuesBefore = {
    '0': set(),
    '1': set(),
    '2': set(),
    '3': set(),
    '4': set(),
    '5': set(),
    '6': set(),
    '7': set(),
    '8': set(),
    '9': set(),
}

def main():
    numbers = []

    with open("0079_keylog.txt", "r") as file:
        for line in file:
            numbers.append(line.strip())


    # 4 and 5 arent being used
    # first digit 7

    code = ""
    usedNums = usedNumbers(numbers)
    while usedNums:
        chosenDigit = itemWithNoneBefore(usedNums)
        code += chosenDigit
        # print(chosenDigit)
        for before_set in valuesBefore.values():
            before_set.discard(chosenDigit)

        usedNums.remove(chosenDigit)
        del valuesBefore[chosenDigit]

    print(code)


if __name__ == "__main__":
    main()

