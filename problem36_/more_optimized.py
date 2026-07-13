def isPalindrome(n: str):
    return n == n[::-1]

def generatePalindrome(s: str, odd_length):
    if odd_length:
        return s + s[-2::-1] 
    return s + s[::-1]

result = 0
for i in range(1, 999 + 1):
    strNum = str(i)
    odd = generatePalindrome(strNum, True)
    even = generatePalindrome(strNum, False)
    binaryOdd = bin(int(odd))[2:] #built in python function that returns binary starting with 0b hence the [2:]
    binaryEven= bin(int(even))[2:] #built in python function that returns binary starting with 0b hence the [2:]

    if isPalindrome(odd) and isPalindrome(binaryOdd):
        result += int(odd)
    if isPalindrome(even) and isPalindrome(binaryEven):
        result += int(even)

print("Sum:", result)


# s = "123"
# l = len(s)
# print(s + s[l-2::-1])

