import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


import numpy as np
import time
import board as bd
import rules as rls
import pygame as gui

TITLE = "Conway's game of life"
CELL_SIZE = 20
BOARD_DIMENSIONS = (20,20)
BOARD_WIDTH_HEIGHT = (BOARD_DIMENSIONS[0] * CELL_SIZE, BOARD_DIMENSIONS[1] * CELL_SIZE)
SCREEN_WIDTH_HEIGHT = (1800,1000)
OFFSET = ((SCREEN_WIDTH_HEIGHT[0] - BOARD_WIDTH_HEIGHT[0]) // 2,(SCREEN_WIDTH_HEIGHT[1] - BOARD_WIDTH_HEIGHT[1]) // 2)

gui.init()

bgcolor = (40,40,40)
screen = gui.display.set_mode(SCREEN_WIDTH_HEIGHT)
gui.display.set_caption(TITLE)
screen.fill(bgcolor)



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
    paused = False
    
    # initial_live_cells = [[10,9], [10,10], [10,11]]
    # initial_live_cells = [[1,2], [2,3], [3,1], [3,2], [3,3]]
    # board = bd.board_builder(initial_live_cells)
    
    board = bd.random_board()
    
    board_drawer(board,screen)
    time.sleep(0.5)

    try:
        gen = 1
        while running:
            for event in gui.event.get():
                if event.type == gui.QUIT:
                    running = False
                if event.type == gui.KEYDOWN and event.key == gui.K_SPACE:
                    paused = not paused
            
            if not paused:
                board_y = rls.rule_check(board)
                if np.array_equal(board, board_y):
                    running = False
                board = board_y
                screen.fill(bgcolor)
                
                board_drawer(board, screen)
                
                gui.display.set_caption(TITLE + f" – Generation {gen}")
                gen += 1
                
                gui.display.flip()
                gui.time.delay(200)


    except KeyboardInterrupt:
        ...
        # print(f"Game terminated by user after {gen} generations.")

