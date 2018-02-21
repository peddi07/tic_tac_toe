#from Ipython.display import clear_output
def display_board(board):
    clear_output()
    print("  |  |")
    print("" + board[7] + "|" + board[8] + "|" + board[9])
    print("  |  |")
    print("----------")
    print("  |  |")
    print("" + board[4] + "|" + board[5] + "|" + board[6])
    print("  |  |")
    print("----------")
    print("  |  |")
    print("" + board[1] + "|" + board[2] + "|" + board[3])
    print("  |  |")

def player_input():

    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("player 1: do you whnt to be X or O?").upper()

    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")

def place_marker(board,marker,position):
    board[position] = marker

def check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark))

import random
def initiate():
    if random.randint(0,1)==0:
        return "player 2"
    else:
        return "player 1"

def space_check(board,position):
    return board[position] ==" "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position =" "
    while position not in"1,2,3,4,5,6,7,8,9".split() or not space_check(board,int(position)):
        position = input("choose your nest position:(1-9)")
    return int(position)

def replay():
    return input("do you wantb to play again? Enter yes or No:").lower().startswith("y")

print("welcome to tic tac toe!")

while True:
    theBoard = [" "]*10
    player1_marker ,player2_marker = player_input()
    turn = initiate()
    print(turn + "will go first.")
    game_on = True

    while game_on:
        if turn =="player1":
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if check(theBoard,player1_marker):
                display_board(theBoard)
                print("congratulations! you have won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("the game is draw!")
                    break
                else:
                    turn = "player2"

        else:
            if turn =="player2":
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard,player1_marker,position)

                if check(theBoard,player1_marker):
                    display_board(theBoard)
                    print("congratulations! you have won the game!")
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print("the game is draw!")
                        break
                    else:
                        turn = "player1"

    if not replay():
        break
