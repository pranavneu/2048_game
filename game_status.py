'''
Pranav Kanth Anbarasan
CS5001, Spring 2023
Project
This program checks the status of the game and if any one of the numbers in
matrix equals to 2048 it will print 'You won!!' or if you are not able to
make any more moves and there is no space left it prints 'You lose' and ends
the game.
'''

def game_state_helper(matrix):
    '''
    This is a helper function for the game_state() and if the matrix is
    filled with numbers, then checks if any of the adjacent numbers are equal
    (left,right,up,down) and if it is same then the function returns True

    Parameters:
        matrix (nested list): contains the numbers in a nested list,
            example: [[0,0,0,8],[0,4,0,0],[2,0,4,8],[4,2,0,16]]

    Return:
        True (boolean): Returns True if the adjacent element is identical.

    Precondition: The inputted matrix should be a nested list.
    Postcondition: The object returned from the function is a boolean.
    '''

    row = len(matrix)
    for i in range(row):
        for j in range(row):
            # checking for each element
            element = matrix[i][j]
            # check the left side for same element
            if j > 0 and element == matrix[i][j - 1]:
                return True
            # check the right side
            if j < row - 1 and element == matrix[i][j + 1]:
                return True
            # check the element above
            if i > 0 and element == matrix[i - 1][j]:
                return True
            # check the element present below
            if i < row - 1 and element == matrix[i + 1][j]:
                return True

def game_state(matrix):
    '''
    This function checks if any of the number in the matrix equals to 2048 or
    if there is empty space in the matrix by checking for zero's, it also has
    the helper function to check if the adjacent elements are equal and
    returns the appropriate message depending on the scenario to the calling
    function

    Parameters:
        matrix (nested list): contains the numbers in a nested list,
            example: [[0,0,0,8],[0,4,0,0],[2,0,4,8],[4,2,0,16]].

    Return:
        (String): Returns the string depending on the scenario when
            a number 2048 is found in the matrix, it returns 'You won!!
            Congrats' ; if there is 0 in the matrix it returns 'Playing' ;
            if the matrix is filled with non-zero numbers and
            adjacent elements are equal returns 'Playing' else returns
            'You Lose!! Better Luck Next Time'.

    Helper_function : game_state_helper()

    Precondition: The inputted matrix should be a nested list.
    Postcondition: The function returns a string.
    '''

    # Check if any tile equals to 2048
    for row in matrix:
        if 2048 in row:
            return "You won!! Congrats"

    # check if any of the element in matrix is zero
    for row in matrix:
        if 0 in row:
            return 'Playing'

    # helper function call to check if adjacent elements are equal
    adjacent_elements = game_state_helper(matrix)
    if adjacent_elements == True:
        return 'Playing'
    else:
        return 'You Lose!! Better Luck Next Time'
