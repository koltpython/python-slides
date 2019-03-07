for row in board:
    square = row[3]
    if square == '*':
        # How to get row_no?

for r in range(6):
    square = board[r][3]
    if square == '*':
        # We have the row_no
        row_no = r
        # We found the square
        break
# What if there is no empty square?
else:
    # User entered a full column
    # Start over and get a new column