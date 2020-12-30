# Implementation of Two Player Tic-Tac-Toe game in Python.
# Sources: https://dev.to/jamesshah/the-classic-tictactoe-game-in-python-cpi
import random
import sys

# KEY:
# variable 'turn' holds string value X or O

'''We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move
    we will change the value according to player's choice of move.'''

# board is a dictionary. the initial keys to the dictionary are empty strings
masterBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

boardKeys = []

for key in masterBoard:
    # generates this list: ['7', '8', '9', '4', '5', '6', '1', '2', '3'] BUT WHY?
    boardKeys.append(key)

print(boardKeys)
'''We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def winLogic(board, turn):
    value = False
    if board['7'] == board['8'] == board['9'] != ' ': # across the top # TURN WINNING LOGIC INTO A SEPARATE FUNCTION
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    return value


# Returns winner and position that will cause the win
def simulate(board, currentTurn):
    boardCopy = dict(board) #create a copy of masterBoard dictionary
    print("Running simulation on ")
    printBoard(boardCopy)

    openSpot = ''
    for key in boardCopy:
        if boardCopy[key]  == ' ':
            if openSpot == '':
                openSpot = key
                print("Trying openspot ", openSpot)

            boardCopy[key] = currentTurn

            if winLogic(boardCopy, currentTurn):
                # Base case, win found
                print('WIN by ', currentTurn, " at ", key)
                return currentTurn, key
            else:
                # Recursive case
                if currentTurn == 'O':
                    winner, pos  = simulate(boardCopy, 'X')
                else:
                    winner, pos = simulate(boardCopy, 'O')

                if winner != '':
                    # There is a winner... we need to take that spot.  If it
                    # is currentTurn, we will win.  Else we will block the
                    # opponent.
                    return winner, pos

            # Iterative case... Try the next position in the board.
            print("Resetting Board")
            boardCopy[key] = ' '

    # If we get here, there was no winner
    # if openSpot == '', then the board was full
    if openSpot == '':
        print("Board full")
    else:
        print("No win for ", currentTurn, "... Returning ", openSpot)
    return '', openSpot

# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    for i in range(10): #iterate 9 times
        printBoard(masterBoard)

        if turn == 'O': #if O's turn
            print("It's " + turn + "'s turn!")
            winner, move = simulate(masterBoard, turn)
            if winner != '':
                print("Simulate detected that ", winner, " will win at ", move)
        else:
            print("It's your turn, " + turn + ". Move to which place?")
            move = input()

        if masterBoard[move] == ' ': #if dict[key] = empty, put x in place
            masterBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        # Because the min # after which someone can win is in 5 counted moves from both.
        if count >= 5:
            if winLogic(masterBoard, turn):
                print("Gane Over.  ", turn, " Won!")
                sys.exit()


        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("Game Over. It's a Tie!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in boardKeys:
            masterBoard[key] = " " #erases everything

        game()

if __name__ == "__main__":
    game()
