# Problem: Number of Days in a Month

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

month = int(input('Enter a month: '))
year = int(input('Enter a year: '))

if (month == 2 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
    print('29 Days')
elif (month == 2):
    print('28 Days')
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print('31 Days')
else:
    print('30 Days')


# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

month = int(input('Enter a month: '))
year = int(input('Enter a year: '))

leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
set_mon = {1, 3, 5, 7, 8, 10, 12}

if (month < 1 or month > 12):
    print('Enter valid month')
elif (month == 2 and leap):
    print('29 Days')
elif (month == 2):
    print('28 Days')
elif (month in set_mon):
    print('31 days')
else:
    print('30 Days')