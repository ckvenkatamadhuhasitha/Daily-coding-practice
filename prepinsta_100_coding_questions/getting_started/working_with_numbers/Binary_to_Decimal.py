# Problem: Binary to Decimal Conversion

# -----------------------------
# Optimised (Mathematic Logic)
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

binary_num = int(input('Enter a binary number: '))
decimal_num = 0
power = 0
base = 1

while binary_num != 0:
    rem = binary_num % 10
    decimal_num = decimal_num + rem * base
    base = base * 2
    binary_num = binary_num // 10

print(decimal_num)


# -----------------------------
# Optimised (Built-in Function)
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

binary_num = input('Enter a binary number: ')
decimal_num = int(binary_num, 2)
print(decimal_num)