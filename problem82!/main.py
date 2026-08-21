matrix = []
with open("0082_matrix.txt", "r") as file:
    for line in file:
        line = line.strip().split(",")
        row = []
        for i in line:
            row.append(int(i))
        matrix.append(row)
print(matrix)