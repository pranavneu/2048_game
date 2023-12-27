'''
Pranav Kanth Anbarasan
CS5001, Spring 2023
Project
This program shifts the number in left, right, up or down to the end when
they just have zero or if the two adjacent numbers are same they merge
to become twice that number, the remaining cells  are filled with zero
and the result is returned to the calling function.
'''

def merge_right(matrix):
    '''
    This function is called if the 'right' key on the keyboard is pressed.
    This function slides each number to its right to occupy the farthest blank
    cell (denoted by 0 in matrix) without jumping over another number in the
    same row.If two cells in the same row shift next to each other and they
    both have the same number, the numbers are merged and placed in the cell
    that is on the right.
    Parameters:
        matrix (nested list): contains the numbers in a nested list,
            example: [[0,0,0,8],[0,4,0,0],[2,0,4,8],[4,2,0,16]].

    Return:
        point (int): add twice all the elements that are identical and merged
            and return to the calling function.
        merged_matrix (nested list): the matrix that is returned to the calling
            function.

    Precondition: The input matrix must be a nested list
    Postcondition: The matrix returned must be a nested list and the point
        returned must be an integer.
    '''
    # creating an empty matrix to append the result
    merged_matrix = []
    # initialising the point to zero
    point = 0
    for row in matrix:
        # storing the non-zero numbers of each row in a list
        non_zero = [num for num in row if num != 0]
        result = []
        while non_zero:
            # popping elements from non-zero
            current = non_zero.pop()
            # if current and last element of non-zero are equal merge them
            if non_zero and current == non_zero[-1]:
                current += non_zero.pop()
                point += current
                # append the element to result
            result.insert(0, current)
            # fill the remaining row with 0 on the front
        single_row = [0] * (len(row) - len(result)) + result
        # append the single_row with the merged_matrix
        merged_matrix.append(single_row)

    return merged_matrix, point

def merge_left(matrix):
    '''
    This function is called if the 'left' key on the keyboard is pressed.
    This function slides each number to its left to occupy the farthest blank
    cell (denoted by 0 in matrix) without jumping over another number in the
    same row.If two cells in the same row shift next to each other and they
    both have the same number, the numbers are merged and placed in the cell
    that is on the left.
    Parameters:
        matrix (nested list):contains the numbers
            in a nested list, example: [[0,0,0,8],[0,4,0,0],[2,0,4,8],
            [4,2,0,16]].

    Return:
        point (int): add twice all the elements that are identical and merged
            and return to the calling function.
        marged_matrix (nested list): the matrix that is returned to the calling
            function.

    Precondition: The input matrix must be a nested list
    Postcondition: The matrix returned must be a nested list and the point
        returned must be an integer.
    '''
    # creating an empty matrix to append the result
    merged_matrix = []
    # initialising the point to zero
    point = 0
    for row in matrix:
        # storing the non-zero numbers of each row in a list
        non_zero = [num for num in row if num != 0]
        result = []
        while non_zero:
            # popping the first element
            current = non_zero.pop(0)
            # comparing the current with first element of non_zero
            if non_zero and current == non_zero[0]:
                current += non_zero.pop(0)
                # updating the point
                point += current
            # appending the current element to result
            result.append(current)
        # adding zero's to the remaining places
        single_row = result + [0] * (len(row) - len(result))
        # appending the single row to the merged_matrix
        merged_matrix.append(single_row)

    return merged_matrix, point

def reverse_matrix_helper(matrix):
    '''
    This helper function helps to reverse the rows as columns so that left
    and right merge can be performed on the appropriate elements

    Parameter:
        matrix (nested list):contains the numbers in a nested list, example:
        [[0,0,0,8],[0,4,0,0],[2,0,4,8], [4,2,0,16]].

    Return:
        new_matrix (nested_list): the reversed list that is either
            merged left or right.

    Precondition: The input matrix must be a nested list.
    Postcondition: The returned matrix is nested list.
    '''
    # creating new matrix
    new_matrix = []
    # reversing the rows as columns
    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]
        new_matrix.append(column)
    return new_matrix

def transpose_matrix_helper(matrix):
    '''
    This helper function helps to convert the merged rows into columns
    which is then returned to the merged_up or merged_down function.

    Parameter:
        matrix (nested list): contains the numbers in a nested list, example:
        [[0,0,0,8],[0,4,0,0],[2,0,4,8], [4,2,0,16]].

    Return:
         transposed_matrix (nested list): the reversed list, where the row is
            transposed into columns.

    Precondition: The input matrix must be a nested list.
    Postcondition: The returned matrix is a nested list.
    '''
    # convert rows into columns
    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix

def merge_down(matrix):
    '''
    This function is called if the 'down' key on the keyboard is pressed.
    This function slides each number down to occupy the farthest blank
    cell (denoted by 0 in matrix) without jumping over another number in the
    same column.If two cells in the same row shift next to each other and they
    both have the same number, the numbers are merged and placed in the cell
    that is down. This is achieved by making use of two helper functions
    reverse_matrix_helper() and transpose_matrix_helper().

    Parameter:
        matrix (nested list): contains the numbers in a nested list, example:
        [[0,0,0,8],[0,4,0,0],[2,0,4,8], [4,2,0,16]].

    Return:
        point (int): add twice all the elements that are identical and merged
            and return to the calling function.
        transposed_matrix (nested list): the matrix that is returned to the calling
            function.

    Precondition: The input matrix must be a nested list
    Postcondition: The matrix returned must be a nested list and the point
        returned must be an integer.
    '''
    # calling the reverse_matrix_helper()
    new_matrix = reverse_matrix_helper(matrix)
    # merge_right function call
    merged,point = merge_right(new_matrix)
    # transposed_matrix function call
    transposed_matrix = transpose_matrix_helper(merged)
    return transposed_matrix, point


def merge_up(matrix):
    '''
    This function is called if the 'Up' key on the keyboard is pressed.
    This function slides each number up to occupy the farthest blank
    cell (denoted by 0 in matrix) without jumping over another number in the
    same column.If two cells in the same row shift next to each other and they
    both have the same number, the numbers are merged and placed in the cell
    that is up. This is achieved by making use of two helper functions
    reverse_matrix_helper() and transpose_matrix_helper().

    Parameter:
        matrix (nested list): contains the numbers in a nested list, example:
        [[0,0,0,8],[0,4,0,0],[2,0,4,8], [4,2,0,16]].

    Return:
        point (int): add twice all the elements that are identical and merged
            and return to the calling function.
        transposed_matrix (nested list): the matrix that is returned to the calling
            function.

    Precondition: The input matrix must be a nested list.
    Postcondition: The matrix returned must be a nested list and the point
        returned must be an integer.
    '''
    # reverse_matrix_helper function call
    new_matrix = reverse_matrix_helper(matrix)
    # merge_left function call
    merged, point = merge_left(new_matrix)
    # transpose_matrix_helper function call
    transposed_matrix = transpose_matrix_helper(merged)
    return transposed_matrix, point
