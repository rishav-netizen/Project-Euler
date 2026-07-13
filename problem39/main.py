'''
perimeter p of a right triangle
find p <= 1000 for which there are the most number of triplets
{a, b, c}
a + b + c = p

'''

# list of sets
# triplets = [{20, 48, 52}, {24, 45, 51}, {30, 40, 50}]

def generateTriplets(p: int) -> list:
    triplets = []
    triplet = set()
    for a in range(1, p//3):
        b = (p**2 - 2*p*a)/(2*(p-a))
        if (a<=b) and (b.is_integer()):
            triplet = {a, int(b), int(p-(a+b))}
            triplets.append(triplet)
    return triplets

pMax = 1000
best_p = 0
maxLen = 0
for p in range(1, pMax):
    length = len(generateTriplets(p))
    if length > maxLen:
        maxLen = length
        best_p = p
print(best_p)
        

