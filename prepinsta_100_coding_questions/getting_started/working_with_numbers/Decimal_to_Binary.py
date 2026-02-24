# Problem: Decimal to Binary Conversion

# -----------------------------
# Optimised (Mathematic Logic)
# -----------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)

decimal_num = int(input('Enter a number: '))
binary_num = 0
i = 1

while decimal_num != 0:
    rem = decimal_num % 2
    binary_num = binary_num + rem * i
    decimal_num = decimal_num // 2
    i *= 10

print(binary_num)


# -----------------------------
# Optimised (Built-in Function)
# -----------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)

decimal_num = int(input('Enter a number: '))
binary_num = bin(decimal_num)[2:]   # To remove prefix '0b'
print(binary_num)
