#!/usr/bin/python3
""" Perimeter of the island """


def island_perimeter(grid):
    """
    A function that returns the perimeter of the island

    Args:
        grid: list of list of integers

    Returns: integer
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    row = 1
    sides_count = []
    multiple_islands = []
    while row <= n_rows - 2:
        for col in range(1, n_cols - 2):
            if grid[row][col] == 1:
                up = grid[row - 1][col]
                down = grid[row + 1][col]
                left = grid[row][col - 1]
                right = grid[row][col + 1]
                total = up + down + left + right
                if total == 0:
                    multiple_islands.append(1)
                sides_count.append(4 - total)
        row += 1
    if len(multiple_islands) > 1:
        print(f" Error!! There are {len(multiple_islands)} island(s).")
        return
    else:
        perimeter = sum(sides_count)
        return perimeter
