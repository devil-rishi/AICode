import random

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
    print("Welcome to Tic-Tac-Toe (You vs Computer)!")
    print_board(board)

    while True:
        try:
            human_move = int(input("Enter your move (1-9): ")) - 1
            if human_move < 0 or human_move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            if not make_move(board, human_move, 'X'):
                print("This position is already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print_board(board)

        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        computer_move = get_computer_move(board)
        make_move(board, computer_move, 'O')
        print_board(board)

        if is_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
