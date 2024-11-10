def solve_sudoku(grid: list):
    sgrid = []
    
    for row in grid:
        new_row = []
        for space in row:
            new_row.append([space, []])
        sgrid.append(new_row)

    digits = [1,2,3,4,5,6,7,8,9]

    #traverse the sgrid and replace the empty list in the space[1] with possible numbers
    for i in range(9):
        for j in range(9):
            if sgrid[i][j][0] == 0:
                #now we know its empty, check col grid and square for missing numbers and replace x with them
                for digit in digits:
                    if digit not in get_square(grid,i,j) and digit not in get_row(grid,i) and digit not in get_col(grid, j):
                        sgrid[i][j][1].append(digit)

    #second traversal, if there is only one possibility we will place it as the answer
    for i in range(9):
        for j in range(9):
            if len(sgrid[i][j][1]) == 1:
                sgrid[i][j][0] = sgrid[i][j][1][0]

    #now switch back to a regular grid, so we can pass it out with one iteration solved:
    return_grid = []
    for row in sgrid:
        new_row = []
        for space in row:
            new_row.append(space[0])
        return_grid.append(new_row)

    return return_grid


corners = [[(0,0), (2,2)], [(0,3), (2,5)], [(0,6), (2,8)], [(3,0), (5,2)], [(3,3), (5,5)], [(3,6), (5,8)], [(6,0), (8,2)], [(6,3), (8,5)], [(6,6), (8,8)]]

def get_square(grid:list, i: int, j: int):
    target_square = [(0,0),(2,2)]
    for square in corners:
        if square[0][0] <= i <= square[1][0] and square[0][1] <= j <= square[1][1]:
            target_square = square

    square_list = []
    for i in range(target_square[0][0], target_square[1][0] + 1):
        for j in range(target_square[0][1], target_square[1][1] + 1):
            square_list.append(grid[i][j])
    return square_list
print('hello world')


def get_row(grid: list, i: int):
    return grid[i]

def get_col(grid: list, j: int):
    col_list = []
    for row in grid:
        col_list.append(row[j])
    return col_list

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

#print(get_square(grid, 1,6))
#print(get_row(grid,1))
#print(get_col(grid,1))
#print(solve_sudoku(grid))
#print(get_square(grid,3,4))

soln = grid
for i in range(10):
    soln = solve_sudoku(soln)



for row in soln:
    print(row)