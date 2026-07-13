def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def digit_fact(n):
    resultant = 0
    for i in str(n):
        resultant += fact(int(i))
    return resultant

def result():
    for i in range(11, 60000):
        if digit_fact(i) == i:
            print(i)

if __name__ == "__main__":
    result()