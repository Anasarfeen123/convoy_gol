import numpy as np

def board_builder(lis:list):
    board = np.full([20,20],"⬛")
    for i in lis:
        add_cells(i[0],i[1],board)
    return board
    
def add_cells(x,y,map, mark="⬜"):
    map[x,y] = mark

def adj_cell(x,y,map):
    count = 0
    rows, cols = map.shape
    offsets = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    for dx, dy in offsets:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if map[nx, ny] == "⬜":
                count += 1
    return count