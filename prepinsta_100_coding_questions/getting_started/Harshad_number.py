# Problem: Harshad (Niven) Number
# Example: 21 → 2 + 1 = 3 → 21 is divisible by 3

# -----------------------------
# Approach: Optimal
# -----------------------------
# Time Complexity: O(d), where d is number of digits
# Space Complexity: O(1)
# Note: Further optimization is not possible.

num = int(input("Enter a number: "))
digit_sum = 0
temp = num

while num != 0:
    rem = num % 10
    digit_sum += rem
    num //= 10

if temp % digit_sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
