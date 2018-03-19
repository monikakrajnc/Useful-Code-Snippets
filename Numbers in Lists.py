# This procedure takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

def numbers_in_lists(string):
    n = len(string)
    i = 0
    list = [int(string[0])]              #add first number to the list as an integer
    sublist = []
    while i < n - 1:
        if int(string[i + 1]) > int(string[i]):     #if number i is smaller than next number in the string(i+1),
            if string[i] in list:                   #check if number i is already in the list and 
                list.append(int(string[i + 1]))     #add next number (i+1) to the list
            else:
                if int(string[i + 1]) > list[len(list)-1]:     #check, if the next number (i+1) is bigger than the last number in the list
                    if len(sublist) !=0:                       #if the sublist is not empty,
                        list.append(sublist)                   #add sublist to the list and then add next number (i+1) to the list
                        list.append(int(string[i+1]))
                        sublist = []                           #make an empty sublist for the next round
                    else:
                        list.append(int(string[i+1]))          #in case sublist is empty, add nuxt number (i+1) to the list
                else:
                    sublist.append(int(string[i+1]))           #if next number is equal to or smaller than last number in the list, add next number to the sublist
        if int(string[i]) >= int(string[i+1]):      #if the number x is bigger than or equal to next number (x+1), add next number to sublist
            sublist.append(int(string[i+1]))
        i = i + 1
    if len(sublist) > 0:                            #before finishing, check if the sublist is not empty, if it's not add it to the list
        list.append(sublist)
    return list


#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
