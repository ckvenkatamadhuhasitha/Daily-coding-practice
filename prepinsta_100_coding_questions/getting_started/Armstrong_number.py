# Problem: Armstrong Number

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
pow = len(str(num))
temp = num
sum = 0

while num != 0:
    rem = num % 10
    sum = sum + rem ** pow
    num = num // 10

if temp == sum:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
