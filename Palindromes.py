# is_palindrome takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    n = len(s)
    i = 0
    k = n - 1
    count = 0
    if s == "":           #base Case
        return True
    while i < n:
        if s[i] == s[k - i]:      #first and last characters match
            count =  count + 1
        i = i + 1
    if count == n:     #the string is a palindrome
        return True
    else:
        return False
 
or
def is_palindrome(s):
    if s == "":
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1 : -1])
        else:
            return False

or
#if we have bigger input, use iterative
def iter_palindrome(s):
    for i in range(0, len(s)/2):  #go throught the fisrt half of the string, it has to be a mirror image of the second half
        if s[i] != s[-(i+1)]:     #if first and last characters don't match
            return False
    return True

 
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True
