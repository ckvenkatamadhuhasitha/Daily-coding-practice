# Problem: Octal to Decimal Conversion

# -----------------------------
# Optimised (Mathematical Logic)
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

octal_num = int(input('Enter an octal number: '))
decimal_num = 0
base = 1

while octal_num != 0:
    rem = octal_num % 10
    decimal_num = decimal_num + rem * base
    base = base * 8
    octal_num = octal_num // 10

print(decimal_num)


# -----------------------------
# Optimised (Built-in Function)
# -----------------------------
# Time Complexity: O(d)
# Space Complexity: O(1)

octal_num = input('Enter an octal number: ')
decimal_num = int(octal_num, 8)
print(decimal_num)