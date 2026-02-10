# Problem: Reverse a Number

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(d)

num = int(input('Enter a number: '))
rev = int(str(num)[::-1])
print(rev)

# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
sum = 0
while num != 0:
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10
print(sum)
