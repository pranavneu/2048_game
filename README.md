# 2048 Game in Python
Pranav Kanth Anbarasan  
CS5001, Spring 2023  
Project (2048)  

### Instructions on how to run the program:
1. Unzip the contents of the submitted file.
2. The file consists of 7 python programs (main.py, game_status.py, matrix.py, merge_matrix.py, turtle_controls.py, turtle_screen.py, test.py) and one read_me text file.
3. In order to open the game, run the main.py file in IDLE.
4. Enter the number of rows or columns you want in your 2048 board, in the IDLE window. It should be between 4 to 6, else will throw a ValueError.
5. The turtle window will open up allowing you to play the game with the help of the arrow keys in your keyboard.
6. If you wish to restart the game press 'r' in your keyboard.
7. If you wish to quit the game press 'q' in your keyboard.

### Features of the program:
1. Asking the user to enter the size of the board between 4 and 6 and creating a game of that dimension. 
2. The game will be able to shift elements inside the table in all the four directions (left, right, up, down).
3. The player will use the arrow keys to play the game.
4. The game will keep track of the score and display it on the board at all times.
5. If the player wants to end the game, he can just press the letter 'q' to quit the game.
6. If the player wants to restart the game, the player can just press the letter 'r'.
7. The direction to play, quit and restart the game is always visible on the turtle window.
8. If the user presses any keys other than what the game uses, the game will not be affected.
9. The program will not crash when the user enters an invalid value for the size of the board, instead the program will raise a ValueError.
10. The cells will be highlighted in different colour, when they merge.

### Program design:  
**main.py:**  
Functions : board_size() - This function asks the user to enter the size of the board between 4 and 6. If any other values are entered, the function raises a ValueError.  
main() -  This is the main function for the entire program, it calls the initialising_matrix(), game_start(), draw_board() and controls()  

**turtle_controls.py:**  
This Program uses the turtle module to get the predefined inputs (Left, Right, Up or Down) and call the relevant merge functions for that input and displays the matrix in the turtle window.  
Functions:  
controls() - uses the turtle.listen() and if any of the appropriate keys are pressed ('Up', 'Down', 'Left', 'Right', 'q', 'r'), calls the appropriate function for that key.  
move_right() - This function shifts elements in the matrix to the right, updates the score. If the two cells have the same number, the numbers are merged. It then checks the status of the game, whether the player has won or lost or can he keep playing and the player can keep playing it calls the draw() to display the resultant matrix in the turtle window.  
move_left() - This function shifts elements in the matrix to the left, updates the score. If the two cells have the same number, the numbers are merged. It then checks the status of the game, whether the player has won or lost or can he keep playing and the player can keep playing it calls the draw() to display the resultant matrix in the turtle window.  
move_down() - This function shifts elements in the matrix down, updates the score. If the two cells have the same number, the numbers are merged. It then checks the status of the game, whether the player has won or lost or can he keep playing and the player can keep playing it calls the draw() to display the resultant matrix in the turtle window.  
move_up() - This function shifts elements in the matrix up, updates the score. If the two cells have the same number, the numbers are merged. It then checks the status of the game, whether the player has won or lost or can he keep playing and the player can keep playing it calls the draw() to display the resultant matrix in the turtle window.  
quit_game() - This function closes the turtle window and ends the program, if the letter 'q' is pressed.  
reset_game() - This function resets the game and the score if the user presses the key 'r'.  

**game_status.py:**  
This program checks the status of the game and if any one of the numbers in matrix equals to 2048 it will print 'You won!!' or if you are not able to make any more moves and there is no space left,  it prints 'You lose' and ends the game.  
Functions:  
game_state_helper() - This is a helper function for the game_state() and if the matrix is filled with numbers, then checks if any of the adjacent numbers are equal (left,right,up,down) and if it is same then the function returns True.  
game_state() - This function checks if any of the number in the matrix equals to 2048 or if there is empty space in the matrix by checking for zero's, it also has the helper function to check if the adjacent elements are equal and returns the appropriate message depending on the scenario to the calling function.

**merge_matrix.py:**  
This program shifts the number in left, right, up or down to the end when they just have zero or if the two adjacent numbers are same they merge to become twice that number, the remaining cells  are filled with zero and the result is returned to the calling function.  
Functions : merge_right(), merge_left(), merge_down(), merge_up()    
Helper functions : reverse_matrix_helper() and transpose_matrix_helper()  

**turtle_screen.py** 
This program is used to draw the 2048 board in the turtle module and updates the score accordingly in the turtle module. It also displays the rules in the turtle module. This program also holds the color palate which displays distinct color for each number.  
Functions : color_palate(), draw_board(), rules(), reverse_list()  






