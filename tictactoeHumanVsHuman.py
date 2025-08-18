#Human vs Human
def print_board(board):
    print(f'\n{board[0]} | {board[1]} | {board[2]}')
    print('--+--+--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--+--+--')
    print(f'{board[6]} | {board[7]} | {board[8]}\n')

def is_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in winning_combinations)

def is_board_full(board):
    return '' not in board

def make_move(board, position, player):
    if board[position] == '':
        board[position] = player
        return True
    return False

def main():
    board = ['' for _ in range(9)]
    current_player = 'X'
    print("Welcome to Tic-Tac-Toe (Human vs Human)!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue
            if not make_move(board, move, current_player):
                print("This position is already taken. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print_board(board)

        if is_winner(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
