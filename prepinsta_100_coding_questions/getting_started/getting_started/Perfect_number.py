# Problem: Perfect Number
# Example: 28 → 1 + 2 + 4 + 7 + 14 = 28

# -----------------------------
# Approach 1: Brute Force
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# -----------------------------
# Approach 2: Optimized
# -----------------------------
# Time Complexity: O(√n)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
sum = 0

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        if i != num:
            sum += i
        if num // i != i and num // i != num:
            sum += num // i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
