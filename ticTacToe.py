#Implementation of Two Player Tic-Tac-Toe game in Python.
#Sources: https://dev.to/jamesshah/the-classic-tictactoe-game-in-python-cpi
#         https://www.amazon.in/Automate-Boring-Stuff-Python-Programming-ebook/dp/B00WJ049VU/ref=as_li_ss_tl?crid=36GA0S183R1H9&keywords=automate+the+boring+stuff+with+python&qid=1573710172&sprefix=Automate+t,aps,372&sr=8-1&linkCode=sl1&tag=bytetales-21&linkId=365febe171431796e07d4419d0a621ca&language=en_IN
import random

# KEY:
# variable 'turn' holds string value X or O

'''We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move
    we will change the value according to player's choice of move.'''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' } #board is a dictionary. the initial keys to the dictionary are empty strings

board_keys = []

for key in theBoard:
    board_keys.append(key) #generates this list: ['7', '8', '9', '4', '5', '6', '1', '2', '3'] BUT WHY?

print(board_keys)
'''We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def winLogic(copyBoard, turn):
    value = False
    if copyBoard['7'] == copyBoard['8'] == copyBoard['9'] != ' ': # across the top # TURN WINNING LOGIC INTO A SEPARATE FUNCTION
        printBoard(copyBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")
        value = True
    elif copyBoard['4'] == copyBoard['5'] == copyBoard['6'] != ' ': # across the middle
        printBoard(copyBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")
        value = True
    elif copyBoard['1'] == copyBoard['2'] == copyBoard['3'] != ' ': # across the bottom
        printBoard(copyBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")
        value = True
    elif copyBoard['1'] == copyBoard['4'] == copyBoard['7'] != ' ': # down the left side
        printBoard(copyBoard)
        print(" **** " + turn + " won. ****")
        print("\nGame Over.\n")
        value = True
    elif copyBoard['2'] == copyBoard['5'] == copyBoard['8'] != ' ': # down the middle
        printBoard(copyBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")
        value = True
    elif copyBoard['3'] == copyBoard['6'] == copyBoard['9'] != ' ': # down the right side
        printBoard(copyBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")
        value = True
    elif copyBoard['7'] == copyBoard['5'] == copyBoard['3'] != ' ': # diagonal
        printBoard(copyBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")
        value = True
    elif copyBoard['1'] == copyBoard['5'] == copyBoard['9'] != ' ': # diagonal
        printBoard(copyBoard)
        print("\nGame Over.\n")
        print(" **** " + turn + " won. ****")
        value = True
    return value

#why isn't rank returning anything?
def rank(boardState, currentTurn):
    theBoardCopy = dict(boardState) #create a copy of theBoard dictionary
    for key in theBoardCopy:
        i = 1
        if theBoardCopy[key] == ' ':
            theBoardCopy[key] = currentTurn #assign random value, then check winLogic
            value2 = winLogic(theBoardCopy, currentTurn)
            # winLogic needs to return one of 3 values:
            # X wins
            # O wins
            # No one wins
            # In rank, check to see if there is a win, then check if the
            # winning party is the same as "currentTurn".  If so, this is the winning simulation
            print(value2)
            #print(i) #INDEX: EXACTLY WHICH SPOT IN THE DICTIONARY TO PLACE 'O'
            if value2 == True: #why doesn't this work as a base case?
                # Pick this spot IFF currentTurn
                print('WIN')
                return key #board_keys[i] would be ordered wrong 
            else:
                if currentTurn == 'O':
                    return rank(theBoardCopy, 'X')
                else:
                    return rank(theBoardCopy, 'O')
                #EDITS TO MAKE TOMORROW: Instead of printing lose, recurse.
                #this is where we call rank again, but we switch the turn. currentTurn = 'X' if 'O' and vice versa
        i += 1
        theBoardCopy = dict(boardState)
 
# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    for i in range(10): #iterate 9 times
        printBoard(theBoard)

        if turn == 'O': #if O's turn
            print("It's " + turn + "'s turn!")
            move = rank(theBoard, turn)
            #str(random.randint(1, 9))

        else:
            print("It's your turn," + turn + ".Move to which place?")
            move = input() #asks for numerical input from turn, so the random must be before this

        if theBoard[move] == ' ': #if dict[key] = empty, put x in place
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        # Because the min # after which someone can win is in 5 counted moves from both.
        if count >= 5:
            winLogic(theBoard, turn)

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
        for key in board_keys:
            theBoard[key] = " " #erases everything

        game()

if __name__ == "__main__":
    game()
