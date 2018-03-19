# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def triangle(n):
    list = []
    if n == 0:    #if the input is not positive integer, return empty list
        return list
    if n == 1:    #if the input is number 1, then there is just one sublist with number 1 inside
        sublist = [1]
        list.append(sublist)
        return list
    if n == 2:
        list = triangle(1)     #result of the input is number 1
        sublist = [1, 1]
        list.append(sublist)
    else:      #if the input number is bigger than 2
        list = [[1], [1, 1]]
        b = 1
        while b < n - 1:       #calculating numbers in places in list between the first and last place
            count = 0
            sublist = [1]      #first element in the sublist is always number 1
            k = 1
            while k <= b:
                a = list[b][k-1] + list[b][k]    #Each number (a) is the sum of the number above it to the left and the number above it to the right
                sublist.append(a)
                count = count + 1
                k = k + 1
            if count == b:   #that means we just need to add last number, which is always 1      
                d = 1
                sublist.append(d)
                list.append(sublist)
            b = b + 1
    return list          #the first n rows in the triangle


#or as in video:

def make_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for unused in range(0, n):
        result.append(current)
        current = make_next_row(current)
    return result

#For example:

print triangle(0)
#>>> []

print triangle(1)
#>>> [[1]]

print triangle(2)
#>> [[1], [1, 1]]

print triangle(3)
#>>> [[1], [1, 1], [1, 2, 1]]

print triangle(6)
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
