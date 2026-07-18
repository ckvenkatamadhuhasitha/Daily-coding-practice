# Problem: Add Two Fractions

# -----------------------------
# Method 1: Direct Cross Multiplication (Brute Force)
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

num1 = int(input('Enter numerator: '))
denom1 = int(input('Enter denominator: '))
num2 = int(input('Enter numerator: '))
denom2 = int(input('Enter denominator: '))

numerator = num1 * denom2 + num2 * denom1
denominator = denom1 * denom2

print(f'{numerator}/{denominator}')


# -----------------------------
# Method 2: LCM + Fraction Reduction (Optimized)
# -----------------------------
# Time Complexity: O(min(d₁, d₂) + min(sum, lcm))
# Space Complexity: O(1)

def GCD(n1, n2):
    gcd = 0
    for i in range(1, int(min(n1, n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

num1, den1 = map(int, list(input("Enter numerator and denominator: ").split(" ")))
num2, den2 = map(int, list(input("Enter numerator and denominator: ").split(" ")))

lcm = (den1 * den2) // GCD(den1, den2)
sum = (num1 * lcm // den1) + (num2 * lcm // den2)

numerator = sum // GCD(sum, lcm)
denominator = lcm // GCD(sum, lcm)

print(f'{numerator}/{denominator}')