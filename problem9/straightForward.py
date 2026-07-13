s = 1000
for a in range(3, (s-3)//3 + 1):
    for b in range(a+1, (s-1-a)//2 + 1):
        c = s - a - b
        if (c*c == a*a + b*b):
            print(a*b*c)

# another person approach
for i in range(1,1000):
    for j in range(i+1,1000):
        z = 1000 - i - j
        if z > i and z > j:
            if (i**2)+(j**2) == z**2:
                print(i*j*z)