'''
1pound = 100pence
Denominations(8): 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

Number of ways to make 2pound?

max number of each denomination we can use:
£2 (200p) = 1
£1 (100p) = 2
50p = 4
20p = 10
10p = 20
5p = 40
2p = 100
1p = 200

DYNAMIC PROGRAMMING APPROACH (apparently)
i think we should keep decreasing the higher denomination coins and 
replace them with all possible combinations of smaller ones using the same logic
'''

#! This is the Tabulation (bottom up) approach
#? there is also Memoization (tod down) approach 
#? the two approaches in dynamic programming
# length 201, each index will store the number of ways to make that indexed amount in penny
# so we decide a base case, for DP its 1, so 1 way to make 0 pence
target = 200
ways = [1] + [0] * target
# print(ways)
coins = [1, 2, 5, 10, 20, 50, 100, 200]

for coin in coins:
    for amount in range(coin, 201): #start from coin not from 1 because if amount < coin then makesno sense to check
        ways[amount] += ways[amount - coin]
        #! (amount - coin) represents the total we need to have built up before we add the coin we are currently holding.
        print(ways)

print(f"Total {ways[target]} different ways to make {target}p")


'''
Dynamic programming is fundamentally linked to recursion. In fact, it is essentially the exact same logic, just flipped upside down!
Here is how the two approaches compare:
•	Recursion (Top-Down): If you wrote this recursively, you would start at your massive target of 200p. The code would say, "To solve 200p, I need to call this exact same function again to solve for 180p." It keeps calling itself, drilling further and further down until it hits the base case of 0p.
•	Dynamic Programming (Bottom-Up): This is the method we just wrote. Instead of starting at the top and drilling down, we started at the base case (0p) and built our way up.
By building from the bottom up and saving our intermediate answers in a list (a technique formally called tabulation), we completely avoided the biggest trap of recursion: recalculating the exact same math over and over again. That is why your script can process all those combinations in a fraction of a millisecond.
'''