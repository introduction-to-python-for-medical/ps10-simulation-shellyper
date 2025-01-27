import copy
def spread_fire(grid):

    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
          if i == 0 and j == 0:
            neighbors = [grid[i+1][j],grid[i][j+1]]
            if 2 in neighbors:
                update_grid[i][j] = 2

          elif i == 0 and j == len(grid) - 1 :
            neighbors = [grid[i+1][j],grid[i][j-1]]
            if 2 in neighbors:
                update_grid[i][j] = 2

          elif i == len(grid) - 1  and j == 0:
            neighbors = [grid[i-1][j],grid[i][j+1]]
            if 2 in neighbors:
                update_grid[i][j] = 2

          elif i == len(grid) - 1 and j == len(grid) - 1:
            neighbors = [grid[i-1][j],grid[i][j-1]]
            if 2 in neighbors:
                update_grid[i][j] = 2

          elif i == 0:
              neighbors = [grid[i+1][j],grid[i][j-1],grid[i][j+1]]
              if 2 in neighbors:
                  update_grid[i][j] = 2

          elif i == len(grid) - 1:
              neighbors = [grid[i-1][j],grid[i][j-1],grid[i][j+1]]
              if 2 in neighbors:
                  update_grid[i][j] = 2

          elif j == 0:
              neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j+1]]
              if 2 in neighbors:
                  update_grid[i][j] = 2

          elif j == len(grid) - 1:
              neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1]]
              if 2 in neighbors:
                  update_grid[i][j] = 2

          elif grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2
    return update_grid
