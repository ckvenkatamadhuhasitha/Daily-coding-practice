# Problem: Automorphic Number
# Example: 25 → 25² = 625 → ends with 25

# -----------------------------
# Approach 1: Brute Force (Using Inbuilt Functions)
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(d)

num = input('Enter a number: ')
sqr = str(int(num) ** 2)

if sqr.endswith(num):
    print('Automorphic number')
else:
    print('Not an Automorphic number')

# -----------------------------
# Approach 2: Optimized
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
square = num ** 2
power = 10 ** (len(str(num)))
print(power)

if square % power == num:
    print('Automorphic number')
else:
    print('Not an Automorphic number')
