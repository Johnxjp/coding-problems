""" 
Solves a simpler version of the wedding dance floor problem simply returning
true if there is a solution and false otherwise.

We solve it with backtracking. But this implementation is 
suboptimal as it creates new grids on each recursive check.
"""

from typing import Tuple

test_cases = [((17, 4, 8), False), ((8, 4, 4), True)]

def build_start_grid(h: int, d: int, start_row: int, start_col: int) -> list[list[str]]:
    """ Need to represent dance floor and empty space. Represent empty space as '' """
    grid = []
    for i in range(h):
        row = []
        for j in range(h):
            row.append("")
        grid.append(row)

    for i in range(d):
        for j in range(d):
            grid[start_row + i][start_col + j] = "D"

    return grid

def solve(h: int, d: int, t: int) -> bool:
    """
    Attempts to solve the dance floor issue returning true if can solve and false otherwise. Let's try
    to solve this problem first then we can modify to solve returning the orientation.
    """

    # We can do a quick area check which is a necessary condition
    # If we can't fit tables neatly into area without space left over
    # then return false
    remaining_area = (h * h - d * d)
    if remaining_area % t:
        return False

    # +1 to include row and column
    for start_row in range(h - d + 1):
        for start_col in range(h - d + 1):
            start_grid = build_start_grid(h, d, start_row, start_col)
            
            if solver(start_grid, h, d, t, remaining_area):
                return True

    return False


def solver(current_grid: list[list[str]], h: int, d: int, t: int, remaining_area: int) -> bool:
    
    # base case, we have fit all tables in
    if remaining_area == 0:
        return True
    
    # Failed case. We have left over space and can't fit a table
    if remaining_area < t:
        return False
    
    # Run some algorithm
    # 1. loop through and look for empty spaces. Process them sequentially
    # 2. Try to place a table vertically or horizontally. We do this by modifying the grid
    # directly. Create new grid?
    # 3. Then we try to solve with new grid
    # 4. If we can't solve then reverse and try again.

    new_grid = current_grid  # should copy
    for row in range(h):
        for col in range(h):
            # Constraint. Either table or dance floor present
            if current_grid[row][col] != "":
                continue
            
            for orientation in ["h", "v"]:
                # Try placing horizontal or vertical
                # if cannot, then we will return the (current_grid, false)
                # if we can we will return (new_grid, true)
                new_grid, can_insert = insert_table(current_grid, row, col, t, orientation=="h")
                
                # fails to insert
                if not can_insert:
                    continue
            
                # solve
                remaining_area -= t 
                if solver(new_grid, h, d, t, remaining_area):
                    return True

                # undo
                new_grid = current_grid

                # don't bother changing orientation if table is a square i.e. 1xt = 1x1
                if t == 1:
                    continue
            

    return False
    

def insert_table(current_grid: list[list[str]], row: int, col: int, t: int, is_horizontal: bool) -> Tuple[list[list[str]], bool]:
    """ Probably should not be building new grid each time. Will take up a lot of space. Better to modify """
    new_grid = []
    h = len(current_grid)
    for row_index in range(h):
        new_grid_row = []
        for column_index in range(h):
            new_grid_row.append(current_grid[row_index][column_index])
        
        new_grid.append(new_grid_row)

    # Insert
    if is_horizontal:
        for i in range(t):
            
            # out of bounds
            if col + i >= h:
                return current_grid, False
            
            # run into obstacle
            if new_grid[row][col + i] != "":
                return current_grid, False
            
            new_grid[row][col + i] = "T"
    
    else:
        for i in range(t):

            if row + i >= h:
                return current_grid, False
            
            # run into obstacle
            if new_grid[row + i][col] != "":
                return current_grid, False

            new_grid[row + i][col] = "T"

    return new_grid, True


# def undo_insertion(current_grid: list[list[str]], row: int, col: int, t: int, is_horizontal: bool) -> list[list]


if __name__ == "__main__":
    print(solve(8, 4, 4))