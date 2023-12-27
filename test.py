'''
Pranav Kanth Anbarasan
CS5001, Spring 2023
Project
This program incorporates the UnitTesting module and checks whether all the
functions returns value that is expected, we then compare the outcomes with
assert statements.
'''
# importing the unittest module
import unittest
# importing all the required files
from merge_matrix import *
from game_status import *
from matrix import *
from turtle_screen import *

class Test_game(unittest.TestCase):
    '''
    This Test_game Class Comprises methods that checks whether
    the values expected and the resulting values from all the
    functions are equal.
    '''

    def test_merge_right(self):
        '''
        This method tests whether the merge_right() works correctly by
        passing in a matrix to the merge_right() and comparing the returned
        result with the expected_result with the help of assertEqual statement.
        '''

        # testing with same and different adjacent elements
        matrix = [[0, 0, 0, 8], [0, 4, 0, 4], [2, 0, 4, 8], [4, 2, 0, 16]]
        expected_result = ([[0, 0, 0, 8], [0, 0, 0, 8], [0, 2, 4, 8], [0, 4, 2, 16]], 8)
        self.assertEqual(merge_right(matrix), expected_result)

        # testing with same and different adjacent elements
        matrix_2 = [[8, 0, 0, 8], [4, 4, 0, 4], [2, 0, 8, 8], [4, 2, 0, 16]]
        expected_result_2 = ([[0, 0, 0, 16], [0, 0, 4, 8], [0, 0, 2, 16], [0, 4, 2, 16]], 40)
        self.assertEqual(merge_right(matrix_2), expected_result_2)

    def test_merge_left(self):
        '''
        This method tests whether the merge_left() works correctly by
        passing in a matrix to the merge_left() and comparing the returned
        result with the expected_result with the help of assertEqual statement.
        '''
        # testing without same adjacent elements
        matrix = [[0, 0, 0, 8],[0, 8, 0, 4],[0, 0, 4, 8], [0, 0, 0, 16]]
        expected_result = ([[8, 0, 0, 0], [8, 4, 0, 0], [4, 8, 0, 0], [16, 0, 0, 0]], 0)
        self.assertEqual(merge_left(matrix), expected_result)

        # testing with same adjacent elements
        matrix_2 = [[0, 0, 8, 8], [0, 8, 4, 4], [2, 2, 8, 8], [4, 4, 16, 16]]
        expected_result_2 = ([[16, 0, 0, 0], [8, 8, 0, 0], [4, 16, 0, 0], [8, 32, 0, 0]], 84)
        self.assertEqual(merge_left(matrix_2), expected_result_2)

    def test_merge_down(self):
        '''
        This method tests whether the merge_down() works correctly by
        passing in a matrix to the merge_down() and comparing the returned
        result with the expected_result with the help of assertEqual statement.
        '''
        # testing without same adjacent elements
        matrix = [[0, 0, 2,4], [0, 0, 0, 8],[0, 0, 0, 0], [2, 4, 0, 0]]
        expected_result = ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4], [2, 4, 2, 8]], 0)
        self.assertEqual(merge_down(matrix), expected_result)

        # testing with same adjacent elements
        matrix_2 = [[2, 8, 8, 16], [4, 8, 16, 16], [2, 4, 8, 4], [2, 4, 16, 8]]
        expected_result_2 = ([[0, 0, 8, 0], [2, 0, 16, 32], [4, 16, 8, 4], [4, 8, 16, 8]], 60)
        self.assertEqual(merge_down(matrix_2), expected_result_2)

    def test_merge_up(self):
        '''
        This method tests whether the merge_up() works correctly by
        passing in a matrix to the merge_up() and comparing the returned
        result with the expected_result with the help of assertEqual statement.
        '''
        # testing without same adjacent element
        matrix = [[0, 0, 0, 0], [0, 2, 0, 4], [8, 0, 0, 16], [32, 4, 512, 0]]
        expected_result = ([[8, 2, 512, 4],[32, 4, 0, 16], [0, 0, 0, 0], [0, 0, 0, 0]], 0)
        self.assertEqual(merge_up(matrix), expected_result)

        # testing with same adjacent elements
        matrix_2 = [[0, 4, 16, 8], [4, 4, 16, 4], [8, 32, 4, 2], [8, 2, 4, 2]]
        expected_result_2 = ([[4, 8, 32, 8], [16, 32, 8, 4], [0, 2, 0, 4], [0, 0, 0, 0]], 68)
        self.assertEqual(merge_up(matrix_2), expected_result_2)

    def test_game_status(self):
        '''
        This method tests whether the value returned from the game_state()
        is the same as expected value using the assertEqual statement
        '''

        # if the matrix has the element 2048, should return you won!! Congrats
        matrix = [[0, 0, 0, 0], [0, 2, 0, 4], [8, 0, 0, 16], [32, 4, 512, 2048]]
        expected_result = "You won!! Congrats"
        self.assertEqual(game_state(matrix),expected_result)

        # if the player can still play
        matrix_2 = [[2, 4, 8, 16], [4, 2, 2, 4], [8, 0, 8, 16], [8, 4, 512, 512]]
        expected_result_2 = 'Playing'
        self.assertEqual(game_state(matrix_2), expected_result_2)

        # if the board is full but atleast one adjacent element is identical
        matrix_3 = [[2, 4, 8, 16], [4, 2, 2, 4], [8, 4, 8, 16], [8, 4, 512, 512]]
        expected_result_3 = 'Playing'
        self.assertEqual(game_state(matrix_3), expected_result_3)

        # if the board is full and no further moves are possible
        matrix_4 = [[4, 8], [16, 4]]
        expected_result_4 = 'You Lose!! Better Luck Next Time'
        self.assertEqual(game_state(matrix_4), expected_result_4)

    def test_matrix(self):
        '''
        This method tests, when the input size of the board is passed onto the
        initialising_matrix(), the returned matrix is the same as the expected
        output, using assertEqual statements.
        '''

        # when the input size is 2
        size = 2
        expected_output = [[0,0],[0,0]]
        self.assertEqual(initialising_matrix(size),expected_output)
        # when the inout size is 5
        size_2 = 5
        expected_output_2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.assertEqual(initialising_matrix(size_2),expected_output_2)

    def test_random_element(self):
        '''
        This method tests whether the non-zero numbers returned from the game_start()
        is the same as expected_value, when the attributes (matrix, limit, board_size)
        are passed on to game_start() when calling.
        '''
        # checking whether adding single random element works
        matrix = [[0, 0,0],[0,0,0],[0,0,0]]
        output_matrix = game_start(matrix,1,3)
        count = 0
        for row in range(len(output_matrix)):
            for column in range((len(output_matrix))):
                value = output_matrix[row][column]
                if value != 0:
                    count += 1
        self.assertEqual(count, 1)

        # checking whether adding three random elements works
        matrix_2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        output_matrix_2 = game_start(matrix_2, 3, 4)
        count = 0
        for row in range(len(output_matrix_2)):
            for column in range((len(output_matrix_2))):
                value = output_matrix_2[row][column]
                if value != 0:
                    count += 1
        self.assertEqual(count, 3)

    def test_reverse_matrix(self):
        '''
        This method tests whether the matrix returned from the reverse_list()
        is the same as the expected_output, using the assertEqual statement.
        '''
        matrix = [[2,0,4],[4,4,8],[8,8,4]]
        expected_output = [[8, 8, 4], [4, 4, 8], [2, 0, 4]]
        self.assertEqual(reverse_list(matrix),expected_output)

# test driver
def main():
    unittest.main()

if __name__ == '__main__':
    main()


