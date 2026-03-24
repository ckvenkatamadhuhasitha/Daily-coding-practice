# Problem: Count Number of Digits

# -----------------------------
# Approach 1: Basic
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
count = 0

while num > 0:
    num = num // 10
    count += 1

print(count)


# -----------------------------
# Approach 2: Handling Edge Cases
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
count = 0

if num < 0:
    num = num * (-1) # For cleaner code we can write --> num = abs(num)

if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1

print(count)