import board as bd

RULES = {
    "gol":              ( {3},          {2, 3} ),
    "HighLife":         ( {3, 6},       {2, 3} ),
    "DaynNight":        ( {3, 6, 7, 8}, {3, 4, 6, 7, 8} ),
    "seed":             ( {2},          set() ),
    "life_without_death": ({3},         set(range(9)) ),
    "Maze":             ( {3},          {1, 2, 3, 4, 5} ),
    "Replicator":       ( {1, 3, 5, 7}, {1, 3, 5, 7} ),
    "34":               ( {3, 4},       {3, 4} ),
}

DEAD = "⬛"
ALIVE = "⬜"
def rule_check(grid, rule="gol"):
    rows, cols = grid.shape
    new_grid = grid.copy()
    birth, survive = RULES[rule]

    for x in range(rows):
        for y in range(cols):
            n = bd.adj_cell(x, y, grid)
            cell = grid[x, y]

            if cell == DEAD and n in birth:
                new_grid[x, y] = ALIVE
            elif cell == ALIVE and n not in survive:
                new_grid[x, y] = DEAD

    return new_grid
