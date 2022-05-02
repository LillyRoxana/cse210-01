# REQUIREMENTS:
# The program must have at least one if/then block.
# The program must have at least one while loop.
# The program must have more than one function.
# The program must have a function called main.

def main():
    player = next_player("")
    board = new_board()
    while not (winner(board) or draw(board)):
        display_board(board)
        next_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Thanks for playing!") 

def new_board():
    board = []
    for value in range(9):
        board.append(value + 1)
    return board

def draw(board):
    for value in range(9):
        if board[value] != "x" and board[value] != "o":
            return False
    return True 

def display_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0],board[1], board[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3],board[4], board[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6],board[7], board[8]))
    print("     |     |")
    print("\n")


def next_move(player, board):
    value = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[value - 1] = player
    
    
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def next_player(now):
    if now == "" or now == "o":
        return "x"
    elif now == "x":
        return "o"

if __name__ == "__main__":
    main()

    
