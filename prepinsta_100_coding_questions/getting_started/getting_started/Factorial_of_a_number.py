# Problem: Factorial of a Number

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(f'Factorial of {num} is {fact}')
