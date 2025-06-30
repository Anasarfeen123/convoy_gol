import board as bd

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
            neighbors = bd.adj_cell(x, y, map)
            if map[x, y] == "⬛" and neighbors == 3:
                ex_map[x, y] = "⬜"

            elif map[x, y] == "⬜":
                if neighbors < 2 or neighbors > 3:
                    ex_map[x, y] = "⬛"

    return ex_map