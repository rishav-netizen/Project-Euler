MILLION = 1000000

def sumOfProperDivisorsOf(n: int) -> int:
    total = 1 # since 1 is already every integers proper divisor
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            total += i
            if (n != i*i): # handling edge case for squares so that i dont accidentally add twice to the total
                total += n/i
    return int(total)

# amicable chain must return to starting point n
def amicableChainLength(n): 
    count = 0
    members = {n} # already have n so that we are able to break the while loop
    i = sumOfProperDivisorsOf(n)
    while i not in members:
        members.add(i)
        i = sumOfProperDivisorsOf(i)
        if i > MILLION:
            return -1
        if i == 1:
            return -1
        count += 1

    if i == n: # property of amicable chain
        return count
    else:
        return -1


def minMember(n):
    count = 0
    members = {n}
    i = sumOfProperDivisorsOf(n)
    while i not in members:
        members.add(i)
        i = sumOfProperDivisorsOf(i)
        if i > MILLION:
            return -1
        if i == 1:
            return -1
        count += 1

    if i == n:
        return min(members)
    else:
        return -1


def main():
    max_length = 0
    max_i = 0

    for i in range(2, MILLION):
        current_len = amicableChainLength(i)
        if max_length < current_len:
            max_length = current_len
            max_i = i

    print(minMember(max_i))
    # print(max_length, minMember(max_i), max_i)

main()