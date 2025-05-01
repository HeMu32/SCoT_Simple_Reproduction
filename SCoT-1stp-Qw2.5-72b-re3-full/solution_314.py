def max_sum_rectangular_grid(grid):
    if not grid or not grid[0]:
        return 0

    n = len(grid[0])
    prev, curr = 0, 0

    for i in range(n):
        temp = curr
        # Calculate the maximum sum for the current column
        curr = max(prev + max(grid[0][i], grid[1][i]), curr)
        # Update prev to the old curr
        prev = temp

    return curr