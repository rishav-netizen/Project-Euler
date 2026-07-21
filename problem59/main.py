def main():    
    with open("0059_cipher.txt", "r") as file:
        for line in file:
            # print(line)
            pass

        cipher = line.split(",")
        # print(cipher)

    possibleKeys = combinations()
    # print(possibleKeys)
    length = len(cipher)
    # print(length)
    for key in possibleKeys:
        decryptedValue = ""
        asciiSum = 0
        for i in range(length):
            encryptedValue = int(cipher[i])
            operated = encryptedValue ^ key[i % 3]
            decryptedValue += chr(operated)
            asciiSum += operated
        if " the " in decryptedValue:
            print(asciiSum)
            print(decryptedValue)
            break

            
        
        

def combinations():
    key = []
    allPossibilities = []
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                key.append(i)
                key.append(j)
                key.append(k)
                allPossibilities.append(key)
                key = []

    # print(len(allPossibilities))
    # print(allPossibilities[2634])
    return allPossibilities

        

if __name__ == "__main__":
    main()

"""
the key is three lower case character of the alphabets so possibility is 26 ** 3
"""