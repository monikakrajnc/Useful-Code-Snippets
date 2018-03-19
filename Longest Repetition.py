# longest_repetition takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.


def longest_repetition(list):
    n = len(list)
    i = 0           #best element so far
    a = 0           #current element, we are counting
    count = 1       #counting the current element
    num = 0         #the longest lasting element
    if n == 0:      #If the input list is empty
        return None
    for entry in list:     #counting number of each element in the list
        if entry == a:
            count = count + 1
        else:
            count = 1
            a = entry
        if count > num:      #if current counting is bigger than previous the biggest counting, 
            i = a            #then current counting of a specific number becomes the longest
            num = count
    return i        #the element that has the most consecutive repetitions



print(longest_repetition([[1], [2, 2], [2, 2], [2, 2], [3, 3, 3]]))

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None
