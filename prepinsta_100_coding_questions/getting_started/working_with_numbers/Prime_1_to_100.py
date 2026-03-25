# Problem: Prime Numbers up to N

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n²)
# Space Complexity: O(1)

num = 100

for i in range(1, num + 1):
    if i <= 1:
        continue
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end=' ')


# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(n√n)
# Space Complexity: O(1)

num = 100

print(2, end=' ')

for i in range(3, num + 1, 2):
    flag = 0
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i, end=' ')