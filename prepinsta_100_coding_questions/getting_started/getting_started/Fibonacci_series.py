# Problem: Fibonacci Series (Range)

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

fibo_range = int(input('Enter a range: '))
fibo1 = 0
fibo2 = 1

for i in range(0, fibo_range):
    print(fibo1, end=' ')
    new = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = new
