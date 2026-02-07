# Problem: Prime Number Check

# -----------------------------
# Approach: Brute Force
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
flag = 1

for i in range(2, num):
    if num % i == 0:
        flag = 0
        break

if flag == 1:
    print('Prime Number')
else:
    print('Not a Prime Number')
