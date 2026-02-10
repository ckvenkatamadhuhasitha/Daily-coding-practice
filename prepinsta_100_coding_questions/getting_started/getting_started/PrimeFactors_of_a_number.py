# Problem: Prime Factors of a Number

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n²)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
for i in range(2, num + 1):
    if num % i == 0:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i)

# -----------------------------
# Optimised
# -----------------------------
# Time Complexity: O(n√n)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
for i in range(2, num + 1):
    if num % i == 0:
        flag = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i)
