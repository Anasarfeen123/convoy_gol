import numpy as np
import time, os

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

def rule_check(map):
    '''
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
    rows, cols = map.shape
    ex_map = map.copy()
    for x in range(0,rows):
        for y in range(0,cols):
            neighbors = adj_cell(x, y, map)
            if map[x, y] == "⬛" and neighbors == 3:
                ex_map[x, y] = "⬜"

            elif map[x, y] == "⬜":
                if neighbors < 2 or neighbors > 3:
                    ex_map[x, y] = "⬛"

    return ex_map


if __name__ == "__main__":
    # initial_live_cells = [[10,9], [10,10], [10,11]]
    initial_live_cells = [[1,2], [2,3], [3,1], [3,2], [3,3]]

    board = board_builder(initial_live_cells)
    print("Initial Generation:")
    for row in board:
        print(" ".join(row))
    print("---------------------------------------------------")

    while True:
        board = rule_check(board)
        for row in board:
            print(" ".join(row))
        print("---------------------------------------------------")
        time.sleep(0.5)