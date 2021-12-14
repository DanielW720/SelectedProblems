"""
Given a solvable 9x9 Sudoku grid, with 0s representing empty cells, solve the Sudoku.
"""

def valid_solution(grid):
    """
    Return true if grid is complete and valid, else return false.
    Args:
        grid (2D list): 9x9 grid.
    """
    valid_values = {i for i in range(1, 10)}
    
    # Check row
    for row in grid:
        if set(row) != valid_values: return False 
        
    # Check columns
    for i in range(9):
        current_column = []
        for j in range(9):
            current_column.append(grid[j][i])
        if set(current_column) != valid_values: return False
        
    # Check 3x3 blocks
    for i in range(0, 9, 3):
        current_3x9_block = grid[i:i+3]
        for j in range(0, 9, 3):
            current_block = current_3x9_block[0][j:j+3] + \
                            current_3x9_block[1][j:j+3] + \
                            current_3x9_block[2][j:j+3]
            if set(current_block) != valid_values: return False

    return True # Grid is valid


def find_block(grid, row_idx, col_idx):
    """
    Find and return the 3x3 block that coordinate (row_idx, col_idx) belongs to. 
    Block is returned as a flat list.
    Args:
        grid (2D list): 9x9 grid.
        row_idx: Index of the row.
        col_idx: Index of the column.
    """
    if row_idx in range(0,3):
        current_3_by_9_block = grid[0:3]
    elif row_idx in range(3, 6):
        current_3_by_9_block = grid[3:6]
    elif row_idx in range(6, 9):
        current_3_by_9_block = grid[6:9]
        
    if col_idx in range(0, 3):
        current_block = current_3_by_9_block[0][0:3] + \
                        current_3_by_9_block[1][0:3] + \
                        current_3_by_9_block[2][0:3]
    elif col_idx in range(3, 6):
        current_block = current_3_by_9_block[0][3:6] + \
                        current_3_by_9_block[1][3:6] + \
                        current_3_by_9_block[2][3:6]                                
    elif col_idx in range(6, 9):
        current_block = current_3_by_9_block[0][6:9] + \
                        current_3_by_9_block[1][6:9] + \
                        current_3_by_9_block[2][6:9]
    return current_block


def sudoku(grid):
    """
    Assuming grid is determinable; i.e., solvable without the need of "guessing" a solution. 
    Returns solved puzzle.
    Args:
        grid (2D list): 9x9 grid.
    """
    not_solved = True
    while not_solved:
        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                if cell == 0: # Choose an empty cell
                    
                    # Gather all values that are occupied to a set
                    occupied = set() 
                    
                    # Add occupied values from current row
                    for cell_on_same_row in row:
                        if cell_on_same_row != 0: occupied.add(cell_on_same_row)
                    
                    # Add occupied values from current column
                    for ith_row in grid:
                        if ith_row[col_idx] != 0: occupied.add(ith_row[col_idx])
                    
                    # Find current block
                    current_block = find_block(grid, row_idx, col_idx)
                    
                    # Add occupied values from current block
                    for c in current_block:
                        if c != 0: occupied.add(c)
                    
                    # If exactly one non-zero digit is missing, there is no ambiguity regarding what value cell should be
                    if len(occupied) == 8:
                        grid[row_idx][col_idx] = {x for x in range(1, 10) if x not in occupied}.pop()
                        break # Start outer for loop again to check if previous cells can be solved
        
        # Check if grid has been solved
        not_solved = not valid_solution(grid)
    return grid


def print_grid(grid):
    """ Print the Sudoku grid.
    Args:
        grid (2D list): 9x9 grid.
    """
    for row in grid:
        print(row)


# Example from codewars.com
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

solved = sudoku(grid)
# Should return:
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]

print_grid(solved)
