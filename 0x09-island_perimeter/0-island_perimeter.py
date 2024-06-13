#!/usr/bin/python3
"""island_perimeter module"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    grid is a list of list of integers:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        - grid is rectangular, with its width and height not exceeding 100
        - The grid is completely surrounded by water
        - There is only one island (or nothing).
        - The island doesn’t have “lakes” (water inside that isn’t connected to
        the water surrounding the island).
    """
    perimeter = 0
    height = len(grid)
    width = len(grid[0])

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 0:
                continue
            # top
            if i == 0 or grid[i - 1][j] == 0:
                perimeter += 1
            # right
            if j == width - 1 or grid[i][j+1] == 0:
                perimeter += 1
            # bottom
            if i == height - 1 or grid[i + 1][j] == 0:
                perimeter += 1
            # left
            if j == 0 or grid[i][j - 1] == 0:
                perimeter += 1

    return perimeter
