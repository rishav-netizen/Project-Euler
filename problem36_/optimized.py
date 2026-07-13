def isPalindrome(n: str):
    return n == n[::-1]

MILLION = 1000000
result = 0
for i in range(1, MILLION):
    binary = bin(i)[2:] #built in python function that returns binary starting with 0b hence the [2:]
    if isPalindrome(str(i)) and isPalindrome(binary):
        print(i, binary)
        result += i

print("Sum:", result)
