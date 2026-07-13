# def triangleNumber(n) -> int: 
#     return n*(n+1)/2

# setTriangleNumbers = set()
# for i in range(1, 50):
#     setTriangleNumbers.add(triangleNumber(i))

def wordValue(word: str) -> int:
    value = 0
    for letter in word:
        value += ord(letter.upper()) - ord('A') + 1
    return value

with open("0042_words.txt", "r") as file:
    words = file.read().replace('"', "").split(",")

count = 0
for word in words:
    value = wordValue(word)
    n = ((8*value + 1)**0.5 + 1)/2
    if n.is_integer():
        count += 1

print(count)

