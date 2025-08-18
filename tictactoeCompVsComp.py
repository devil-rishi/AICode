import random
import time

def print_board(board):
    print(f'\n{board[0]} | {board[1]} | {board[2]}')
    print('--+--+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+--+--')
    print(f'{board[6]} | {board[7]} | {board[8]}\n')

def is_winner(board, player):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in winning_combinations)

def is_board_full(board):
    return '' not in board

def make_move(board, position, player):
    if board[position] == '':
        board[position] = player
        return True
    return False

def get_computer_move(board):
    available_positions = [i for i, spot in enumerate(board) if spot == '']
    return random.choice(available_positions)

def main():
    board = ['' for _ in range(9)]
    print("Welcome to Tic-Tac-Toe (Computer vs Computer)!")
    print("Computer X vs Computer O")
    print_board(board)
    time.sleep(1)

    while True:
        print("Computer X's turn...")
        computer_move = get_computer_move(board)
        make_move(board, computer_move, 'X')
        print_board(board)
        
        if is_winner(board, 'X'):
            print("Computer X wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break
        time.sleep(1)

        print("Computer O's turn...")
        computer_move = get_computer_move(board)
        make_move(board, computer_move, 'O')
        print_board(board)
        
        if is_winner(board, 'O'):
            print("Computer O wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        time.sleep(1)

if __name__ == "__main__":
    main()
