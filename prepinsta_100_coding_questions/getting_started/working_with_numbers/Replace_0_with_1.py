# Problem: Replace all 0's with 1 in a Number

# -----------------------------
# Approach: Digit Manipulation
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
temp = 0

if num == 0:
    temp = 1

while num > 0:
    rem = num % 10
    if rem == 0:
        rem = 1
    num = num // 10
    temp = temp * 10 + rem

num = 0

while temp > 0:
    rem = temp % 10
    temp = temp // 10
    num = num * 10 + rem

print(num)