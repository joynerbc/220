"""
Name: Brianna Joyner
lab10.py
"""

def build_board():
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return positions

def display_board(board):
    print("{0} | {1} | {2}".format(board[0], board[1], board[2]))
    print("{3} | {4} | {5}".format(board[3], board[4], board[5]))
    print("{6} | {7} | {8}".format(board[6], board[7], board[8]))

def fill_spot(board, pos, char):
    if board[pos-1] == 'x' or board[pos-1] == 'o':
        return
    else:
        board[pos-1] = char

def is_legal(board, pos):
    if board[pos-1] == 'x' or board[pos-1] == 'o':
        return False
    else:
        return True

def game_won(board):
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True

def game_over(board):
    acc = 0
    for i in board:
        if i == 'x' or i == 'o':
            acc = acc + 1

def play_game():
    build_board()
    display_board()
    fill_spot()
    is_legal()
    game_won()
    game_over()

def main():
    build_board()
    display_board()
    fill_spot()
    is_legal()
    game_won()
    game_over()
    play_game()
    pass

main()
