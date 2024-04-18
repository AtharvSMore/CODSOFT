def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_draw(board)

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -10 + depth, None
    elif is_winner(board, 'O'):
        return 10 - depth, None
    elif is_draw(board):
        return 0, None

    if maximizing_player:
        best_score = float('-inf')
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            score, _ = minimax(board, depth+1, False)
            board[move[0]][move[1]] = ' ' # Undo move
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            score, _ = minimax(board, depth+1, True)
            board[move[0]][move[1]] = ' ' # Undo move
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    player = input("Do you want to be X or O? ").upper()
    if player not in ['X', 'O']:
        print("Invalid choice. Please choose either 'X' or 'O'.")
        return

    print("You are", player)
    if player == 'X':
        ai = 'O'
    else:
        ai = 'X'
        print("AI will make the first move.")

    while not game_over(board):
        if len(available_moves(board)) == 0:
            break
        if player == 'O':
            score, move = minimax(board, 0, True)
            board[move[0]][move[1]] = ai
            print("AI makes move:", move)
            print_board(board)
            if game_over(board):
                break

        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if (row, col) in available_moves(board):
                    board[row][col] = player
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input, please enter a number.")

        print_board(board)

        if not game_over(board):
            if player == 'X':
                score, move = minimax(board, 0, True)
                board[move[0]][move[1]] = ai
                print("AI makes move:", move)
                print_board(board)

    if is_winner(board, player):
        print("Congratulations! You win!")
    elif is_winner(board, ai):
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()

