# Given your birthday and the current date, this calculates your age in days. 
# Accounts for leap days. 
#
# It assumes that the birthday and current date are correct dates (and no 
# time travel). 

#check if it is a leap year
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

#find how many days has a specific month
def daysInMonth(year, month):
    # if month in (1, 3, 5, 7, 8, 10, 12)
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:    #if month is February, check if it is a leap year
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30

#find "tomorrow" for the input
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
#print nextDay(1999, 12, 30)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    # return True if year1, month1, day1 is before year2, month2, day2. Otherwise, returns False.
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

               

def daysBetweenDates(year1, month1, day1, year2, month2, day2):    #returns the number of days between year1/month1/day1 and year2/month2/day2.
    days = 0                                                       #Assumes inputs are valid dates in Gregorian calendar.  program defensively! add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def my_test():
        #assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
        assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
        #assert nextDay(2013, 1, 1) == (2013, 1, 2)
        #assert nextDay(2013, 4, 30) == (2013, 5, 1)
        #assert nextDay(2012, 12, 31) == (2013, 1, 1)
        #assert nextDay(2013, 2, 28) == (2013, 3, 1)
        #assert nextDay(2013, 9, 30) == (2013, 10, 1)
        #assert nextDay(2012, 2, 28) == (2012, 2, 29)
        assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366
        assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365
        assert daysBetweenDates(2013, 1, 24, 2013, 6, 29) == 156
        print("Tests finished")

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

#test()
print(test())

