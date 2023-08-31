#!/usr/bin/python3

""" Function to find perimiter of an island """

def island_perimeter(grid):
    """
    Input: List of Lists
    Returns: Perimeter of the island
    """
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            is_valid_neighbor = [1 if k[0] in range(row) and k[1] in range(col) else 0
                               for k in neighbors]

            if grid[i][j]:
                count += sum([1 if not is_neighbor or not grid[k[0]][k[1]] else 0
                              for is_neighbor, k in zip(is_valid_neighbor, neighbors)])

    return count
