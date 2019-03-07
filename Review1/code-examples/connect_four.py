"""
Koc University, Turkey
KOLT Python Certificate Program
Spring 2019 - Assignment 1
Created by @ahmetuysal
"""

print('Welcome to two player Connect Four game!')
print('This a two player game played on a seven-column, six-row board.')

# empty squares are denoted with *
board = [
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*']]

players = []
player_pieces = []

# Take player names


# Take player piece symbols
# Symbols need be unique and have length 1 
# They should also be different than '*'
print('\'*\' symbol is reserved to denote empty squares.')


# Print the initial board

# Loop for game
for move_counter in range(42):  # Why 42? 
    # Take user input for column_no   

    # Check whether this is a valid move
    # It needs to be an integer, hint: use str.isnumeric()
    # It needs to be in range [0, 6] inclusive
    # And the selected column cannot be full
    # You need to ask for new column_no until user enters a valid one

    # Play the move

    # Print the current board

    # Check whether the game is finished
    game_ended = False
   
    # Print the winner and number of moves if game is finished
    # The game should stop at this point if game is finished


# this else block only runs if condition on while loop becomes false
# it is not executed if loop is terminated by a break statement
# i.e when all 42 moves are played without a break statement
else:
    print('There no other legal moves, game is ended in a draw.')
