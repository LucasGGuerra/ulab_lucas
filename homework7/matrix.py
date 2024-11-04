#this module is used to perform matrix operations such as row reductions on matrices.
import numpy as np

def simple_diagonalization(array):
    """
    Takes in an array and reduces it to have ones along the diagonal of the 'matrix.'
    I realize now this function has like no practical implications lol.
    Input: Array
    Output: modified array with ones along its columns
    """
    shape = array.shape
    empty_array = np.empty((0, shape[1]), float)
    index = 0
    for list in array:
        list = list/list[index]
        empty_array = np.append(empty_array, np.array([list]), axis=0)
        index = index + 1
    return empty_array


def row_reduction(array):
    """
    Takes in an array with 1's along the diagonal and row reduces it into reduced row echelon form
    First, the array is checked for it's size, and then the algorithm normalizes each row in the matrix with respect to the diagonal term
    If the diagonal term is equal to zero, the algorithm skips the current iteration
    Next, the column is rescaled to solve the system by elimination, adding multiples of itself to generate 0s along the column except for the diagonal
    After the row reduction occurs, the matrix is stored and used for the next round of row reduction
    This took hours :sob:
    Input: Array
    Output: Upper Triangular Array
    """
    shape = array.shape
    empty_array = np.empty((0, shape[1]), float)
    for row in range(shape[0]):
        if array[row, row] == 0:
            continue
        for column in range(shape[0]): #this nested loop iterates like 00 01 02, 10 11 12, 20 21 22 for a 3xN matrix.
            list = array[row] / array[row, row] #need to reset list after each iteration
            if column == row:
                empty_array = np.append(empty_array, np.array([list]), axis=0)
                continue
            else:
                scalar = -1 * array[column, row] #we want it to access the same row value but a different column value.
                list = scalar * list
                list = list + array[column]
                empty_array = np.append(empty_array, np.array([list]), axis=0)     
        array = empty_array
        empty_array = np.empty((0, shape[1]), float)
    return array


def solution_set(array, solution_set):
    """
    This function is meant to find the solution vector to an augmented matrix by row-reducing the array
    First, we identify the shape of the original matrix, and set our free_variable list, free_variable_presence, and row-reduced array
    Next, we augment our matrix to contain the solution column vector.
    Next, we row-reduce our matrix using the row_reduction() function defined above
    lastly, we detect any free variables and piece together our solutions by appending them as strings to the solution_list
    Input: Array, List
    Output: List
    Constraints: The solution_set must have the same dimensions as the array otherwise it will return out of bounds
    """
    shape = array.shape
    free_variables = []
    free_variable_presence = False
    empty_array = np.empty((0, shape[1]+1), float) #make sure to add one to the shape of the array because you are adding on an additional column.
    solution_list = [] #make sure to note that the type of class you will add to the array is a string.
    if shape[0] == len(solution_set):
        for row in range(shape[0]):
            list = []
            for column in range(shape[1]):
                list.append(array[row, column])
            list.append(solution_set[row])
            empty_array = np.append(empty_array, np.array([list]), axis=0)
        empty_array = row_reduction(empty_array) #this gives us our RREF solution matrix. Now we need to return our solutions
        for row in range(empty_array.shape[0]):
            if empty_array[row, row] == 0:
                free_variables.append(row)
                free_variable_presence = True
        for row in range(empty_array.shape[0]):
            solution = "Variable " + str(row+1) + ' = ' + str(empty_array[row, -1])
            if free_variable_presence == True:
                for free_variable in free_variables:
                    solution = solution + ' + ' + str(empty_array[row, free_variable]) + "*(x sub " + str(free_variable+1) + ")"
                    if row == free_variable:
                        solution = "Variable " + str(row+1) + " is a free variable."
            solution_list.append(solution)
    else:
        return np.array(["Solution Set out of bounds"])
    return solution_list





















        