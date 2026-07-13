target = 999 #since 1000 is exclusive

def SumDivisibleBy(n):
    p = target // n
    return n*p*(p+1)/2

result = SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)
print(result)

''' !! from their pdf !!
To get a more efficient solution you could also calculate the sum of the numbers less
than1000 that are divisible by 3, plus the sum of the numbers less than1000 that are divisible
by 5. But as you have summed numbers divisible by 15 twice you would have to subtract the
sum of the numbers divisible by 15

Then the answer would be
SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)
Let’s look at the details of our function and take as example n=3.
We would have to add:
3+6+9+12+......+999=3*(1+2+3+4+...+333)
For n=5 we would get:
5+10+15+...+995=5*(1+2+....+199)
Now note that 199=995/5 but also 999/5 rounded down to the nearest integer.
In many programming languages there exists a separate operator for that: div 
If we now also note that sum of p natural numbers 1+2+3+...+p=½*p*(p+1) our program becomes as above.
'''