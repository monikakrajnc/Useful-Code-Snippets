# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# rabbits() takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.



def rabbits(n):
    k = [0, 1, 1]
    if n < 2:            #if n is 0 or 1 return that number
        return n
    if n == 2:
        return k[n]
    else:
        for i in range(3, 6):            #start with 2, because 0 and 1 are already in k
            v = k[i - 1] + k[i - 2]      #new number is the sum of two previous ones
            k.append(v)                  #add new number to k
        for i in range(6, n + 1):        #after they are 5 months old, they die
            v = k[i - 1] + k[i - 2] - k[i - 5]
            k.append(v)
    return k[n]


#or - video solution
def rabbits(n):
    if n < 1:          #no rabbits dead yet
        return 0
    else:
        if n == 1 or n == 2:     #base case defined in problem statement
            return 1
        else:
            return rabbits(n-1) + rabbits(n-2) - rabbits(n-5)      #formula from problem statement. Don't need formula without the last člen, because if n<5, potem je ta člen 0

print (rabbits(10))
#>>> 35

#s = ""
#for i in range(1,12):
#    s = s + str(rabbits(i)) + " "
#print s
#>>> 1 1 2 3 5 7 11 16 24 35 52
