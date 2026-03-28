# Problem: Maximum Number of Handshakes

# -----------------------------
# Brute Force
# -----------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)

num = int(input('Enter no.of persons in room: '))
handshakes = 0

for i in range(1, num):
    handshakes = handshakes + i

print(f'The maximum no.of handshakes: {handshakes}')


# -----------------------------
# Optimised (Mathematical Logic)
# -----------------------------
# Time Complexity: O(1)
# Space Complexity: O(1)

num = int(input('Enter no.of persons in room: '))

if num == 0 or num == 1:
    handshakes = 0
    print(f'The maximum no.of handshakes: {handshakes}')
elif num < 0:
    print('Enter a valid number')
else:
    handshakes = (num * (num - 1)) // 2
    print(f'The maximum no.of handshakes: {handshakes}')