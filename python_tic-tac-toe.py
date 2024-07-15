#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    position = int(position)
    board[position] = mark
    return board

# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def preBoard(position):
    if board[position] != ' ':
        return board[position]
    return str(position)

def printBoard():
    print('\n' +
    ' '+preBoard(1)+' | '+preBoard(2)+' | '+preBoard(3)+' \n' +
    ' --------- \n' +
    ' '+preBoard(4)+' | '+preBoard(5)+' | '+preBoard(6)+' \n' +
    ' --------- \n' +
    ' '+preBoard(7)+' | '+preBoard(8)+' | '+preBoard(9)+' \n')

# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
option = [1,2,3,4,5,6,7,8,9]
def validateMove(position):
    position = int(position)
    if position in option and board[position] == " ":
        return True
    return False

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    count = 0
    for list in winCombinations:
        for item in list:
            if board[item] == player:
                count += 1
        if count != 3:
            count = 0
        else:
            return True
    return False

# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for v in board.values():
        if v == ' ':
            return False 
    return True



#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('\nGame started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while True:
    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
# Validate the input
        try:
            validateMove(move)
        except ValueError:
            print("Error. Please enter a number.")
            continue
# Update the board
        if validateMove(move) == True:
            markBoard(move,currentTurnPlayer)
            printBoard()
# Check win or tie situation
            if checkWin(currentTurnPlayer) == True:
                print("Game over. " + currentTurnPlayer + " player won\n")
                gameEnded = True 
            elif checkFull() == True:
                print("Game over. It's a tie\n")
                gameEnded = True
# Switch user
            else:
                if currentTurnPlayer == 'X':
                    currentTurnPlayer = 'O'
                else:
                    currentTurnPlayer = 'X'
        elif int(move) not in option:
            print("Please enter a value between 1 to 9")
        else:
            print("Occupied. Please enter another value between 1 to 9")

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
    restart = input("Do you want to play again? Enter y/n: ")
    if restart == 'y'or restart == 'Y':
        print('\nGame started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')
        for k in board.keys():
            board[k] = ' '
        gameEnded = False
    else:
        print("Thank you for your participation.")
        gameEnded = True
        break