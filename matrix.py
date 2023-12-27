'''
Pranav Kanth Anbarasan
CS5001, Spring 2023
Project
This program creates a matrix filled with 0's for the input size
the user has entered. It then inputs two random numbers (2,4) on
random places at the start of the game and then input one random
number (2,4) after each move the player made.
'''

# importing the random module
import random

def initialising_matrix(size):
    '''
    This function creates a matrix that contains the same number of columns
    rows as specified in the size parameter filled with zeros. It then
    returns the matrix to the calling function.
    Parameter:
        size (int): the size of the matrix and board

    Return:
        matrix (nested list): contains the numbers in a nested list, example:
        [[0,0,0,8],[0,0,0,0],[0,0,0,0], [0,0,0,0]].

    Precondition: The input parameter size must be an integer.
    Postcondition: The returned matrix should be a nested list
    '''
    # creating an empty matrix
    matrix = []
    for element in range(size):
        # creating entire column filled with zero for given size
        matrix.append([0] * size)
    return matrix

def game_start(matrix, limit, board_size):
    '''
    This function is used to generate random numbers (2,4) each time and
    append it to matrix at random places. The limit parameter specifies
    how many random numbers should be appended each time in the matrix.
    Parameters:
        matrix (nested list): contains the numbers in a nested list, example:
        [[0,0,0,8],[0,4,0,0],[2,0,4,8], [4,2,0,16]].

        limit (int): The number of random elements (2,4) to be added to the
            matrix.

        board_size (int): the size of the matrix and board

    Return:
        matrix (nested list): contains the numbers in a nested list, example:
        [[0,0,0,8],[0,4,0,0],[2,0,4,8], [4,2,0,16]].

    Precondition: the matrix is a nested list, whereas limit and board size
        are integers.
    Postcondition: The returned matrix is a nested list.
    '''
    count = 0
    while count < limit:
        # generating random column number
        column = random.randint(0, board_size - 1)
        # generating random row number
        row = random.randint(0, board_size - 1)
        # if the column,row in matrix is filled with zero proceed
        if matrix[column][row] == 0:
            # insert random element (2,4)
            matrix[column][row] = random.choice([2, 4])
            count += 1
    return matrix

