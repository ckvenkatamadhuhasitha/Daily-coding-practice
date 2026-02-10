# Problem: Sum of Digits of a Number

# -----------------------------
# Approach: Digit Extraction
# -----------------------------
# Time Complexity: O(d), where d is number of digits
# Space Complexity: O(1)

num = int(input('Enter a number: '))
temp = num
sum = 0

while num != 0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

print(f'The sum of digits of {temp} is {sum}')
