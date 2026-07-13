n_old = 3
d_old = 2 
count = 0
for i in range(1000):
    n_new = n_old + (2 * d_old)
    d_new = n_old + d_old
    if len(str(n_new)) > len(str(d_new)):
        count += 1 
    # print(f"{n_new}/{d_new}")
    n_old, d_old = n_new, d_new


print(count)