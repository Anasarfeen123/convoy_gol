import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import numpy as np
import time
import board as bd
import rules as rls
import pygame as gui

gui.init()
gui.font.init()
font = gui.font.SysFont(None, 36)
info = gui.display.Info()

TITLE = "Conway's game of life"
CELL_SIZE = 20
BOARD_DIMENSIONS = (50,50)
BOARD_WIDTH_HEIGHT = (BOARD_DIMENSIONS[0] * CELL_SIZE, BOARD_DIMENSIONS[1] * CELL_SIZE)
SCREEN_WIDTH_HEIGHT = (info.current_w, info.current_h)
OFFSET = ((SCREEN_WIDTH_HEIGHT[0] - BOARD_WIDTH_HEIGHT[0]) // 2,(SCREEN_WIDTH_HEIGHT[1] - BOARD_WIDTH_HEIGHT[1]) // 2)
BGCOLOR = (40,40,40)
help_lines = [
"Esc - Quit",
"When paused:",
"       R - Randomize board",
"       C - Clear board"
]
label_help_x = SCREEN_WIDTH_HEIGHT[0] - 300

screen = gui.display.set_mode(SCREEN_WIDTH_HEIGHT, gui.FULLSCREEN)
gui.display.set_caption(TITLE)
screen.fill(BGCOLOR)

def board_drawer(map, screen):
    for row in range(len(map)):
        for col in range(len(map[0])):
            color = (255, 255, 255) if map[row][col] == "⬜" else (0, 0, 0)
            x = col * CELL_SIZE + OFFSET[0]
            y = row * CELL_SIZE + OFFSET[1]
            gui.draw.rect(screen, color, gui.Rect(x, y, CELL_SIZE, CELL_SIZE))
    for i in range(BOARD_DIMENSIONS[0] + 1):
        x = OFFSET[0] + i * CELL_SIZE
        gui.draw.line(screen, (60, 60, 60), (x, OFFSET[1]), (x, OFFSET[1] + BOARD_WIDTH_HEIGHT[1]))

    for j in range(BOARD_DIMENSIONS[1] + 1):
        y = OFFSET[1] + j * CELL_SIZE
        gui.draw.line(screen, (60, 60, 60), (OFFSET[0], y), (OFFSET[0] + BOARD_WIDTH_HEIGHT[0], y))


if __name__ == "__main__":
    running = True
    paused = True
    
    # initial_live_cells = [[10,9], [10,10], [10,11]]
    initial_live_cells = [[1,2], [2,3], [3,1], [3,2], [3,3]]
    board = bd.board_builder(initial_live_cells,BOARD_DIMENSIONS[0])
    
    # board = bd.random_board()
    
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
                
                if event.type == gui.MOUSEBUTTONDOWN and paused:
                    mx, my = gui.mouse.get_pos()
                    grid_x = (mx - OFFSET[0]) // CELL_SIZE
                    grid_y = (my - OFFSET[1]) // CELL_SIZE
                    if 0 <= grid_x < BOARD_DIMENSIONS[0] and 0 <= grid_y < BOARD_DIMENSIONS[1]:
                        board[grid_y][grid_x] = "⬛" if board[grid_y][grid_x] == "⬜" else "⬜"
                
                if event.type == gui.KEYDOWN and paused:
                    if event.key == gui.K_r:
                        board = bd.random_board(BOARD_DIMENSIONS[0], count=100)
                    if event.key == gui.K_c:
                        board = bd.board_builder([], BOARD_DIMENSIONS[0])
            
            if not paused:
                label = font.render(f"Running - Generation {gen}", True, (255, 255, 255))
                board_y = rls.rule_check(board)
                if np.array_equal(board, board_y):
                    paused = True
                board = board_y
                screen.fill(BGCOLOR)
                
                board_drawer(board, screen)
                
                gui.display.set_caption(TITLE + f" – Generation {gen}")
                gen += 1
                
                screen.blit(label, (20, 20))
                
                for i, line in enumerate(help_lines):
                    label_help = font.render(line, True, (255, 255, 255))
                    screen.blit(label_help, (label_help_x, 20 + i * 30))

                gui.display.flip()
                gui.time.delay(150)

            if paused:
                board_y = rls.rule_check(board)
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