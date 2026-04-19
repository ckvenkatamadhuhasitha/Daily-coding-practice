# Problem: Count Occurrences of a Digit in a Number

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(d)

num = int(input('Enter a number: '))
digit = int(input('Enter a digit to count: '))

print(str(num).count(str(digit)))


# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
digit = int(input('Enter a digit to count: '))
count = 0

if num == 0:
    if digit == 0:
        print(1)
    else:
        print(0)
elif digit < 0 or digit > 9:
    print('Please enter digit correctly')
else:
    if num < 0:
        num = num * (-1)
    while num > 0:
        rem = num % 10
        if rem == digit:
            count += 1
        num = num // 10
    print(count)