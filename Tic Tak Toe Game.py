def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def get_valid_move(board):
    while True:
        move = input("Enter your move (row col): ")
        if len(move) != 3 or not move[0].isdigit() or not move[2].isdigit() or move[1] != ' ':
            print("Invalid input. Please enter row and column numbers separated by space.")
            continue

        row, col = map(int, move.split())
        if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != ' ':
            print("Invalid move. Please enter a valid empty cell.")
            continue

        return row, col


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        row, col = get_valid_move(board)
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1


play_game()
