# gotta perform long division like we do on paper
longest_cycle = 0
for d in range(2, 1000):
    recurring_count = 0
    remainders = []
    current_remainder = 1

    while (current_remainder != 0) and (current_remainder not in remainders):
        if current_remainder not in remainders:
            remainders.append(current_remainder)
        
        current_remainder *= 10

        current_remainder %= d

    
    recurring_count = len(remainders)
    longest_cycle = max(recurring_count, longest_cycle)
    if recurring_count == 982:
        print(d)
        break

