def decimal_to_binary(n):
    if n == 0:
        return '0'
    
    binary = ""

    while n:
        binary += str(n%2)
        n //= 2
    
    return int(binary[::-1])

def isPalindrome(n):
    return str(n) == str(n)[::-1]

MILLION = 1000000
result = 0
for i in range(1, MILLION):
    binary = decimal_to_binary(i)
    if isPalindrome(i) and isPalindrome(binary):
        print(i, binary)
        result += i

print("Sum:", result)
