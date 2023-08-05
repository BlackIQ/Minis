import termcolor as tc
import itertools

PLAYER1 = "red"
PLAYER2 = "blue"

# if want to add feature then make so can chose the amount of numbers and the sum

# functions to play the game
def turn(player, board):
    if player == PLAYER1:
        tc.cprint("Player 1 turn", "red")
    elif player == PLAYER2:
        tc.cprint("Player 2 turn", "blue")
        
    num = input("enter number between 1 and 9: ")
    # check if number is valid
    if num.isdigit() and int(num) in range(1, 10):
        num = int(num)
        if board[num] == " ":
            board[num] = player
        else:
            print("This number is already taken!")
            turn(player, board)
    else:
        print("Invalid number!")
        turn(player, board)


def sum_nums(board):
    """
    get sum of numbers on the board
    Args:
        board (dict): the board
    """
    sum1 = 0
    sum2 = 0
    for key, value in board.items():
        if value == PLAYER1:
            sum1 += key
        elif value == PLAYER2:
            sum2 += key
    return sum1, sum2


def check_win(board:dict):
    """
    check if one of the players has a sum of 15 in the numbers 
    Args:
        board (dict): the board of the game 
    """
    sum1, sum2 = sum_nums(board)
    
    c1, c2 = check_lose(board, sum1, sum2)
    # check winner
    if sum1 == 15 or sum2 > 15 or not c2:
        return "player 1 wins!"
    elif sum2 == 15 or sum1 > 15 or not c1:
        return "player 2 wins!"
    # check if all values in beard are filled
    for value in board.values():
        if value == " ":
            return None
    
    
    return "draw"
        

def print_board(board):
    """
    print the board 
    Args:
        board (dict): the board of the game 
    """
    print("\nboard:\n------------------")
    for key, value in board.items():
        if value == " ":
            tc.cprint(str(key), "grey", end = " ")
        elif value == PLAYER1:
            tc.cprint(str(key), "red", end = " ") 
        elif value == PLAYER2:
            tc.cprint(str(key), "blue", end = " ")
        
    print("\n------------------")
    
    sum1, sum2 = sum_nums(board)
    tc.cprint("Player 1 sum: {}".format(sum1), "red")
    tc.cprint("Player 2 sum: {}\n".format(sum2), "blue")


def find_iters(board):
    """
    find all possible combinations of numbers to add to get to 15
    Args:
        board (dict): the board
    """
    # get all possible combinations of numbers to add to get to 15
    for i in range(1, 10):
        for j in range(i+1, 10):
            for k in range(j+1, 10):
                for l in range(k+1, 10):
                    if i + j + k + l == 15:
                        print("[{}, {}, {}, {},],".format(i, j, k, l))


def check_combows(sum_nums, arr):
    sequences = []
    for i in range(len(arr)):
        for j in itertools.combinations(arr, i):
            sequences.append(j)
    sec = []
    for i in sequences:
        if sum(i) + sum_nums == 15:
            sec.append(i)
    return sec


def check_lose(board, sum1, sum2):
    """
    check if a player can not get to 15 with the remaining numbers on the board
    Args:
        board (dict): the board
    """
    # get sum of " " values
    remain_sum = []
    
    for key, value in board.items():
        if value == " ":
            remain_sum.append(key)
    # check if player can not get to 15 with the remaining numbers on the board
    c1 = check_combows(sum1, remain_sum)
    print("\n")
    c2 = check_combows(sum2, remain_sum)
    
    return c1, c2



board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
win = False

# welcome and instructions
print("Welcome to the game of 15!")
tc.cprint("player one is red", "red", end="\t")
tc.cprint("and player two is blue", "blue")
tc.cprint("\n  the goal of the game is to get to 15 with the remaining numbers on the board\n  or to block the other player from getting to 15", "yellow")

# game loop
while (not win):
    print_board(board)
    turn(PLAYER1, board)
    win = check_win(board)
    
    if not win:
        print_board(board)
        turn(PLAYER2, board)
        win = check_win(board)

print_board(board)
print("\n", win)
