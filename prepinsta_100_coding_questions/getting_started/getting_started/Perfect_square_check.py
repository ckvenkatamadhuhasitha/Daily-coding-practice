# Problem: Perfect Square Check

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
root = num ** 0.5
print(root)

if num == (root ** 2):
    print('Perfect Square')
else:
    print('Not a perfect square')

# -----------------------------
# Optimised and Safe
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

import math
num = int(input('Enter a number: '))
root = int(math.sqrt(num))
print(root)

if num == (root ** 2):
    print('Perfect Square')
else:
    print('Not a perfect square')
