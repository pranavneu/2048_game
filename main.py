'''
Pranav Kanth Anbarasan
CS5001, Spring 2023
Project
This is the main program that gets the board size from the user and raises
an error if an invalid input is entered. It then calls all the other
functions to start the game.
'''

# importing all the required files for the main()
from matrix import *
from turtle_screen import *
from turtle_controls import *


def board_size():
    '''
    This function gets the input from the user as an integer between
    4 and 6, if an invalid input is entered an error is raised.

    Parameter:
        none

    Return:
        size (int): the size of the board

    Raises:
        ValueError: If input not between 2 and 6 or not an integer raises a
            value error.

    Postcondition: the returned size must be an integer between 2 and 6.
    '''
    # keep asking for input until a valid one is entered
    while True:
        try:
            size = int(input('Enter the size of the row or column, from 4 to 6:'))
            # conditional statement to check if the number is btn 4 to 6
            if size < 4 or size > 6:
                raise ValueError('Please enter a number between 4 to 6')
            return size
        except ValueError as msg:
            print(msg)

def main():

    # function calls to resume the game
    size = board_size()
    matrix = initialising_matrix(size)
    matrix = game_start(matrix, 2, size)
    # initialising score as 0
    score = 0
    draw_board(matrix, size, score)
    controls(matrix, size, score)
    turtle.done()

main()

