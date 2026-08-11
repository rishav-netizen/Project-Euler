def rects(m, n):
    # by observation we can notice that for n * 1 rect we have n(n+1)/2 rects
    # so for m*n we deduce this
    return m*(m+1)*n*(n+1)/4

TWO_MILLION = 2000000

def main():
    best = 10000
    best_pair = (0, 0)
    for m in range(1, 2001):
        for n in range(m, 2001):
            rect_count = rects(m, n)
            difference = abs(TWO_MILLION - rect_count)
            if difference < best:
                best = difference
                best_pair = (m, n)
            if rect_count > TWO_MILLION:
                break
            # if (rect_count == TWO_MILLION + best) or ((rect_count == TWO_MILLION - best)):
            #     print(f"m = {m}, n = {n}, area = {m*n}")
            
    # print(best)
    print(f"Least difference = {best}\nm = {best_pair[0]}, n = {best_pair[1]}, area = {best_pair[0] * best_pair[1]}")


main()
