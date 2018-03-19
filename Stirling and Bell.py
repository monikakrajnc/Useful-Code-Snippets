# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group 
# of people Dave, Sarah, Peter and Andy could be split into two groups in 
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# so S(4,2) = 7

# If instead we split the group into one group, we have just one way to 
# do it.

# 1. Dave, Sarah, Peter, Andy

# so S(4,1) = 1

# or into four groups, there is just one way to do it as well

# 1. Dave        Sarah          Peter         Andy

# so S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n 
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# stirling takes as its inputs two positive integers of which the first is the 
# number of items and the second is the number of sets into which those 
# items will be split. The second procedure, bell, takes as input a 
# positive integer n and returns the Bell number B(n).

#n = number of items
#k = number of sets (items will be split)
#if k = 1 or k = n, then items can be split into one set (in one way)
#if n is smaller than k, then items cannot be split

def stirling(n, k): 
    if k == 1:
        return k
    if n == k:
        return 1
    if n < k:
        return 0
    else:
        m = k * stirling(n-1, k) + stirling(n-1, k-1)
        return m    

#count = the number of ways of splitting n into any number of parts
def bell(n):
    count = 0
    k = 1
    while k <= n:
        a = stirling(n, k)        #ways of splitting n (number of items)       
        count = count + a
        k = k + 1                #change k, add one set
    return count

# or as in the video:
def stirling(n, k):
    if n < k:
        return 0
    if n == k or k == 1:
        return 1
    return k*stirling(n-1, k) + stirling(n-1, k-1)

def bell(n):
    total = 0
    for k in range(1, n+1):
        total = total + stirling(n, k)
    return total


#print stirling(1,1)
#>>> 1
#print stirling(2,1)
#>>> 1
#print stirling(2,2)
#>>> 1
#print stirling(2,3)
#>>>0

#print stirling(3,1)
#>>> 1
#print stirling(3,2)
#>>> 3
#print stirling(3,3)
#>>> 1

#print stirling(4,1)
#>>> 1
#print stirling(4,2)
#>>> 7
#print stirling(4,3)
#>>> 6
#print stirling(4,4)
#>>> 1

#print stirling(5,1)
#>>> 1
#print stirling(5,2)
#>>> 15
#print stirling(5,3)
#>>> 25
print stirling(5,4)
#>>> 10
#print stirling(5,5)
#>>> 1

print stirling(20,15)
#>>> 452329200

print bell(1)
#>>> 1
print bell(2)
#>>> 2
print bell(3)
#>>> 5
print bell(4)
#>>> 15
print bell(5)
#>>> 52
print bell(15)
#>>> 1382958545
