
# ? SEIVE METHOD
limit = 130_000_000
# list stores the number of distinct prime factors each number has
factor_counts = [0] * (limit + 1)

for i in range(2, limit + 1):
    # If the count is 0, it means 'i' has no factors yet, so it must be a prime!
    if factor_counts[i] == 0:
        # Loop through all multiples of this prime up to the limit
        for multiple in range(i, limit + 1, i):
            factor_counts[multiple] += 1

# now that we know the number of prime factors each number has we need to find consecutives
consecutives = 5
count = 0
for i in range(2, limit + 1):
    if factor_counts[i] == consecutives:
        count += 1
    else:
        count = 0
    
    if count == consecutives:
        consecutiveNumbers = list(range(i-(consecutives - 1), i + 1))
        # ! INSTEAD OF THIS 
        # consecutiveNumbers = []
        # for j in range(i-(consecutives - 1), i + 1):
        #     consecutiveNumbers.append(j)
        print(consecutiveNumbers)
        break