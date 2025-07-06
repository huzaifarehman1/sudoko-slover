# solver.py

def solve(bo):
    find = FindEmptyPro(bo)  # we might be trying to solve an invalide board like one with 2 same num in same row etc so
    # i modify the this part and added findEmptyPro so it return false(2) for invalide one (0) if no empty and (i,j) for empty square
    if find==0:
        return True
    elif find==2:
        return False
    else:    
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def FindEmptyPro(bo):
    emp = None
    for i in range(9):
        rowseen = set()
        colseen = set()
        sqseen = set()
        
        for j in range(9):
            # Find the first empty cell
            if bo[i][j] == 0 and not emp:
                emp = (i, j)

            # Check for duplicates in row
            if bo[i][j] != 0:
                if bo[i][j] in rowseen:
                    return 2
                rowseen.add(bo[i][j])

            # Check for duplicates in column
            if bo[j][i] != 0:
                if bo[j][i] in colseen:
                    return 2
                colseen.add(bo[j][i])

            # Check for duplicates in 3x3 square
            rowIndex = 3 * (i // 3)
            colIndex = 3 * (i % 3)
            r = rowIndex + j // 3
            c = colIndex + j % 3
            if bo[r][c] != 0:
                if bo[r][c] in sqseen:
                    return 2
                sqseen.add(bo[r][c])

     # Return the first empty cell found, or None if board is full and valid
    if emp is None:
        return 0
    return emp