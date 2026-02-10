# Problem: HCF of Two Numbers

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(min(n, m))
# Space Complexity: O(1)

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
hcf = 0

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print(hcf)


# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(log(min(n, m)))
# Space Complexity: O(1)

import math
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
hcf = math.gcd(num1, num2)
print(hcf)
