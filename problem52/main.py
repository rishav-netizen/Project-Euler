# by intuition only the number should be 6digit i think
# 6x <= 999999 means x <= 166666

for x in range(100000, 166666 + 1):
    if all(sorted(str(x)) == sorted(str(i * x)) for i in range(2, 7)):
        print(x)
        break
    
    
        