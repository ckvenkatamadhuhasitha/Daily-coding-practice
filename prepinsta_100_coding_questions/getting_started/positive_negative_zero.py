# Problem: Positive, Negative or Zero

# -----------------------------
# Approach: Conditional Check
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

num = int(input('Enter a number: '))
if num <= 0:
    if num == 0:
        print('Zero')
    else:
        print('Negative')
else:
    print('Positive')
