#!/usr/bin/python3
""" Perimeter of the island """


def island_perimeter(grid):
    """
    A function that returns the perimeter of the island

    Argument:
    grid: list of list of integers

    Returns: integer
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    row = 1
    sides_count = []
    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == 1:
                up = grid[row - 1][col]
                down = grid[row + 1][col]
                left = grid[row][col - 1]
                right = grid[row][col + 1]
                total = up + down + left + right
                sides_count.append(4 - total)
        row += 1
    perimeter = sum(sides_count)
    return perimeter

if __name__ == '__main__':
    island_perimeter(grid)
