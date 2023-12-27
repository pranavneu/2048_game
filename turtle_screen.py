'''
Pranav Kanth Anbarasan
CS5001, Spring 2023
Project
This program is used to draw the 2048 board in the turtle module and updates
the score accordingly in the turtle module. It also displays the rules in the
turtle module. This program also holds the color palate which displays
distinct color for each number.
'''

# importing turtle module
import turtle

def color_palate(value):
    '''
    This function holds distinct colors for each number and when the
    value of the number is passed this function returns the appropriate
    color to the calling function.
    Parameter:
        Value (int): The value as an integer for which the color is to
            be fetched.

    Return:
        color_map[value] (string): The color that is returned to the calling
            function for the appropriate value.

    Precondition: The value should be inputted as an integer.
    Postcondition: The returned color_map[value] should be a string.
    '''

    # dictionary containing number as key and color as value
    color_map = {
        0: "white smoke",
        2: "silver",
        4: "powder blue",
        8: "pale goldenrod",
        16: "tan",
        32: "light steel blue",
        64: "peach puff",
        128: "misty rose",
        256: "lavender",
        512: "burlywood",
        1024: "pale turquoise",
        2048: "alice blue"
    }

    # return color for that value
    return color_map[value]

def draw_board(matrix, board_size, score):
    '''
    This function draws the turtle 2048 board and displays the score
    in the turtle window. The turtle window also displays the matrix in
    each appropriate square on the turtle 2048 square board.
    Parameters:
        matrix (nested_list): contains the numbers in a nested list,
            example: [[0,0,0,8],[0,4,0,0],[2,0,4,8],[4,2,0,16]].

        board_size (int): The size of the board to be drawn on the turtle
            window, which is inputted from the user.

        score (int): The score that is returned from the controls()

    Precondition: the matrix should be a nested list, board_size and score
        is an integer.
    '''

    screen = turtle.Screen()
    screen.setup(1000, 1000)
    screen.title("2048 Game Board")
    screen.tracer(0)
    # clear the turtle window
    turtle.clear()
    turtle.penup()
    rules('none')
    turtle.goto(300, 300)
    # print the score in turtle window
    text = f'Score: {score}'
    turtle.write(text, align="left", font=("Times New Roman", 25, "normal"))
    # calling the reverse matrix function
    matrix = reverse_list(matrix)
    turtle.penup()
    turtle.speed(0)
    turtle.hideturtle()
    # define the tile size
    tile_size = 50

    # Drawing the board
    for i in range(board_size):
        for j in range(board_size):
            # Get the value of the current tile in the matrix
            value = matrix[i][j]
            x_axis = j * 50
            y_axis = i * 50
            turtle.goto(x_axis, y_axis)
            color = color_palate(value)
            turtle.color('black', color)
            turtle.begin_fill()
            # drawing a square
            for count in range(4):
                turtle.pendown()
                turtle.forward(tile_size)
                turtle.left(90)
                turtle.penup()
            turtle.end_fill()
            # Display the value in the tile if not zero
            if value != 0:
                turtle.goto(x_axis + tile_size / 2, y_axis + tile_size / 2)
                turtle.write(value, align="center", font=("Arial", 20, "bold"))

    screen.tracer(1)

def rules(game_status):
    '''
    This function displays the rules of the game in the turtle window,all
    the time. It also displays a message in the window if you lose or win
    the game.
    Parameter:
        game_status (String): If the string is not none, display the message
            onto the turtle window.
    Return:
        none

    Precondition: the game_status parameter should be an integer.
    '''
    # all the rules saved into a variable
    rules = ('Instructions: \n 1.Press Q to quit. \n 2.Press R to restart. \n 3.Press'
             ' "Right" arrow key to move right \n 4.Press "Left" arrow key to move left \n'
             ' 5.Press "Up" arrow key to move up \n 6.Press "Down" arrow key to move down')
    turtle.goto(-490, 200)
    # write the rules in the turtle window
    turtle.write(rules, align="left", font=("Times New Roman", 25, "normal"))
    turtle.goto(-100, -200)
    # conditional statement to check the game status
    if game_status != 'none':
        turtle.color('red')
        # printing the game status
        turtle.write(game_status, align="left", font=("Times New Roman", 35, "normal"))
        turtle.color('black')

def reverse_list(matrix):
    '''
    This function reverses the matrix, so that the matrix in the
    turtle board appears in the same order as the matrix paramerter.
    Parameter:
        matrix (nested_list):  contains the numbers in a nested list, example:
        [[0,0,0,8],[0,4,0,0],[2,0,4,8], [4,2,0,16]].
    Return:
        none

    Precondition: The inputted matrix must be a nested_list.
    '''
    # to appended to the new list
    reverse_list = []
    # reversing the matrix
    index = -1
    for i in range(len(matrix)):
        reverse_list.append(matrix[index])
        index -= 1
    return reverse_list
