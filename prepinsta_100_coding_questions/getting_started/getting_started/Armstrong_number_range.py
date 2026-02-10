# Problem: Armstrong Numbers in a Given Range

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n · d)
# Space Complexity: O(1)

a = int(input('Enter start: '))
b = int(input('Enter end'))

for i in range(a, b + 1):
    temp = i
    pow = len(str(i))
    sum = 0
    while temp != 0:
        rem = temp % 10
        sum = sum + rem ** pow
        temp = temp // 10
    if i == sum:
        print(i)
