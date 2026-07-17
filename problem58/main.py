def is_prime(n): # dont use prime sieve for this one
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
        
    return True

def main():
    n = 2 # cant be one since no spiral then only 1 exists in the centre
    prime_count = 0 
    ratio = 0
    while True:
        s = 2*n - 1 # side length increase by 2 in each spiral

        bot_right = s**2 # perfect square hence never prime
        bot_left = s**2 - (s-1)
        top_left = s**2 - 2*(s-1)
        top_right = s**2 - 3*(s-1)
        
        diag_nums_count = 2*s - 1

        potential_primes = [bot_left, top_left, top_right] # hence here we exclude bot_right
        for corner in potential_primes:
            if is_prime(corner):
                prime_count += 1
        
        ratio = (prime_count/diag_nums_count) * 100

        if ratio < 10:
            print(s)
            break

        n += 1


if __name__ == "__main__":
    main()


"""
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

s = 2n - 1

BR s^2
BL s^2 - (s-1)
TL s^2 - 2(s-1)
TR s^2 - 3(s-1)

"""