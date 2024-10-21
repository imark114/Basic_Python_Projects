# Tic-Tac-Toe: Create a simple Tic-Tac-Toe game using a list to represent the game board. Implement the game logic and allow players to take turns.

def create_board():
    return [[None] * 3 for _ in range(3)]

def print_board(board):
     for row in board:
        print(" | ".join(str(cell) if cell else " " for cell in row))
        print("-" * 9)

board = create_board()
print_board(board)