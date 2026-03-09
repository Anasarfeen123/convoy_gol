import os
import numpy as np
import time
import board as bd
import rules as rls
import pygame as gui
gui.init()
gui.font.init()
font = gui.font.SysFont(None, 36)
info = gui.display.Info()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

RULE = "gol"
TITLE = "Conway's game of life"
CELL_SIZE = 20
BOARD_DIMENSIONS = (50,50)
BOARD_WIDTH_HEIGHT = (BOARD_DIMENSIONS[0] * CELL_SIZE, BOARD_DIMENSIONS[1] * CELL_SIZE)
SCREEN_WIDTH_HEIGHT = (info.current_w, info.current_h)
OFFSET = ((SCREEN_WIDTH_HEIGHT[0] - BOARD_WIDTH_HEIGHT[0]) // 2,(SCREEN_WIDTH_HEIGHT[1] - BOARD_WIDTH_HEIGHT[1]) // 2)
BGCOLOR = (40,40,40)
help_lines = [
"Esc   - Quit",
"Space - Play / Pause",
"Click - Toggle cell",
"1-8   - Change rule",
"When paused:",
"   R - Randomize board",
"   C - Clear board"
]

label_help_x = SCREEN_WIDTH_HEIGHT[0] - 300

screen = gui.display.set_mode(SCREEN_WIDTH_HEIGHT, gui.FULLSCREEN)
gui.display.set_caption(TITLE)
screen.fill(BGCOLOR)

def board_drawer(map, screen):
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == "⬜":
                a = age[row][col]
                r = min(255, 100 + a * 90)
                g = max(255, 255 - a * 10)
                b = min(255, a*30)
                color = (r, g, b)
            else:
                color = (0, 0, 0)

            x = col * CELL_SIZE + OFFSET[0]
            y = row * CELL_SIZE + OFFSET[1]
            gui.draw.rect(screen, color, gui.Rect(x, y, CELL_SIZE, CELL_SIZE))
    for i in range(BOARD_DIMENSIONS[0] + 1):
        x = OFFSET[0] + i * CELL_SIZE
        gui.draw.line(screen, (60, 60, 60), (x, OFFSET[1]), (x, OFFSET[1] + BOARD_WIDTH_HEIGHT[1]))

    for j in range(BOARD_DIMENSIONS[1] + 1):
        y = OFFSET[1] + j * CELL_SIZE
        gui.draw.line(screen, (60, 60, 60), (OFFSET[0], y), (OFFSET[0] + BOARD_WIDTH_HEIGHT[0], y))

age = np.zeros(BOARD_DIMENSIONS, dtype=int)
if __name__ == "__main__":
    running = True
    paused = True
    initial_live_cells = [[1,2], [2,3], [3,1], [3,2], [3,3]]
    board = bd.board_builder(initial_live_cells,BOARD_DIMENSIONS[0])
    
    board_drawer(board,screen)
    time.sleep(1)

    try:
        gen = 1
        while running:
            for event in gui.event.get():
                if event.type == gui.QUIT or (event.type == gui.KEYDOWN and event.key == gui.K_ESCAPE):
                    running = False
                
                if event.type == gui.KEYDOWN and event.key == gui.K_SPACE:
                    paused = not paused
                if event.type == gui.KEYDOWN:
                    if event.key == gui.K_1:
                        RULE = "gol"
                    elif event.key == gui.K_2:
                        RULE = "HighLife"
                    elif event.key == gui.K_3:
                        RULE = "DaynNight"
                    elif event.key == gui.K_4:
                        RULE = "seed"
                    elif event.key == gui.K_5:
                        RULE = "life_without_death"
                    elif event.key == gui.K_6:
                        RULE = "Maze"
                    elif event.key == gui.K_7:
                        RULE = "Replicator"
                    elif event.key == gui.K_8:
                        RULE = "34"
                        
                
                if event.type == gui.MOUSEBUTTONDOWN and paused:
                    mx, my = gui.mouse.get_pos()
                    grid_x = (mx - OFFSET[0]) // CELL_SIZE
                    grid_y = (my - OFFSET[1]) // CELL_SIZE
                    
                    if 0 <= grid_x < BOARD_DIMENSIONS[0] and 0 <= grid_y < BOARD_DIMENSIONS[1]:
                        if board[grid_y][grid_x] == "⬜":
                            board[grid_y][grid_x] = "⬛"
                            age[grid_y][grid_x] = 0
                        else:
                            board[grid_y][grid_x] = "⬜"
                            age[grid_y][grid_x] = 1
                if event.type == gui.KEYDOWN and paused:
                    if event.key == gui.K_r:
                        board = bd.random_board(BOARD_DIMENSIONS[0], count=100)
                        age[:] = 0

                    if event.key == gui.K_c:
                        board = bd.board_builder([], BOARD_DIMENSIONS[0])
                        age[:] = 0
            
            if not paused:
                label = font.render(f"{TITLE} [{RULE}] – Generation {gen}", True, (255, 255, 255))
                
                board_next = rls.rule_check(board, RULE)

                for y in range(BOARD_DIMENSIONS[1]):
                    for x in range(BOARD_DIMENSIONS[0]):
                        if board_next[y][x] == "⬜":
                            if board[y][x] == "⬜":
                                age[y][x] += 1      # survived
                            else:
                                age[y][x] = 1       # born
                        else:
                            age[y][x] = 0           # dead

                if np.array_equal(board, board_next):
                    paused = True
                board = board_next
                screen.fill(BGCOLOR)
                
                board_drawer(board, screen)
                
                gui.display.set_caption(f"{TITLE} [{RULE}] – Generation {gen}")
                gen += 1
                
                screen.blit(label, (20, 20))
                
                for i, line in enumerate(help_lines):
                    label_help = font.render(line, True, (255, 255, 255))
                    screen.blit(label_help, (label_help_x, 20 + i * 30))

                gui.display.flip()
                gui.time.delay(150)

            if paused:
                board_y = rls.rule_check(board, RULE)
                if np.array_equal(board, board_y):
                    label = font.render(f"Last Generation {gen}", True, (255, 255, 255))
                else:
                    label = font.render(f"Paused - Generation {gen}", True, (255, 255, 255))
                screen.fill(BGCOLOR)
                board_drawer(board, screen)
                screen.blit(label, (20, 20))
                for i, line in enumerate(help_lines):
                    label_help = font.render(line, True, (255, 255, 255))
                    screen.blit(label_help, (label_help_x, 20 + i * 30))
                gui.display.flip()

    except KeyboardInterrupt:
        print(f"Game terminated by user after {gen} generations.")