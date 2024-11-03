from random import randint

def choose_first()->str:
    flip = randint(0,1)
    return 'Player1' if flip == 0 else 'Player2'

def display_board(board:list)->None:
    print(board[7]+'|'+ board[8]+'|' + board[9])
    print(board[4]+'|'+ board[5]+'|' + board[6])
    print(board[1]+'|'+ board[2]+'|' + board[3])

def player_input()->tuple:
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player1, Choose (X or O): ").upper()
        if marker not in ['X', 'O']:
            print("Invalid Choiche.")
    player1 = marker
    player2 = 'O' if player1 == 'X' else 'X'
    return (player1, player2)

def marker_place(board:list, marker:str, position:int)->None:
    board[position] = marker

def win_check(board:list, mark: str)->bool:
    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2]==board[4] == board[6] == mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark)

def space_check(board: list, position: int)->bool:
    return board[position] == ' '

def full_board_check(board:list)->bool:
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choiche(board: list)->int:
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9): "))
        if position not in [1,2,3,4,5,6,7,8,9]:
            print("Invalid position")
    return position

def reply()->bool:
    choiche = ''
    while choiche not in ['Y', 'N']:
        choiche = input("Do you want to play again? (Y / N): ").upper()
    return choiche == 'Y'

if __name__ == "__main__":
    print("Welcom to Tic Tac Toe!")
    while True:
        # Play The game
        # Set everyting up (Board, Whos First, Choose marker X, 9)
        game_board = [' ']*10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first')
        play_game = input("Ready to play? (Y / N): ").upper()
        if play_game == 'Y':
            game_on = True
        elif play_game == 'N':
            game_on = False
        else:
            print("Invalid Choice, Pleasee input (Y / N)")
        
        while game_on:
            if turn == 'Player1':
                print("Player 1 Turn")
                # Show the board
                display_board(game_board)
                # Choosing Positon
                position = player_choiche(game_board)
                # Place the marker on the position
                marker_place(game_board,player1_marker,position)
                # Check win
                if win_check(game_board,player1_marker):
                    display_board(game_board)
                    print("Player1 has own!!")
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board()
                        print("Tie Game!")
                        game_on = False
                    else:
                        turn = "Player2"

            else:
                print("Player 2 Turn")
                # Show the board
                display_board(game_board)
                # Choosing Positon
                position = player_choiche(game_board)
                # Place the marker on the position
                marker_place(game_board,player2_marker,position)
                # Check win
                if win_check(game_board,player2_marker):
                    display_board()
                    print("Player2 has own!!")
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("Tie Game!")
                        game_on = False
                    else:
                        turn = "Player1"
                        
        if not reply():
            break