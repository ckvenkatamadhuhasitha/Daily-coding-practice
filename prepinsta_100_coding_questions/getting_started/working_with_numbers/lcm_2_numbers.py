# Problem: LCM of Two Numbers

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n × m)
# Space Complexity: O(1)

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
lcm = 0

for i in range(max(num1, num2), (num1 * num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break

print(lcm)


# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(log(min(n, m)))
# Space Complexity: O(1)

import math
num1 = int(input('Enter number: '))
num2 = int(input('Enter another number: '))
lcm = math.lcm(num1, num2)
print(lcm)
