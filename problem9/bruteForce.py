# find a pythagorean triplet for which a + b + c = 1000
# tell abc, if a < b < c
# 2*c^2 +(ab+bc+ac) = 10^6
# a+b>c, b+c>a, c+a>b


for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            l = i**2 + j**2
            r = k**2
            if ((l == r) and (k + j + i == 1000)):
                print(i,j,k)
                break

# printed i,j,k
print(200*375*425)
    