# Deep Count 

# deep_count takes as input a list, and outputs the total number of elements 
# in the list, including all elements in lists that it contains.

def is_list(p):
    return isinstance(p, list)

# This returns True if the input is a List, and returns False otherwise.

def deep_count(p):
	if is_list(p):    #check if input is a list
		r = len(p)
	for i in p:             # for each element in p, check if it is a list
		if is_list(i):
			r = r + deep_count(i)      #sum lengths of all lists
	return r


# Examples

print deep_count([1, 2, 3])
#>>> 3

# The empty list still counts as an element of the outer list
print deep_count([1, [], 3]) 
#>>> 3 

print deep_count([1, [1, 2, [3, 4]]])
#>>> 7

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
#>>> 10
