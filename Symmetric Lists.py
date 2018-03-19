# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(list):
    n = len(list)
    i = 0
    count = 0
    #Check if the list is empty, if length "n" is zero
    if n==0:
        return True
    #Check if the list has the same number of rows as columns
    #If length of the list is not the same as the length of the sublist, means the list is not symmetric
    if n != len(list[0]):
        return False
    while i < n:
        #count = 0
        if list[i] == [row[i] for row in list]:
            count = count + 1
        i = i +1
    if count == n:
        return True
    else:
        return False

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                [2,3,1]])
#>>> False

print symmetric([['cricket', 'football', 'tennis'], ['golf']])
print symmetric([])
