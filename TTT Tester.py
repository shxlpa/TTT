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
            '1': 'X' , '2': ' ' , '3': ' ' }

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

globalVar = 0

def simulate(board, currentTurn):
    boardCopy = dict(board)
    allBoards = []
    winningBoards = []
    i = -1
    globalVar += 1
    while i < len(allBoards): #some range??
        openSpot = ''

        for key in boardCopy: 
            '''this for loop generates two lists. one of them is a list of all possible boards; the other is a list of all winning boards.'''
            #still have to write code to update boardCopy
            if boardCopy[key]  == ' ':
                if openSpot == '':
                    openSpot = key
                    print("Trying openspot ", openSpot)
                boardCopy[key] = currentTurn
            #add new board to list
            allBoards += [boardCopy]
            if winLogic(boardCopy, currentTurn):
                winningBoards += boardCopy
            
            boardCopy[key] = ' ' #resets board --> THIS MAKES IT A FOREVER LOOP. HOW ELSE DO I RESET BOARD?

        #recurse
        if currentTurn == 'O': #logic to switch turns
            i += 1
            return simulate(allBoards[i], 'X')
        else:
            i += 1
            return simulate(allBoards[i], 'O')
    
    return winningBoards 


simulate(masterBoard, 'O')