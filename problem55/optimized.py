def isPalindrome(n):
    return str(n) == str(n)[::-1]

def main():
    lychrel_count = 0
    for i in range(1, 10000):
        operated_value = i
        for iterations in range(1, 50):
            operated_value += int(str(operated_value)[::-1])
            if isPalindrome(operated_value):
                break
        else:
            lychrel_count += 1
    print(lychrel_count)

if __name__ == "__main__":
    main()