# A stub for printMonth may look like this 
def printMonth(year, month): 
    print("printMonth")
  
# A stub for printMonthTitle may look like this 
def printMonthTitle(year, month): 
    print("printMonthTitle")

# A stub for getMonthBody may look like this 
def printMonthBody(year, month): 
    print("printMonthBody")

# A stub for getMonthName may look like this 
def getMonthName(month): 
    print("getMonthName")

# A stub for getStartDay may look like this 
def getStartDay(year, month): 
    print("getStartDay")

# A stub for getTotalNumberOfDays may look like this 
def getTotalNumberOfDays(year, month):
    days = 0
    for i in range(1800, year):
        if isLeapYear(y):
            days += 366
        else:
            days += 365
    for m in range(1,month):
        days += getNumberOfDaysInMonth(year, m)
    return days


# A stub for getNumberOfDaysInMonth may look like this 
def getNumberOfDaysInMonth(year, month): 
    # year = 2016, month = 2
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    if isLeapYear(year):
        days_in_month[1] = 29

    return days_in_month[month - 1]


# A stub for isLeapYear may look like this 
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    # Prompt the user to enter year and month 
    year = int(input("Enter full year (e.g., 2001): "))
    month = int(input((
        "Enter month as number between 1 and 12: ")))

    # Print calendar for the month of the year
    printMonth(year, month)
 
main()
