# check_sudoku takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(list):
	n = len(list)
	digit = 1       #because each row and column starts with 1
	while digit <= n:
		i = 0       #represents row
		while i < n:
			row_count = 0
			col_count = 0
			j = 0  #represents column
			while j < n:
				if list[i][j] == digit:
					row_count = row_count + 1
				if list[j][i] == digit:
					col_count = col_count + 1
				j = j + 1      #change a column, row (i) stays the same
			if row_count != 1 or col_count != 1:    #if a digit is not just once in a whole row or column
				return False
			i = i + 1         #go to the next row
		digit = digit + 1         #check the next number
	return True




    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False

				
				
