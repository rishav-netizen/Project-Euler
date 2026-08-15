matrix = [] #the 80x80 matrix
scores = [[0 for _ in range(80)] for _ in range(80)]

with open("0081_matrix.txt", "r") as file:
    for line in file:
        line_array = line.strip().split(",")
        row = []
        for value in line_array:
            row.append(int(value))
        matrix.append(row)


''' DP QUESTIONS ARE INSANE
    if we are the top edge then we can come from left only
    and if on left edge then we can come down only
    and for any other place there is both possibility so we choose the min one
'''

scores[0][0] = matrix[0][0]

for row in range(80):
    for col in range(80):
        if row == 0: # if we are at the top row, we can only come from left not top
            scores[0][col] = matrix[0][col] + scores[0][col - 1]
        elif col == 0: # if we are at the left col, we can only come from top not left
            scores[row][0] = matrix[row][0] + scores[row - 1][0]
        else: # for other parts of matrix
            scores[row][col] = min(scores[row][col - 1], scores[row - 1][col]) + matrix[row][col]

print(scores[79][79])