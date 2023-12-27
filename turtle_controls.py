'''
Pranav Kanth Anbarasan
CS5001, Spring 2023
Project
This Program uses the turtle module to get the predefined inputs
(Left, Right, Up or Down) and call the relevant merge functions
for that input and displays the matrix in the turtle window.
'''

# importing all the necessary files
from merge_matrix import *
from matrix import *
from turtle_screen import *
from game_status import *

def controls(matrix, board_size, score):
    '''
    This functions waits for the user to enter the relevant functions
    in the turtle window and calls the appropriate function nested within
    this block.

    Parameters:
        matrix (nested list): matrix (nested list): contains the numbers in
         a nested list, example: [[0,0,0,8],[0,4,0,0],[2,0,4,8],[4,2,0,16]]

        board_size (int): the size of the board

        Score (int): initialised as 0

    Return:
        none

    Precondition: The matrix should be a nested list and board_size,
        score are integers
    '''


    def move_right():
        '''
        This function is called if the right arrow key is pressed. This
        function then calls the merge_right() to perform the merge operation
        and updates the score. It then calls the draw() to display the matrix
        in the turtle window. After that, it checks the status of the game and
        if the game is over displays the appropriate message in the turtle
        window by calling the rules()

        Parameter:
            none

        Return:
            none
        '''
        # making the variables non-local
        nonlocal matrix
        nonlocal score
        # calling the merge_right() to get the resultant matrix and point
        merged_matrix, point = merge_right(matrix)
        # adding the point to score
        score += point

        # if merged_matrix isn't same as matrix add a new random element
        if matrix != merged_matrix:
            matrix = game_start(merged_matrix, 1, board_size)
            # display them in the turtle window
            draw_board(matrix, board_size, score)
            # check the game status
            game_status = game_state(matrix)
            if game_status != 'Playing':
                rules(game_status)

    def move_left():
        '''
        This function is called if the left arrow key is pressed. This
        function then calls the merge_left() to perform the merge operation
        and updates the score. It then calls the draw() to display the matrix
        in the turtle window. After that, it checks the status of the game and
        if the game is over displays the appropriate message in the turtle
        window by calling the rules()

        Parameter:
            none

        Return:
            none
        '''
        nonlocal matrix
        nonlocal score
        # calling the merge_left()
        merged_matrix, point = merge_left(matrix)
        score += point
        if matrix != merged_matrix:
            matrix = game_start(merged_matrix, 1, board_size)
            # display them in the turtle window
            draw_board(matrix, board_size, score)
            # game status check
            game_status = game_state(matrix)
            if game_status != 'Playing':
                rules(game_status)

    def move_down():
        '''
        This function is called if the down arrow key is pressed. This
        function then calls the merge_down() to perform the merge operation
        and updates the score. It then calls the draw() to display the matrix
        in the turtle window. After that, it checks the status of the game and
        if the game is over displays the appropriate message in the turtle
        window by calling the rules()

        Parameter:
            none

        Return:
            none
        '''

        nonlocal matrix
        nonlocal score
        # calling the merge_down()
        merged_matrix, point = merge_down(matrix)
        score += point
        if matrix != merged_matrix:
            matrix = game_start(merged_matrix, 1, board_size)
            draw_board(matrix, board_size, score)
            game_status = game_state(matrix)
            if game_status != 'Playing':
                rules(game_status)

    def move_up():
        '''
        This function is called if the up arrow key is pressed. This
        function then calls the merge_up() to perform the merge operation
        and updates the score. It then calls the draw() to display the matrix
        in the turtle window. After that, it checks the status of the game and
        if the game is over displays the appropriate message in the turtle
        window by calling the rules()

        Parameter:
            none

        Return:
            none
        '''

        nonlocal matrix
        nonlocal score
        # calling the merge_up()
        merged_matrix, point = merge_up(matrix)
        score += point
        if matrix != merged_matrix:
            matrix = game_start(merged_matrix, 1, board_size)
            draw_board(matrix, board_size, score)
            game_status = game_state(matrix)
            if game_status != 'Playing':
                rules(game_status)

    def quit_game():
        '''
        This function is called when the key 'q' is pressed, this function
        closes the turtle window and ends the program.
        Parameter:
            none

        Return:
            none
        '''
        # command to close the turtle window and end the program
        turtle.bye()

    def reset_game():
        '''
        This function is called if the key 'r' is pressed. This function
        resets the game by creating a new matrix and assigns two random
        values (2 or 4), and initialise the score to zero.
        Parameter:
            none
        Return:
            none
        '''

        nonlocal matrix
        nonlocal score
        # creating a new matrix
        matrix = initialising_matrix(board_size)
        # assigning two random values
        matrix = game_start(matrix, 2, board_size)
        # initialising the score to zero
        score = 0
        # update on the turtle screen
        draw_board(matrix, board_size, score)

    # call the relevant function for each key press
    turtle.onkey(move_right, "Right")
    turtle.onkey(move_left, "Left")
    turtle.onkey(move_down, "Down")
    turtle.onkey(move_up,'Up')
    turtle.onkey(quit_game, 'q')
    turtle.onkey(reset_game, 'r')

    # keep listening in the turtle window for the input
    turtle.listen()
