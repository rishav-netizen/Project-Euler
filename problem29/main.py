terms = set() #! a set by default doesnt allow dublicates
# terms = [] #? using a list but it would be slow, and to search it would be done from start which is bad
for a in range(2, 101):
    for b in range(2, 101):
        terms.add(a**b) # to add into a set
        # if a**b not in terms:
        #     terms.append(a**b)

# ? same as the set nested loop but in just one line, known as comprehension
# terms = {a**b for a in range(2, 101) for b in range(2, 101)}



print(len(terms))
# print(terms)