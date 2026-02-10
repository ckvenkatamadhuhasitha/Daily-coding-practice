# Problem: Nth Fibonacci Number

# -----------------------------
# Approach 1: Brute Force (List)
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)

num = int(input("Enter a number: "))
fibo_list = []
fibo1, fibo2 = 0, 1

for _ in range(num):
    fibo_list.append(fibo1)
    fibo1, fibo2 = fibo2, fibo1 + fibo2

print(fibo_list[num-1])


# -----------------------------
# Approach 2: Optimized
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input("Enter a number: "))
fibo1, fibo2 = 0, 1

if num == 1:
    print(fibo1)
elif num == 2:
    print(fibo2)
else:
    for _ in range(3, num + 1):
        fibo1, fibo2 = fibo2, fibo1 + fibo2
    print(fibo2)
