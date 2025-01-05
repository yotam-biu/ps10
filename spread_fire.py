def spread_fire(grid):

    grid_size_y = len(grid)
    grid_size_x = len(grid[0])
    
    update_grid = [[grid[i][j] for j in range(grid_size_x)] for i in range(grid_size_y)]
    for i in range(grid_size_y-1):      
        for j in range(grid_size_x-1):
            if grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2 
                
    return update_grid
