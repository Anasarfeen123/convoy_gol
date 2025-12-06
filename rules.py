import board as bd

def rule_check(map, rule ="gol"):
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
            if rule=="gol":
                if map[x, y] == "⬛" and neighbors == 3:
                    ex_map[x, y] = "⬜"

                elif map[x, y] == "⬜":
                    if neighbors < 2 or neighbors > 3:
                        ex_map[x, y] = "⬛"
            
            elif rule=="HighLife":
                if map[x, y] == "⬛" and (neighbors in [3, 6]) :
                    ex_map[x, y] = "⬜"
                elif map[x, y] == "⬜":
                    if neighbors < 2 or neighbors > 3:
                        ex_map[x, y] = "⬛"
            
            elif rule=="DaynNight":
                if map[x, y] == "⬛" and (neighbors in [3,6,7,8]) :
                    ex_map[x, y] = "⬜"
                elif map[x, y] == "⬜":
                    if neighbors not in [3,4,6,7,8]:
                        ex_map[x, y] = "⬛"
            
            elif rule=="seed":
                if map[x, y] == "⬛" and neighbors == 2:
                    ex_map[x, y] = "⬜"
                elif map[x, y] == "⬜":
                    ex_map[x, y] = "⬛"
            
            elif rule=="life_without_death":
                if map[x, y] == "⬛" and neighbors == 3:
                    ex_map[x, y] = "⬜"
            
            elif rule=="Maze":
                if map[x, y] == "⬛" and (neighbors in [3]) :
                    ex_map[x, y] = "⬜"
                elif map[x, y] == "⬜":
                    if neighbors not in [1,2,3,4,5]:
                        ex_map[x, y] = "⬛"
            
            elif rule=="Replicator":
                if map[x, y] == "⬛" and (neighbors in [1,3,5,7]) :
                    ex_map[x, y] = "⬜"
                elif map[x, y] == "⬜":
                    if neighbors not in [1,3,7,5]:
                        ex_map[x, y] = "⬛"
            
            elif rule=="34":
                if map[x, y] == "⬛" and (neighbors in [3,4]) :
                    ex_map[x, y] = "⬜"
                elif map[x, y] == "⬜":
                    if neighbors not in [3,4]:
                        ex_map[x, y] = "⬛"
            
    return ex_map