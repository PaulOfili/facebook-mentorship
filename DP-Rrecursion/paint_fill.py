def paint_fill(grid, x, y, new_color):
    old_color = grid[x][y]

    def paint_fill_util(new_x, new_y):
        grid[new_x][new_y] = new_color

        for x1, y1 in [(new_x+1, new_y), (new_x-1,y), (new_x, new_y+1), (new_x, new_y-1)]:
            if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] == old_color:
                paint_fill_util(x1, y1)

        return

    if old_color != new_color:
        paint_fill_util(x,y)

    print(grid)


arr = [[1,1,1,1,1],
       [1,1,1,1,1],
       [1,0,0,1,1],
       [1,2,2,2,2],
       [1,1,1,2,2]]

new_color = 3

x = 4
y = 4

paint_fill(arr,x,y,new_color)