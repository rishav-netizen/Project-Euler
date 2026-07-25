def isPandigitalProduct(multiplicand, multiplier, product):
    total_length = len(str(multiplicand)) + len(str(multiplier)) + len(str(product))
    if total_length > 9:
        return False
    
    common_string = (str(multiplicand)) + (str(multiplier)) + (str(product))
    if all(i in common_string for i in "123456789"):
        return True
    
def main():
    # a * b = c 
    # for this to be pandigital length of a,b can be 1,4 or 2,3
    products = set()
    for a in range(1, 100):
        for b in range(9999, 99, -1):
            c = a * b
            if isPandigitalProduct(a, b, c):
                if c not in products:
                    products.add(c)

    print(sum(products))

if __name__ == "__main__":
    main()