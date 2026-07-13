'''
basically the max sum any n digit number would give would be n * 9^5
we checked for 5digit, 6digit and 7digit number
and saw that max 7digit number yielded a 6digit number, which is obviously less
hence we only should check till 6digit numbers

but since max 6 digit number would give sum 6 * 9^5
which would be 354294, so we only check for numbers below this 6 digit number
'''

def digitPowerSum(number, power):
    summation = 0
    for digit in str(number):
        summation += int(digit)**power
    return summation


print("Checking for upperlimit: ")
for digits in range(5, 8):
    number = digits * 9**5
    print(number, digits > len(str(number)))

print("\nFor the actual answer: ")
total = 0
count = 0
for i in range(2, 6 * 9**5 + 1): # exclude 1 since it doesnt have digits technically
    if i == digitPowerSum(i, 5):
        total += i
        count += 1
        print(f"Numbers that can be written as the sum of fifth power of their digits: {i}")

print(f"Sum of those {count} numbers is", total)
