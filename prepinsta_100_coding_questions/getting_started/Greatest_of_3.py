# Problem: Greatest of Three Numbers

# -----------------------------
# Approach: Conditional Comparison
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a > b and a > c:
    print(f'{a} is greater')
elif b > c:
    print(f'{b} is greater')
else:
    print(f'{c} is greater')
