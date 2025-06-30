import numpy as np
import time, os
import board as bd
import rules as rls


if __name__ == "__main__":
    # initial_live_cells = [[10,9], [10,10], [10,11]]
    # initial_live_cells = [[1,2], [2,3], [3,1], [3,2], [3,3]]
    
    # board = bd.board_builder(initial_live_cells)
    board = bd.random_board()
    print("Initial Generation:")
    for row in board:
        print(" ".join(row))
    print("---------------------------------------------------")

    try:
        gen = 1
        while True:
            # os.system('cls' if os.name == 'nt' else 'clear')
            board_y = rls.rule_check(board)
            if np.array_equal(board, board_y):
                break
            print(f"Genration: {gen}")
            board = board_y
            for row in board:
                print(" ".join(row))
            gen +=1
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Game terminated by user.")
