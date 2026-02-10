# Problem: Strong Number
# Example: 145 → 1! + 4! + 5! = 145

# -----------------------------
# Approach 1: Brute Force
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
temp = num
sum = 0

while num != 0:
    rem = num % 10
    fact = 1
    for i in range(1, rem + 1):
        fact *= i
    sum += fact
    num //= 10

if temp == sum:
    print("Strong Number")
else:
    print("Not a Strong Number")


# -----------------------------
# Approach 2: Optimized
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
fact_list = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
temp = num
sum = 0

while num != 0:
    rem = num % 10
    sum += fact_list[rem]
    num //= 10

if temp == sum:
    print("Strong Number")
else:
    print("Not a Strong Number")
