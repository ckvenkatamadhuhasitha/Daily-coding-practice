# Problem: Prime Numbers in a Given Range

# -----------------------------
# Approach: Optimized (√n)
# -----------------------------
# Time Complexity: O(n√n)
# Space Complexity: O(1)

a = int(input('Enter start: '))
b = int(input('Enter end: '))

for i in range(a, b + 1):
    if i <= 1:
        continue
    flag = 1
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:
        print(i)
