# Problem: Palindrome Number

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(d)

num = int(input('Enter a number: '))
rev = int(str(num)[::-1])
if num == rev:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')

# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
temp = num
sum = 0
while num != 0:
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10

if temp == sum:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')
