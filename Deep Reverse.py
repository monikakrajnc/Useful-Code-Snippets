# deep_reverse takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# The procedure is_list below returns True if 
# p is a list and False if it is not.

#check if it is a list
def is_list(p):
    return isinstance(p, list)


def deep_reverse(q):
    if is_list(q):
        new_list = []
        for entry in q[::-1]:     #start with the last element 
            new_list.append(deep_reverse(entry))
        return new_list      #reverse list of the input list
    else:
        return q       #return input, if it is not a list


#Examples

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
#print q
#>>> [1, [2,3], 4, [5,6]]
