def reverse_add(number, iterations):
    result = number 
    for i in range(iterations):
        result = result + int(str(result)[::-1])
    return result

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def main():
    lychrel_count = 0
    for i in range(1, 10000):
        for iterations in range(1, 50):
            operated_value = reverse_add(i, iterations)
            if isPalindrome(operated_value):
                break
        else:
            lychrel_count += 1
    print(lychrel_count)

if __name__ == "__main__":
    main()