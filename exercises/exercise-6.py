# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

def print_season():
    month = input('Enter the three-character month of the year (Jan - Dec): ')
    if month in ('Jan', 'Feb', 'Mar'):
        season = 'Winter'
    elif month in ('Apr', 'May', 'Jun'):
        season = 'Spring'
    elif month in ('Jul', 'Aug', 'Sep'):
        season = 'Summer'
    elif month in ('Oct', 'Nov', 'Dec'):
        season = 'Fall'
    else:
        print('Month entered is invalid. Please try again with a three-character month.')
        return print_season()
    day = int(input('Enter the day of the month: '))
    if day < 1 or day > 31:
        day = int(input('Invalid day number. Enter the day of the month (1-31): '))
    if month == 'Dec' and day > 20:
        season = 'Winter'
    elif month == 'Mar' and day > 19:
        season = 'Spring'
    elif month == 'Jun' and day > 20:
        season = 'Summer'
    elif month == 'Sep' and day > 21:
        season = 'Fall'
    print(f'{month} {day} is in {season}')

print_season()