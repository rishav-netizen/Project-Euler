def main():
    target_limit = 100

    ways = [0] * (target_limit + 1)
    ways[0] = 1
    for i in range(1, target_limit): #since to make 100 we cant use 100, so the upper limit excludes it
        for target_sum in range(i, target_limit + 1): #here we must have 100 so that the 100th index can we used to tell us the answer
            ways[target_sum] += ways[target_sum - i]

    print(ways[100])


if __name__ == "__main__":
    main()