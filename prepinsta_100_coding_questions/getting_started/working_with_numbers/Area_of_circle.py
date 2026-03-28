# Problem: Area of a Circle

# -----------------------------
# Approach 1: Using Radius
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

from math import pi

radius = int(input('Enter Radius(cm): '))
area = pi * radius * radius
print(f'Area of Circle : {area:.2f}')


# -----------------------------
# Approach 2: Using Diameter
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

diameter = int(input('Enter diameter(cm): '))
area = (pi * diameter * diameter) / 4
print(f'Area of Circle : {area:.2f}')