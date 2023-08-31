#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid.

    Args:
        grid (List[List[int]]): A 2D grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Define the neighboring indices
            neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]

            # Check if neighboring indices are within grid boundaries
            is_valid_neighbor = [1 if k[0] in range(row) and k[1] in range(col) else 0
                               for k in neighbors]

            if grid[i][j]:
                # Count edges by checking if neighbor is not part of island
                count += sum([1 if not is_neighbor or not grid[k[0]][k[1]] else 0
                              for is_neighbor, k in zip(is_valid_neighbor, neighbors)])

    return count
