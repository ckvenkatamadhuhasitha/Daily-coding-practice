# Problem: Leap Year Check

# -----------------------------
# Approach: Divisibility Rules
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

year = int(input('Enter year: '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('Leap Year')
else:
    print('Not a Leap Year')
