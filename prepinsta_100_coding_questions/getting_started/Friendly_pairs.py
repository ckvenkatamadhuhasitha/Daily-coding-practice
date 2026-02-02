# Problem: Friendly Pairs
# Example: (6, 28)
# Factors of 6  → 1, 2, 3  → sum = 6
# Factors of 28 → 1, 2, 4, 7, 14 → sum = 28
# sum1 / num1 == sum2 / num2 → Friendly Pairs

# -----------------------------
# Optimized Approach
# -----------------------------
# Time Complexity: O(√n + √m)
# Space Complexity: O(1)

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
sum1, sum2 = 0, 0

for i in range(1, (int(num1**0.5)) + 1):
    if num1 % i == 0:
        if i != num1:
            sum1 = sum1 + i
        if num1 // i != i and num1 // i != num1:
            sum1 = sum1 + (num1 // i)

for i in range(1, (int(num2**0.5)) + 1):
    if num2 % i == 0:
        if i != num2:
            sum2 = sum2 + i
        if num2 // i != i and num2 // i != num2:
            sum2 = sum2 + (num2 // i)

if sum1 * num2 == sum2 * num1: # used this instead of (sum1/num1 == sum2/num2) to avoid floating point conflicts
    print('Friendly Pairs')
else:
    print('Not Friendly Pairs')

