# Problem: Abundant Number
# Example: 12 → 1 + 2 + 3 + 4 + 6 = 16 → 16 > 12

# -----------------------------
# Approach 1: Brute Force
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
div_sum = 0

for i in range(1, num):
    if num % i == 0:
        div_sum += i

if div_sum > num:
    print("Abundant Number")
else:
    print("Not an Abundant Number")

    
# -----------------------------
# Approach 2: Optimized
# -----------------------------
# Time Complexity: O(√n)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
div_sum = 0

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        if i != num:
            div_sum += i
        if num // i != i and num // i != num:
            div_sum += num // i

if div_sum > num:
    print("Abundant Number")
else:
    print("Not an Abundant Number")
