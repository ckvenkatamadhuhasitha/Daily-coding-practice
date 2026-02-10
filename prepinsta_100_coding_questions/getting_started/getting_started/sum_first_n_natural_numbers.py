# Problem: Sum of First N Natural Numbers

# -----------------------------
# Approach: Iterative Sum
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
sum = 0

for i in range(1, num + 1):
    sum = sum + i

print(f'Sum of {num} natural numbers is {sum}')
