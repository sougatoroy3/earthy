def is_leap(year):
    #leap = False
    
    # Write your logic here
    #return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

year = int(input())