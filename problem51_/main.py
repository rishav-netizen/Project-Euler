def primes_till(n: int):
    if n <= 1:
        return set()
    
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for a in range(2, int(n ** 0.5) + 1):
        if is_prime[a]:
            for multiple in range(a*a, n + 1, a):
                is_prime[multiple] = False
    
    primes = set()
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.add(i)
    
    return primes


# we want 8 primes by replacing digits hence we cant have the last digit be replaced 
# since 2, 4, 6, 8, 5, 0 would result in non primes leaving only 1 3 7 9 which is not gonna get us 8 primes
def is_eligible(n: int):
    str_n = str(n)
    l = len(str_n)
    if any(d in str_n for d in "012"):
        zeros = str_n.count('0')
        ones = str_n.count('1')
        twos = str_n.count('2')
        if 3 in (zeros, ones, twos):
            the_digit = ''
            if zeros == 3:
                the_digit = '0'
            elif ones == 3:
                the_digit = '1'
            else:
                the_digit = '2'

            if str_n[0] == '0':
                return False
            if str_n[l-1] == the_digit:
                return False
            
            check_sum = str_n.replace(the_digit, '0')
            others_sum = 0
            for digit in check_sum:
                others_sum += int(digit)
            if others_sum % 3 == 0:
                return False
            
            # since a non empty string would be true only hence we return the digit so that we can use it in our main loop
            return the_digit
    return False


limit = 1000000 
primes = sorted(primes_till(limit))
def main():
    for prime in primes:
        eligibility = is_eligible(prime)
        str_num = str(prime)
        if eligibility:
            count = 0
            for i in range(10):
                new_str = str_num.replace(eligibility, str(i))
                if new_str[0] == '0':
                    continue
                if int(new_str) in primes:
                    count += 1  

                if count == 8:
                    print(str_num)
                    # we return so that next numbers arent checked
                    return
                

if __name__ == "__main__":
    main()

"""
ALGORITHM SUMMARY: Finding an 8-Prime Family
        
To avoid brute-forcing every prime, we aggressively filter candidates 
using a few rules of number theory:
        
1. Limit Starting Digits 🔢
   The repeating digits we target to swap must be 0, 1, or 2.
   Basically we are finding the smallest prime of the 8 primes list so it has to be 0, 1 or 2. 
   If we target a digit like 3, we only have 7 possible replacements 
   (3 through 9). It's impossible to find 8 primes with only 7 options.
           
2. Protect the Last Digit 🛑
   The target digit cannot be the last digit of the prime. Swapping 
   the last digit with even numbers (0, 2, 4, 6, 8) or 5 guarantees 
   composite numbers, leaving too few options to reach an 8-prime family.
           
3. The "Swap 3" Modulo Rule 📐
   We specifically look to replace 3 identical digits. Why? Replacing 
   3 digits with any new digit 'd' adds (3 * d) to the number's total sum. 
   Since (3 * d) is always a multiple of 3, the sum of the *other* digits 
   completely controls divisibility by 3. 
   
   If the remaining, unswapped digits sum to a multiple of 3, EVERY 
   possible replacement will result in a total sum that is a multiple of 3. 
   This would yield exactly zero primes, so we instantly discard these candidates.
"""