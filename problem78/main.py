def main():    
    amount = 60000 # lowkey a guess lol
    MILLION = 1000000
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coins in range(1, amount + 1): #include amount in range because to make a certain amount we can use use that amount of coins too
        for target_sum in range(coins, amount + 1):
            ways[target_sum] += ways[target_sum - coins]
            ways[target_sum] %= MILLION #already doing this so that numbers dont increase hella

    for i in range(amount + 1):
        if ways[i] == 0:
            print(i)
            break

main()

