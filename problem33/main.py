digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
'''
n = 10*e + c 
d = 10*c + f 
n/d = e/f

'''
prod_n = 1
prod_d = 1
for e in digits:
    for f in digits:
        for c in digits:
            n = 10*e + c 
            d = 10*c + f 
            if n < d and n/d == e/f:
                print(f"{n}/{d} = {e}/{f}")
                prod_n *= n
                prod_d *= d

print(f"{prod_n}/{prod_d}") # 1/100