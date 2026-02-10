# Problem: Power of a Number

# -----------------------------
# Approach 1
# -----------------------------
# Time Complexity: O(p)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
power = int(input('Enter power'))
answer = 1

for i in range(0, power):
    answer = answer * num

print(answer)

# -----------------------------
# Approach 2
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
power = int(input('Enter power'))
print(num ** power)
