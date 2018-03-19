# Given a list of lists representing a n * n matrix as input, 
# this procedure returns True if the input is an identity matrix 
# and False otherwise.

import numpy as np

def is_identity_matrix(matrix):
    n = len(matrix)
    i = 0
    if n != len(matrix[0]):   #if the length of the matrix is not the same as length of the first element
        return False          #it is not an identity matrix
    if matrix[0][0] != 1:     #if the first element in a row and column is not 1
        return False          #it is not an identity matrix        
    else:
        while i < n:          #check if is in each row and column just one element 1
            if matrix[i] == [row[i] for row in matrix] and sum(matrix[i]) == 1:
                i = i + 1
            else:
                return False   #it is not an identity matrix
        return True            #it is an identity matrix
   



# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,1],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False           

           
