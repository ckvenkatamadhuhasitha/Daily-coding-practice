# Problem: Factors of a Number

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(√n)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        if i != num:
            print(i)
        if num // i != i:
            print(num // i)
