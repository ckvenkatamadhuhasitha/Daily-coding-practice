# Problem: Sum of Natural Numbers in a Given Range

# -----------------------------
# Approach: Iterative Range Sum
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num1 = int(input('Enter starting number: '))
num2 = int(input('Enter ending number: '))
sum = 0

for i in range(num1, num2 + 1):
    sum = sum + i

print(f'Sum natural numbers from {num1} to {num2} is {sum}')
